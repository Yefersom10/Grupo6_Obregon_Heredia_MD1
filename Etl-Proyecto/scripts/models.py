from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from datetime import datetime
from scripts.database import Base

class Pelicula(Base):
    __tablename__ = "peliculas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), unique=True, nullable=False, index=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    registros = relationship("RegistroPeliculas", back_populates="pelicula", cascade="all, delete-orphan")

class RegistroPeliculas(Base):
    __tablename__ = "registro_peliculas"

    id = Column(Integer, primary_key=True, index=True)
    pelicula_id = Column(Integer, ForeignKey("peliculas.id"), nullable=False, index=True)
    anio = Column(Integer)
    genero = Column(String(255))
    director = Column(String(255))
    actores = Column(String(500))
    imdb_rating = Column(Float)
    duracion = Column(Integer)
    recaudacion = Column(Float)
    idioma = Column(String(100))
    pais = Column(String(100))
    fecha_extraccion = Column(DateTime, default=datetime.utcnow, index=True)

    pelicula = relationship("Pelicula", back_populates="registros")

    __table_args__ = (
        Index('idx_pelicula_fecha', 'pelicula_id', 'fecha_extraccion'),
    )

class MetricasETL(Base):
    __tablename__ = "metricas_etl"

    id = Column(Integer, primary_key=True, index=True)
    fecha_ejecucion = Column(DateTime, default=datetime.utcnow, index=True)
    registros_extraidos = Column(Integer, default=0)
    registros_guardados = Column(Integer, default=0)
    registros_fallidos = Column(Integer, default=0)
    tiempo_ejecucion_segundos = Column(Float)
    estado = Column(String(50))
    mensaje = Column(String(500))