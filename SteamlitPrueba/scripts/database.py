import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(dotenv_path=env_path)
except Exception:
    pass

Base = declarative_base()


def get_database_url():
    

   
    try:
        import streamlit as st

        url = st.secrets.get("DATABASE_URL")
        if url:
            return url

        host     = st.secrets.get("DB_HOST")
        port     = st.secrets.get("DB_PORT", 6543)
        user     = st.secrets.get("DB_USER")
        password = st.secrets.get("DB_PASSWORD")
        dbname   = st.secrets.get("DB_NAME", "postgres")

        if host and user and password:
            return f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    except Exception:
        
        pass

    
    url = os.environ.get("DATABASE_URL")
    if url:
        return url

    
    host     = os.environ.get("DB_HOST")
    port     = os.environ.get("DB_PORT", "6543")
    user     = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    dbname   = os.environ.get("DB_NAME", "postgres")

    if host and user and password:
        return f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    raise ValueError(
        "❌ No se encontró configuración de base de datos.\n"
        "Define DB_HOST, DB_USER, DB_PASSWORD en:\n"
        "  • SteamlitPrueba/.streamlit/secrets.toml  (Streamlit local/cloud)\n"
        "  • SteamlitPrueba/.env                     (ejecución por terminal)"
    )


DATABASE_URL = get_database_url()

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