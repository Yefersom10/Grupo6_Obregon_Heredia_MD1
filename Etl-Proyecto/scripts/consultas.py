#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

from scripts.database import SessionLocal
from scripts.models import Pelicula, RegistroPeliculas, MetricasETL
from sqlalchemy import func
import pandas as pd

db = SessionLocal()

def rating_promedio_por_pelicula():
    """Rating promedio de cada pelicula"""
    registros = db.query(
        Pelicula.titulo,
        func.avg(RegistroPeliculas.imdb_rating).label('rating_promedio')
    ).join(RegistroPeliculas).group_by(Pelicula.titulo).all()

    df = pd.DataFrame(registros, columns=['Pelicula', 'Rating Promedio'])
    print("\n[INFO] RATING PROMEDIO POR PELICULA:")
    print(df.to_string(index=False))

def pelicula_mas_larga():
    """Pelicula con mayor duracion"""
    registro = db.query(
        Pelicula.titulo,
        RegistroPeliculas.duracion,
        RegistroPeliculas.director
    ).join(Pelicula).order_by(
        RegistroPeliculas.duracion.desc()
    ).first()

    if registro:
        print(f"\n[INFO] PELICULA MAS LARGA: {registro.titulo} con {registro.duracion} min")

def mejor_rating():
    """Pelicula con mejor rating IMDB"""
    registro = db.query(
        Pelicula.titulo,
        RegistroPeliculas.imdb_rating,
        RegistroPeliculas.director
    ).join(Pelicula).order_by(
        RegistroPeliculas.imdb_rating.desc()
    ).first()

    if registro:
        print(f"\n[INFO] MEJOR RATING: {registro.titulo} con {registro.imdb_rating}/10 dirigida por {registro.director}")

def mayor_recaudacion():
    """Pelicula con mayor recaudacion"""
    registro = db.query(
        Pelicula.titulo,
        RegistroPeliculas.recaudacion
    ).join(Pelicula).order_by(
        RegistroPeliculas.recaudacion.desc()
    ).first()

    if registro and registro.recaudacion:
        print(f"\n[INFO] MAYOR RECAUDACION: {registro.titulo} con ${registro.recaudacion:,.0f}")

def metricas_etl():
    """Muestra metricas de ejecuciones"""
    metricas = db.query(MetricasETL).order_by(
        MetricasETL.fecha_ejecucion.desc()
    ).limit(5).all()

    print("\n[INFO] ULTIMAS 5 EJECUCIONES DEL ETL:")
    for m in metricas:
        print(f"  - {m.fecha_ejecucion}: {m.estado} ({m.registros_guardados} registros en {m.tiempo_ejecucion_segundos:.2f}s)")

if __name__ == "__main__":
    try:
        print("\n" + "="*50)
        print("ANALISIS DE DATOS - PELICULAS POSTGRESQL")
        print("="*50)

        rating_promedio_por_pelicula()
        pelicula_mas_larga()
        mejor_rating()
        mayor_recaudacion()
        metricas_etl()

        print("\n" + "="*50 + "\n")

    finally:
        db.close()