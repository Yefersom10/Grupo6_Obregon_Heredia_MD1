#!/usr/bin/env python3
from scripts.database import SessionLocal
from scripts.models import Pelicula, RegistroPeliculas, MetricasETL
from datetime import datetime
import time
import logging

logger = logging.getLogger(__name__)

def limpiar_duracion(duracion_str):
    """Convierte '148 min' a 148"""
    try:
        if duracion_str and duracion_str != 'N/A':
            return int(duracion_str.replace(' min', '').strip())
    except:
        pass
    return None

def limpiar_recaudacion(recaudacion_str):
    """Convierte '$858,373,000' a 858373000.0"""
    try:
        if recaudacion_str and recaudacion_str != 'N/A':
            return float(recaudacion_str.replace('$', '').replace(',', '').strip())
    except:
        pass
    return None

def limpiar_rating(rating_str):
    """Convierte '8.8' a 8.8"""
    try:
        if rating_str and rating_str != 'N/A':
            return float(rating_str)
    except:
        pass
    return None

def limpiar_anio(anio_str):
    """Convierte '2010' a 2010"""
    try:
        if anio_str and anio_str != 'N/A':
            return int(str(anio_str)[:4])
    except:
        pass
    return None

def guardar_datos_en_bd(datos):
    db = SessionLocal()
    inicio = time.time()
    guardados = 0
    fallidos = 0

    try:
        for item in datos:

            # Buscar o crear pelicula
            pelicula = db.query(Pelicula).filter_by(
                titulo=item["titulo"]
            ).first()

            if not pelicula:
                pelicula = Pelicula(titulo=item["titulo"])
                db.add(pelicula)
                db.commit()
                db.refresh(pelicula)

            # Crear registro
            nuevo_registro = RegistroPeliculas(
                pelicula_id=pelicula.id,
                anio=limpiar_anio(item.get("anio")),
                genero=item.get("genero"),
                director=item.get("director"),
                actores=item.get("actores"),
                imdb_rating=limpiar_rating(item.get("calificacion_imdb")),
                duracion=limpiar_duracion(item.get("duracion")),
                recaudacion=limpiar_recaudacion(item.get("recaudacion")),
                idioma=item.get("idioma"),
                pais=item.get("pais"),
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