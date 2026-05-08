from sqlalchemy import (    Column, Integer, String, Float, DateTime, ForeignKey, Boolean)
from sqlalchemy.orm import relationship
from datetime import datetime
from scripts.database import Base


class Ciudad(Base):
    __tablename__ = "ciudades"

    id             = Column(Integer, primary_key=True, index=True)
    nombre         = Column(String(100), nullable=False, unique=True)
    pais           = Column(String(100), nullable=False)
    latitud        = Column(Float, nullable=True)
    longitud       = Column(Float, nullable=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    activa         = Column(Boolean, default=True)

    registros = relationship("RegistroClima", back_populates="ciudad")


class RegistroClima(Base):
    __tablename__ = "registros_clima"

    id                = Column(Integer, primary_key=True, index=True)
    ciudad_id         = Column(Integer, ForeignKey("ciudades.id"), nullable=False)
    temperatura       = Column(Float, nullable=False)
    sensacion_termica = Column(Float, nullable=True)
    humedad           = Column(Float, nullable=False)
    velocidad_viento  = Column(Float, nullable=False)
    descripcion       = Column(String(255), nullable=False)
    codigo_tiempo     = Column(Integer, nullable=True)
    fecha_extraccion  = Column(DateTime, default=datetime.utcnow)
    fecha_creacion    = Column(DateTime, default=datetime.utcnow)

    ciudad = relationship("Ciudad", back_populates="registros")


class MetricasETL(Base):
    __tablename__ = "metricas_etl"

    id                        = Column(Integer, primary_key=True, index=True)
    fecha_ejecucion           = Column(DateTime, default=datetime.utcnow)
    registros_extraidos       = Column(Integer, nullable=False)
    registros_guardados       = Column(Integer, nullable=False)
    registros_fallidos        = Column(Integer, default=0)
    tiempo_ejecucion_segundos = Column(Float, nullable=False)
    estado                    = Column(String(50), nullable=False)
    mensaje                   = Column(String(500), nullable=True)