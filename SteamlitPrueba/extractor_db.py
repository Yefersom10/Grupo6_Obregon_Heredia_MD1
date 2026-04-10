#!/usr/bin/env python3


from dotenv import load_dotenv
load_dotenv()

from scripts.extractor import WeatherstackExtractor
from scripts.loader import guardar_datos_en_bd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        extractor = WeatherstackExtractor()
        datos     = extractor.ejecutar_extraccion()

        if datos:
            resumen = guardar_datos_en_bd(datos)
            print(f"\n✅ ETL completado")
            print(f"   Ciudades procesadas : {len(datos)}")
            print(f"   Registros guardados : {resumen['guardados']}")
            print(f"   Fallidos            : {resumen['fallidos']}")
            print(f"   Tiempo              : {resumen['tiempo']}s")
        else:
            print("⚠️  No se obtuvieron datos de la API.")

    except Exception as e:
        logger.error(f"Error en ETL: {e}")
        raise