#!/usr/bin/env python3

from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

import os, requests, logging, time
from datetime import datetime
from scripts.loader import guardar_datos_en_bd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class WeatherstackExtractor:
    def __init__(self):
        self.api_key  = os.getenv("API_KEY")
        self.base_url = os.getenv("WEATHERSTACK_BASE_URL", "http://api.weatherstack.com")
        ciudades_env  = os.getenv("CIUDADES", "")
        self.ciudades = [c.strip() for c in ciudades_env.split(",") if c.strip()]
        if not self.api_key:
            raise ValueError("❌ API_KEY no configurada en .env")
        logger.info(f"Extractor listo — {len(self.ciudades)} ciudades: {self.ciudades}")

    def extraer_clima(self, ciudad: str) -> dict | None:
        try:
            r = requests.get(f"{self.base_url}/current",
                             params={"access_key": self.api_key, "query": ciudad},
                             timeout=10)
            r.raise_for_status()
            data = r.json()
            if "error" in data:
                logger.error(f"API error {ciudad}: {data['error'].get('info')}")
                return None
            logger.info(f"✅ {ciudad}")
            return data
        except Exception as e:
            logger.error(f"Error {ciudad}: {e}")
            return None

    def procesar(self, data: dict) -> dict | None:
        try:
            c = data.get("current", {})
            l = data.get("location", {})
            return {
                "ciudad"           : l.get("name", "Desconocida"),
                "pais"             : l.get("country", "Desconocido"),
                "latitud"          : float(l.get("lat", 0) or 0),
                "longitud"         : float(l.get("lon", 0) or 0),
                "temperatura"      : float(c.get("temperature", 0)),
                "sensacion_termica": float(c.get("feelslike", 0)),
                "humedad"          : float(c.get("humidity", 0)),
                "velocidad_viento" : float(c.get("wind_speed", 0)),
                "descripcion"      : c.get("weather_descriptions", ["N/A"])[0],
                "codigo_tiempo"    : c.get("weather_code"),
                "fecha_extraccion" : datetime.now().isoformat(),
            }
        except Exception as e:
            logger.error(f"Error procesando: {e}")
            return None

    def ejecutar(self) -> list[dict]:
        resultados = []
        for ciudad in self.ciudades:
            raw = self.extraer_clima(ciudad)
            if raw:
                p = self.procesar(raw)
                if p:
                    resultados.append(p)
            time.sleep(1)   # evita 429 en plan gratuito
        logger.info(f"Extracción: {len(resultados)}/{len(self.ciudades)} exitosas")
        return resultados


if __name__ == "__main__":
    extractor = WeatherstackExtractor()
    datos     = extractor.ejecutar()
    if datos:
        resumen = guardar_datos_en_bd(datos)
        print(f"\n✅ ETL completado — {resumen['guardados']} ciudades guardadas ({resumen['tiempo']}s)")
    else:
        print("⚠️  No se obtuvieron datos.")