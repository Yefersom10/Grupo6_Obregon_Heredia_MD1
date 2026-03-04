import os
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Detecta si está en Streamlit Cloud
if "DB_HOST" in st.secrets:
    DB_HOST = st.secrets["DB_HOST"]
    DB_PORT = st.secrets["DB_PORT"]
    DB_USER = st.secrets["DB_USER"]
    DB_PASSWORD = st.secrets["DB_PASSWORD"]
    DB_NAME = st.secrets["DB_NAME"]

    DATABASE_URL = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
else:
    DATABASE_URL = os.getenv("DATABASE_URL")

# Fallback local
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///clima-pitacho.db"
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()