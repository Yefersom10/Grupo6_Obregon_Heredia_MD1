#!/usr/bin/env python3

from dotenv import load_dotenv
load_dotenv()

import logging
from scripts.database import SessionLocal
from scripts.models import RegistroClima

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def categorizar_temperatura(temp: float) -> str:
    if temp < 10:
        return "Frío"
    elif temp < 18:
        return "Fresco"
    elif temp < 26:
        return "Templado"
    else:
        return "Caliente"


def limpiar_y_transformar():
    db          = SessionLocal()
    actualizados = 0
    errores      = 0

    try:
        registros = db.query(RegistroClima).all()
        logger.info(f"Procesando {len(registros)} registros...")

        for r in registros:
            try:
                
                if r.humedad and not (0 <= r.humedad <= 100):
                    r.humedad = max(0, min(100, r.humedad))

                if r.velocidad_viento and r.velocidad_viento < 0:
                    r.velocidad_viento = 0

            
                if r.sensacion_termica is None and r.temperatura is not None:
                    r.sensacion_termica = round(r.temperatura - 1.5, 1)

                
                if r.descripcion:
                    r.descripcion = r.descripcion.strip().capitalize()

                actualizados += 1

            except Exception as e:
                errores += 1
                logger.warning(f"Error en registro {r.id}: {e}")

        db.commit()
        logger.info(f"✅ Transformación completada — {actualizados} actualizados, {errores} errores")
        return {"actualizados": actualizados, "errores": errores}

    except Exception as e:
        db.rollback()
        logger.error(f"Error crítico en transformación: {e}")
        raise

    finally:
        db.close()


if __name__ == "__main__":
    resultado = limpiar_y_transformar()
    print(f"\n✅ Transformación completada")
    print(f"   Registros actualizados : {resultado['actualizados']}")
    print(f"   Errores                : {resultado['errores']}")