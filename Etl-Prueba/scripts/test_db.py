#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

from scripts.database import engine, SessionLocal
from scripts.models import Ciudad, RegistroClima, MetricasETL
from sqlalchemy import text
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    print("\n" + "="*50)
    print("PRUEBA DE CONEXION - WEATHERSTACK ETL")
    print("="*50)

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("[OK] Conexion a PostgreSQL exitosa")
            print(f"Base de datos: {engine.url.database}")
            print(f"Host: {engine.url.host}")
            print(f"Puerto: {engine.url.port}")

        db = SessionLocal()
        ciudades = db.query(Ciudad).count()
        registros = db.query(RegistroClima).count()
        metricas = db.query(MetricasETL).count()
        db.close()

        print(f"\n[INFO] Total Ciudades: {ciudades}")
        print(f"[INFO] Total Registros Clima: {registros}")
        print(f"[INFO] Total Metricas ETL: {metricas}")

    except Exception as e:
        print(f"[ERROR] No se pudo conectar: {str(e)}")
        print("\nVerifica:")
        print("- PostgreSQL esta corriendo")
        print("- DATABASE_URL en .env es correcta")
        print("- La base de datos weatherstack_etl existe")

    print("="*50 + "\n")