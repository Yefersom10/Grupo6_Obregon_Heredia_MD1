#!/usr/bin/env python3

import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

from scripts.loader import guardar_datos_en_bd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


CIUDADES = [
    {"ciudad": "Bogota",       "pais": "Colombia",  "latitud":  4.711,  "longitud": -74.072},
    {"ciudad": "Medellin",     "pais": "Colombia",  "latitud":  6.244,  "longitud": -75.574},
    {"ciudad": "Cali",         "pais": "Colombia",  "latitud":  3.431,  "longitud": -76.522},
    {"ciudad": "Barranquilla", "pais": "Colombia",  "latitud": 10.964,  "longitud": -74.796},
]

DESCRIPCIONES = [
    "Partly cloudy", "Clear", "Sunny", "Light rain",
    "Overcast", "Fog", "Thunderstorm", "Drizzle",
]

CODIGOS = [113, 116, 119, 122, 143, 176, 200, 263]


def generar_registro(ciudad_info: dict, delta_horas: int) -> dict:
    """Genera un registro sintético con variación realista."""
    base_temp = {"Bogota": 14, "Medellin": 22, "Cali": 25, "Barranquilla": 30}
    temp = base_temp.get(ciudad_info["ciudad"], 20) + random.uniform(-4, 4)
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
    registros      = []
    por_ciudad     = total // len(CIUDADES)
    horas_rango    = 720   

    for ciudad_info in CIUDADES:
        for i in range(por_ciudad):
            delta = random.randint(0, horas_rango)
            registros.append(generar_registro(ciudad_info, delta))

    while len(registros) < total:
        ciudad_info = random.choice(CIUDADES)
        registros.append(generar_registro(ciudad_info, random.randint(0, 720)))

    random.shuffle(registros)
    logger.info(f"Generados {len(registros)} registros sintéticos")
    return registros


if __name__ == "__main__":
    datos   = generar_datos_sinteticos(1000)
    resumen = guardar_datos_en_bd(datos)

    print(f"\n✅ Datos sintéticos cargados")
    print(f"   Total generado  : 1000")
    print(f"   Guardados en BD : {resumen['guardados']}")
    print(f"   Fallidos        : {resumen['fallidos']}")
    print(f"   Tiempo          : {resumen['tiempo']}s")