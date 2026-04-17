#!/usr/bin/env python3


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")  
import numpy as np
import logging
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from scripts.database import SessionLocal
from scripts.models import RegistroClima, Ciudad

logger = logging.getLogger(__name__)


def cargar_datos_desde_bd() -> pd.DataFrame:
    
    db = SessionLocal()
    try:
        filas = (
            db.query(
                Ciudad.nombre.label("ciudad"),
                RegistroClima.temperatura,
                RegistroClima.sensacion_termica,
                RegistroClima.humedad,
                RegistroClima.velocidad_viento,
                RegistroClima.descripcion,
                RegistroClima.fecha_extraccion,
            )
            .join(Ciudad)
            .order_by(RegistroClima.fecha_extraccion.desc())
            .limit(500)
            .all()
        )

        if not filas:
            raise ValueError("No hay datos en la base de datos.")

        df = pd.DataFrame(filas, columns=[
            "ciudad", "temperatura", "sensacion_termica",
            "humedad", "velocidad_viento", "descripcion", "fecha_extraccion"
        ])
        return df

    finally:
        db.close()


def generar_graficas(df: pd.DataFrame, output_path: str = "data/clima_analysis.png"):
    
    Path("data").mkdir(exist_ok=True)

    
    resumen = df.groupby("ciudad").agg({
        "temperatura"      : "mean",
        "sensacion_termica": "mean",
        "humedad"          : "mean",
        "velocidad_viento" : "mean",
    }).reset_index().round(1)

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle("Análisis de Clima por Ciudades", fontsize=16, fontweight="bold")


    ax1 = axes[0, 0]
    ax1.bar(resumen["ciudad"], resumen["temperatura"], color="#ff6b6b")
    ax1.set_title("Temperatura Promedio (°C)")
    ax1.set_ylabel("Temperatura (°C)")
    ax1.tick_params(axis="x", rotation=45)
    ax1.grid(axis="y", alpha=0.3)

    
    ax2 = axes[0, 1]
    ax2.bar(resumen["ciudad"], resumen["humedad"], color="#4ecdc4")
    ax2.set_title("Humedad Relativa Promedio (%)")
    ax2.set_ylabel("Humedad (%)")
    ax2.tick_params(axis="x", rotation=45)
    ax2.grid(axis="y", alpha=0.3)

    
    ax3 = axes[1, 0]
    ax3.scatter(resumen["ciudad"], resumen["velocidad_viento"], s=200, color="#95e1d3")
    ax3.set_title("Velocidad del Viento Promedio (km/h)")
    ax3.set_ylabel("km/h")
    ax3.tick_params(axis="x", rotation=45)
    ax3.grid(alpha=0.3)


    ax4 = axes[1, 1]
    x     = np.arange(len(resumen))
    width = 0.35
    ax4.bar(x - width / 2, resumen["temperatura"],       width, label="Temperatura",       color="#ff6b6b")
    ax4.bar(x + width / 2, resumen["sensacion_termica"], width, label="Sensación Térmica", color="#ffa07a")
    ax4.set_title("Temperatura vs Sensación Térmica")
    ax4.set_ylabel("Temperatura (°C)")
    ax4.set_xticks(x)
    ax4.set_xticklabels(resumen["ciudad"], rotation=45)
    ax4.legend()
    ax4.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info(f"✅ Gráficas guardadas en {output_path}")
    return output_path


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    df   = cargar_datos_desde_bd()
    path = generar_graficas(df)
    print(f"✅ Gráficas generadas en: {path}")
    print(df.groupby("ciudad")[["temperatura", "humedad", "velocidad_viento"]].mean().round(1))