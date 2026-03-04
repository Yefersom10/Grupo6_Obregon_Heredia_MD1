import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
 
 
Base = declarative_base()

# 🔥 Producción (Streamlit Cloud)
if "DATABASE_URL" in st.secrets:
    DATABASE_URL = st.secrets["DATABASE_URL"]

    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True
    )

# 💻 Local
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