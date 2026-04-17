#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import sys
sys.path.insert(0, '.')

from scripts.database import SessionLocal
from scripts.models import Ciudad, RegistroClima

st.set_page_config(page_title="Dashboard Clima ETL", page_icon="🌡️", layout="wide")
st.title("🌍 Dashboard de Clima - ETL Weatherstack")
st.markdown("---")

db = SessionLocal()

try:
    registros = db.query(RegistroClima, Ciudad.nombre).join(Ciudad)\
        .order_by(RegistroClima.fecha_extraccion.desc()).all()

    data = []
    for r, ciudad_nombre in registros:
        data.append({
            "Ciudad"           : ciudad_nombre,
            "Temperatura"      : r.temperatura,
            "Sensación Térmica": r.sensacion_termica,
            "Humedad"          : r.humedad,
            "Viento (km/h)"    : r.velocidad_viento,
            "Descripción"      : r.descripcion,
            "Fecha"            : r.fecha_extraccion,
        })

    df = pd.DataFrame(data)
    df["Fecha"] = pd.to_datetime(df["Fecha"])

    if df.empty:
        st.warning("⚠️ No hay datos en la base de datos.")
        st.stop()

    
    st.sidebar.title("🔧 Filtros")
    ciudades_filtro = st.sidebar.multiselect(
        "Selecciona Ciudades:",
        options=df["Ciudad"].unique(),
        default=df["Ciudad"].unique()
    )
    df_f = df[df["Ciudad"].isin(ciudades_filtro)]

    
    st.subheader("📈 Métricas Principales")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🌡️ Temp. Promedio",    f"{df_f['Temperatura'].mean():.1f} °C")
    c2.metric("💧 Humedad Promedio",   f"{df_f['Humedad'].mean():.1f} %")
    c3.metric("💨 Viento Promedio",    f"{df_f['Viento (km/h)'].mean():.1f} km/h")
    c4.metric("📊 Total Registros",    len(df_f))
    st.markdown("---")

    
    st.subheader("📊 Visualizaciones")
    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(df_f.sort_values("Temperatura", ascending=False),
                     x="Ciudad", y="Temperatura", title="Temperatura por Ciudad",
                     color="Temperatura", color_continuous_scale="RdYlBu_r")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(df_f, x="Ciudad", y="Humedad", title="Humedad por Ciudad",
                     color="Humedad", color_continuous_scale="Blues")
        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df_f, x="Ciudad", y="Viento (km/h)", title="Velocidad del Viento",
                     color="Viento (km/h)", color_continuous_scale="Greens")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.scatter(df_f, x="Temperatura", y="Humedad", color="Ciudad",
                         title="Temperatura vs Humedad", size="Viento (km/h)")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("📋 Datos Detallados")
    st.dataframe(df_f.sort_values("Fecha", ascending=False), use_container_width=True, height=400)

finally:
    db.close()