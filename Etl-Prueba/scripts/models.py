from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Index
from sqlalchemy.orm import relationship
from datetime import datetime
from scripts.database import Base

class Ciudad(Base):
    __tablename__ = "ciudades"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False, index=True)
    pais = Column(String(100))
    latitud = Column(Float)
    longitud = Column(Float)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    activa = Column(Boolean, default=True)

    registros_clima = relationship("RegistroClima", back_populates="ciudad", cascade="all, delete-orphan")

class RegistroClima(Base):
    __tablename__ = "registros_clima"

    id = Column(Integer, primary_key=True, index=True)
    ciudad_id = Column(Integer, ForeignKey("ciudades.id"), nullable=False, index=True)
    temperatura = Column(Float)
    sensacion_termica = Column(Float)
    humedad = Column(Float)
    velocidad_viento = Column(Float)
    descripcion = Column(String(255))
    codigo_tiempo = Column(Integer)
    fecha_extraccion = Column(DateTime, default=datetime.utcnow, index=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    ciudad = relationship("Ciudad", back_populates="registros_clima")

    __table_args__ = (
        Index('idx_ciudad_fecha', 'ciudad_id', 'fecha_extraccion'),
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