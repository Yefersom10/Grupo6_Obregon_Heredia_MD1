#!/usr/bin/env python3
import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
from scripts.loader import guardar_datos_en_bd
import logging

# Cargar .env
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/etl.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MovieExtractor:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.base_url = os.getenv('BASE_URL')
        self.peliculas = [p.strip() for p in os.getenv('PELICULAS', '').split(',')]

        if not self.api_key:
            raise ValueError("API_KEY no configurada en .env")

    def extraer_pelicula(self, pelicula):
        try:
            params = {
                'apikey': self.api_key,
                't': pelicula.strip()
            }

            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data.get("Response") == "False":
                logger.error(f"[ERROR] API para {pelicula}: {data.get('Error')}")
                return None

            logger.info(f"[OK] Datos extraidos para {pelicula}")
            return data

        except Exception as e:
            logger.error(f"[ERROR] Extrayendo datos para {pelicula}: {str(e)}")
            return None

    def procesar_respuesta(self, response_data):
        try:
            return {
                'titulo': response_data.get('Title'),
                'anio': response_data.get('Year'),
                'genero': response_data.get('Genre'),
                'director': response_data.get('Director'),
                'actores': response_data.get('Actors'),
                'duracion': response_data.get('Runtime'),
                'calificacion_imdb': response_data.get('imdbRating'),
                'recaudacion': response_data.get('BoxOffice'),
                'idioma': response_data.get('Language'),
                'pais': response_data.get('Country'),
                'fecha_extraccion': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"[ERROR] Procesando respuesta: {str(e)}")
            return None

    def ejecutar_extraccion(self):
        datos_extraidos = []
        logger.info(f"Iniciando extraccion para {len(self.peliculas)} peliculas...")

        for pelicula in self.peliculas:
            response = self.extraer_pelicula(pelicula)
            if response:
                datos_procesados = self.procesar_respuesta(response)
                if datos_procesados:
                    datos_extraidos.append(datos_procesados)
            time.sleep(1)

        return datos_extraidos


if __name__ == "__main__":
    try:
        extractor = MovieExtractor()
        datos = extractor.ejecutar_extraccion()

        if datos:
            guardar_datos_en_bd(datos)

        print("Proceso ETL completado correctamente.")

    except Exception as e:
        logger.error(f"[ERROR] En extraccion: {str(e)}")