# scripts/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# 🔥 Producción (Streamlit Cloud - Environment Variables)
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ Error: No se encontró DATABASE_URL en las variables de entorno")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# 💻 Local (para desarrollo)
# Solo se usa si DATABASE_URL no está configurado
if not DATABASE_URL:
    engine = create_engine(
        "sqlite:///clima-pitacho.db",
        connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)