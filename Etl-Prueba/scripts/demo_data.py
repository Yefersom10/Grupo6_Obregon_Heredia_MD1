#!/usr/bin/env python3

import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

from scripts.loader import guardar_datos_en_bd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# 5 ciudades colombianas con coordenadas reales
CIUDADES = [
    {"ciudad": "Bogota",       "pais": "Colombia", "latitud":  4.711, "longitud": -74.072},
    {"ciudad": "Medellin",     "pais": "Colombia", "latitud":  6.244, "longitud": -75.574},
    {"ciudad": "Cali",         "pais": "Colombia", "latitud":  3.431, "longitud": -76.522},
    {"ciudad": "Barranquilla", "pais": "Colombia", "latitud": 10.964, "longitud": -74.796},
    {"ciudad": "Cartagena",    "pais": "Colombia", "latitud": 10.391, "longitud": -75.479},
]

DESCRIPCIONES = ["Partly cloudy", "Clear", "Sunny", "Light rain",
                 "Overcast", "Fog", "Thunderstorm", "Drizzle"]
CODIGOS       = [116, 113, 113, 176, 119, 143, 200, 263]

# Temperatura base realista por ciudad
BASE_TEMP = {
    "Bogota": 14, "Medellin": 22, "Cali": 25,
    "Barranquilla": 30, "Cartagena": 31
}


def generar_registro(ciudad_info: dict, delta_horas: int) -> dict:
    temp = BASE_TEMP[ciudad_info["ciudad"]] + random.uniform(-4, 4)
    idx  = random.randint(0, len(DESCRIPCIONES) - 1)
    return {
        "ciudad"           : ciudad_info["ciudad"],
        "pais"             : ciudad_info["pais"],
        "latitud"          : ciudad_info["latitud"],
        "longitud"         : ciudad_info["longitud"],
        "temperatura"      : round(temp, 1),
        "sensacion_termica": round(temp - random.uniform(0, 3), 1),
        "humedad"          : round(random.uniform(40, 95), 1),
        "velocidad_viento" : round(random.uniform(5, 40), 1),
        "descripcion"      : DESCRIPCIONES[idx],
        "codigo_tiempo"    : CODIGOS[idx],
        "fecha_extraccion" : (datetime.now() - timedelta(hours=delta_horas)).isoformat(),
    }


def generar_datos_sinteticos(total: int = 1000) -> list[dict]:
    registros   = []
    por_ciudad  = total // len(CIUDADES)   # 200 por ciudad
    horas_rango = 720                      # 30 días hacia atrás

    for ciudad_info in CIUDADES:
        for _ in range(por_ciudad):
            registros.append(generar_registro(ciudad_info, random.randint(0, horas_rango)))

    # Completar si total no es múltiplo exacto
    while len(registros) < total:
        registros.append(generar_registro(random.choice(CIUDADES), random.randint(0, 720)))

    random.shuffle(registros)
    logger.info(f"Generados {len(registros)} registros sintéticos — {len(CIUDADES)} ciudades")
    return registros


if __name__ == "__main__":
    datos   = generar_datos_sinteticos(1000)
    resumen = guardar_datos_en_bd(datos)
    print(f"\n✅ Datos sintéticos cargados en PostgreSQL")
    print(f"   Total generado  : 1000")
    print(f"   Guardados en BD : {resumen['guardados']}")
    print(f"   Fallidos        : {resumen['fallidos']}")
    print(f"   Tiempo          : {resumen['tiempo']}s")