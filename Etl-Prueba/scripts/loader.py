#!/usr/bin/env python3
from scripts.database import SessionLocal
from scripts.models import Ciudad, RegistroClima, MetricasETL
from datetime import datetime
import time
import logging

logger = logging.getLogger(__name__)

def guardar_datos_en_bd(datos):
    db = SessionLocal()
    inicio = time.time()
    guardados = 0
    fallidos = 0

    try:
        for item in datos:

            # Buscar o crear ciudad
            ciudad = db.query(Ciudad).filter_by(
                nombre=item["ciudad"]
            ).first()

            if not ciudad:
                ciudad = Ciudad(
                    nombre=item["ciudad"],
                    pais=item.get("pais"),
                    latitud=item.get("latitud"),
                    longitud=item.get("longitud")
                )
                db.add(ciudad)
                db.commit()
                db.refresh(ciudad)

            # Crear registro climatico
            nuevo_registro = RegistroClima(
                ciudad_id=ciudad.id,
                temperatura=item["temperatura"],
                sensacion_termica=item.get("sensacion_termica"),
                humedad=item["humedad"],
                velocidad_viento=item.get("velocidad_viento"),
                descripcion=item.get("descripcion"),
                codigo_tiempo=item.get("codigo_tiempo"),
                fecha_extraccion=datetime.fromisoformat(item["fecha_extraccion"]),
            )

            db.add(nuevo_registro)
            guardados += 1

        db.commit()
        logger.info("[OK] Datos guardados correctamente en la base de datos")

    except Exception as e:
        db.rollback()
        logger.error(f"[ERROR] Guardando en BD: {str(e)}")
        fallidos += 1

    finally:
        # Guardar metricas de ejecucion
        try:
            tiempo_total = time.time() - inicio
            estado = "SUCCESS" if fallidos == 0 else "PARTIAL"
            metrica = MetricasETL(
                registros_extraidos=len(datos),
                registros_guardados=guardados,
                registros_fallidos=fallidos,
                tiempo_ejecucion_segundos=tiempo_total,
                estado=estado,
                mensaje=f"Extraidos: {len(datos)}, Guardados: {guardados}, Fallidos: {fallidos}"
            )
            db.add(metrica)
            db.commit()
            logger.info("[OK] Metricas guardadas")
        except Exception as e:
            logger.error(f"[ERROR] Guardando metricas: {str(e)}")
        finally:
            db.close()