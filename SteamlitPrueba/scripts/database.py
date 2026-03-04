# scripts/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

def get_database_url():
    # Intento 1: Streamlit secrets
    try:
        import streamlit as st
        url = st.secrets["DATABASE_URL"]
        if url:
            return url
    except Exception:
        pass
    
    # Intento 2: Variable de entorno
    url = os.environ.get("DATABASE_URL")
    if url:
        return url

    raise ValueError("❌ No se encontró DATABASE_URL")

DATABASE_URL = get_database_url()

# Corregir prefijo si es necesario
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    connect_args={"connect_timeout": 10}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)