#!/usr/bin/env python3

import logging
import time
from datetime import datetime
from scripts.database import SessionLocal
from scripts.models import Ciudad, RegistroClima, MetricasETL

logger = logging.getLogger(__name__)


def guardar_datos_en_bd(datos: list[dict]) -> dict:
    db        = SessionLocal()
    guardados = 0
    fallidos  = 0
    inicio    = time.time()

    try:
        for item in datos:
            try:
                ciudad = db.query(Ciudad).filter_by(nombre=item["ciudad"]).first()
                if not ciudad:
                    ciudad = Ciudad(
                        nombre   = item["ciudad"],
                        pais     = item.get("pais", "Desconocido"),
                        latitud  = item.get("latitud"),
                        longitud = item.get("longitud"),
                        activa   = True,
                    )
                    db.add(ciudad)
                    db.flush()
                    logger.info(f"Ciudad nueva: {ciudad.nombre}")

                registro = RegistroClima(
                    ciudad_id         = ciudad.id,
                    temperatura       = item["temperatura"],
                    sensacion_termica = item.get("sensacion_termica"),
                    humedad           = item["humedad"],
                    velocidad_viento  = item["velocidad_viento"],
                    descripcion       = item.get("descripcion", "N/A"),
                    codigo_tiempo     = item.get("codigo_tiempo"),
                    fecha_extraccion  = datetime.fromisoformat(item["fecha_extraccion"]),
                    fecha_creacion    = datetime.utcnow(),
                )
                db.add(registro)
                guardados += 1

            except Exception as e:
                fallidos += 1
                logger.error(f"Error guardando {item.get('ciudad','?')}: {e}")

        tiempo_total = round(time.time() - inicio, 3)
        estado       = "exitoso" if fallidos == 0 else "parcial"

        db.add(MetricasETL(
            registros_extraidos       = len(datos),
            registros_guardados       = guardados,
            registros_fallidos        = fallidos,
            tiempo_ejecucion_segundos = tiempo_total,
            estado                    = estado,
            mensaje                   = f"{guardados} guardados, {fallidos} fallidos en {tiempo_total}s",
        ))
        db.commit()
        logger.info(f"✅ BD actualizada — {guardados} guardados, {fallidos} fallidos ({tiempo_total}s)")
        return {"guardados": guardados, "fallidos": fallidos, "tiempo": tiempo_total}

    except Exception as e:
        db.rollback()
        logger.error(f"Error crítico en loader: {e}")
        raise
    finally:
        db.close()