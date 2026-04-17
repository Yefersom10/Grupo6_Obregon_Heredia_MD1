#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text, and_
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '.')

from scripts.database import SessionLocal
from scripts.models import Ciudad, RegistroClima

st.set_page_config(page_title="Dashboard Interactivo", page_icon="🎛️", layout="wide")
st.title("🎛️ Dashboard Interactivo - Control Total")

db = SessionLocal()

try:
    db.execute(text("SELECT 1"))
except Exception as e:
    st.error(f"❌ No se pudo conectar a la base de datos: {e}")
    st.stop()


st.sidebar.markdown("### 🔧 Controles")

ciudades_disponibles = [c.nombre for c in db.query(Ciudad).all()]

ciudades_sel = st.sidebar.multiselect("🏙️ Ciudades", ciudades_disponibles, default=ciudades_disponibles)
fecha_inicio = st.sidebar.date_input("📅 Desde:", value=datetime.now() - timedelta(days=30))
fecha_fin    = st.sidebar.date_input("📅 Hasta:", value=datetime.now() + timedelta(days=1))
temp_min     = st.sidebar.slider("🌡️ Temp Mín (°C):", -50, 50, value=-10)
temp_max     = st.sidebar.slider("🌡️ Temp Máx (°C):", -50, 50, value=45)


filas = db.query(RegistroClima, Ciudad.nombre).join(Ciudad).filter(
    and_(
        Ciudad.nombre.in_(ciudades_sel),
        RegistroClima.fecha_extraccion >= fecha_inicio,
        RegistroClima.fecha_extraccion <= fecha_fin,
        RegistroClima.temperatura >= temp_min,
        RegistroClima.temperatura <= temp_max
    )
).all()

data = [{"Ciudad": n, "Temperatura": r.temperatura, "Sensación": r.sensacion_termica,
         "Humedad": r.humedad, "Viento": r.velocidad_viento,
         "Descripción": r.descripcion, "Fecha": r.fecha_extraccion}
        for r, n in filas]

df = pd.DataFrame(data) if data else pd.DataFrame()

if df.empty:
    st.warning("⚠️ No hay datos con los filtros seleccionados.")
    db.close()
    st.stop()


st.markdown("### 📊 Indicadores Clave")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("🌡️ Temp Max",      f"{df['Temperatura'].max():.1f}°C")
c2.metric("🌡️ Temp Min",      f"{df['Temperatura'].min():.1f}°C")
c3.metric("🌡️ Temp Prom",     f"{df['Temperatura'].mean():.1f}°C")
c4.metric("💧 Humedad Prom",   f"{df['Humedad'].mean():.1f}%")
c5.metric("💨 Viento Prom",    f"{df['Viento'].mean():.1f} km/h")
st.markdown("---")


col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Distribución de Temperaturas")
    fig = px.box(df, x="Ciudad", y="Temperatura", color="Ciudad",
                 title="Box Plot por Ciudad")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Humedad Promedio")
    fig = px.bar(df.groupby("Ciudad")["Humedad"].mean().reset_index(),
                 x="Ciudad", y="Humedad", color="Humedad",
                 color_continuous_scale="Blues")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("#### 📈 Evolución Temporal")
df["Fecha"] = pd.to_datetime(df["Fecha"])
fig = px.line(df.groupby(["Fecha","Ciudad"])["Temperatura"].mean().reset_index(),
              x="Fecha", y="Temperatura", color="Ciudad",
              title="Temperatura en el Tiempo", markers=True)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("#### 📋 Datos Detallados")
mostrar_todos = st.checkbox("Mostrar todos los registros", value=False)
cols = st.multiselect("Columnas:", df.columns.tolist(),
                      default=["Ciudad","Temperatura","Humedad","Viento","Descripción","Fecha"])
st.dataframe(df[cols] if mostrar_todos else df[cols].head(20), use_container_width=True)

st.markdown("---")
st.download_button("⬇️ Descargar CSV", df.to_csv(index=False),
                   f"clima_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", "text/csv")

db.close()