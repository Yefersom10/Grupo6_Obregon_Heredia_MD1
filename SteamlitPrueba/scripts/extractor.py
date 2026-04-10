#!/usr/bin/env python3
import os
import requests
import logging
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class WeatherstackExtractor:
    def __init__(self):
        self.api_key  = os.getenv("API_KEY")
        self.base_url = os.getenv("WEATHERSTACK_BASE_URL", "http://api.weatherstack.com")

        ciudades_env = os.getenv("CIUDADES", "")
        if not ciudades_env:
            raise ValueError("❌ CIUDADES no definida en .env")

        self.ciudades = [c.strip() for c in ciudades_env.split(",") if c.strip()]

        if not self.api_key:
            raise ValueError("❌ API_KEY no configurada en .env")

        logger.info(f"Extractor listo — {len(self.ciudades)} ciudades: {self.ciudades}")

    # ------------------------------------------------------------------ #
    def extraer_clima(self, ciudad: str) -> dict | None:
        """Llama a la API de Weatherstack y retorna el JSON crudo."""
        try:
            url    = f"{self.base_url}/current"
            params = {"access_key": self.api_key, "query": ciudad}

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            if "error" in data:
                logger.error(f"API error para {ciudad}: {data['error'].get('info')}")
                return None

            logger.info(f"✅ Datos recibidos para {ciudad}")
            return data

        except Exception as e:
            logger.error(f"Error extrayendo {ciudad}: {e}")
            return None

    # ------------------------------------------------------------------ #
    def procesar_respuesta(self, data: dict) -> dict | None:
        """Transforma el JSON de la API al formato que espera el loader."""
        try:
            current  = data.get("current", {})
            location = data.get("location", {})

            return {
                "ciudad"           : location.get("name", "Desconocida"),
                "pais"             : location.get("country", "Desconocido"),
                "latitud"          : float(location.get("lat", 0) or 0),
                "longitud"         : float(location.get("lon", 0) or 0),
                "temperatura"      : float(current.get("temperature", 0)),
                "sensacion_termica": float(current.get("feelslike", 0)),
                "humedad"          : float(current.get("humidity", 0)),
                "velocidad_viento" : float(current.get("wind_speed", 0)),
                "descripcion"      : current.get("weather_descriptions", ["N/A"])[0],
                "codigo_tiempo"    : current.get("weather_code"),
                "fecha_extraccion" : datetime.now().isoformat(),
            }

        except Exception as e:
            logger.error(f"Error procesando respuesta: {e}")
            return None

    # ------------------------------------------------------------------ #
    def ejecutar_extraccion(self) -> list[dict]:
        """Extrae y procesa datos de todas las ciudades configuradas."""
        resultados = []
        logger.info(f"Iniciando extracción para {len(self.ciudades)} ciudades...")

        for ciudad in self.ciudades:
            raw = self.extraer_clima(ciudad)
            if raw:
                procesado = self.procesar_respuesta(raw)
                if procesado:
                    resultados.append(procesado)

        logger.info(f"Extracción completada — {len(resultados)}/{len(self.ciudades)} exitosas")
        return resultados


# ------------------------------------------------------------------ #
if __name__ == "__main__":
    from scripts.loader import guardar_datos_en_bd

    try:
        extractor = WeatherstackExtractor()
        datos     = extractor.ejecutar_extraccion()

        if datos:
            guardar_datos_en_bd(datos)
            print(f"✅ ETL completado — {len(datos)} ciudades guardadas.")
        else:
            print("⚠️  No se extrajeron datos.")

    except Exception as e:
        logger.error(f"Error fatal en extracción: {e}")
        raise