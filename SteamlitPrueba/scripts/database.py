import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

Base = declarative_base()

# 🔥 Está en Streamlit Cloud
if "DB_HOST" in st.secrets:

    DB_HOST = st.secrets["DB_HOST"]
    DB_PORT = st.secrets["DB_PORT"]
    DB_USER = st.secrets["DB_USER"]
    DB_PASSWORD = quote_plus(st.secrets["DB_PASSWORD"])
    DB_NAME = st.secrets["DB_NAME"]

    DATABASE_URL = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True
    )

# 💻 Estás en local
else:
    engine = create_engine(
        "sqlite:///clima-pitacho.db",
        connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)