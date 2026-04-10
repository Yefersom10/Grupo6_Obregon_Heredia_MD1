# 📊 Grupo6_Obregon_Heredia_MD1

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-purple)
![API](https://img.shields.io/badge/API-Data%20Source-green)
![Status](https://img.shields.io/badge/Status-Academic%20Project-orange)

Repositorio del proyecto desarrollado para la asignatura **Minería de Datos**.

En este proyecto se implementan procesos **ETL (Extract, Transform, Load)** utilizando **APIs públicas**, almacenamiento en **PostgreSQL** y visualización de datos mediante **Streamlit**.

El repositorio contiene dos tipos de implementaciones:

- **Procesos ETL ejecutados en local**
- **Aplicaciones de visualización desplegadas en Streamlit Cloud**

---

# 👥 Integrantes

- **Nicolás Obregón**  
- **Yeferson Heredia**

---

# 📁 Estructura del Repositorio
```
Grupo6_Obregon_Heredia_MD1/
│
├── Etl-Prueba/
│   ├── alembic/
│   ├── scripts/
│   │   ├── database.py
│   │   ├── extractor.py
│   │   ├── loader.py
│   │   ├── models.py
│   │   ├── consultas.py
│   │   ├── test_db.py
│   │   └── visualizador.py
│   ├── logs/
│   ├── dashboard_app.py
│   ├── dashboard_advanced.py
│   ├── dashboard_interactive.py
│   ├── .env
│   └── requirements.txt
│
├── Etl-Proyecto/
│   ├── alembic/
│   ├── scripts/
│   │   ├── database.py
│   │   ├── extractor.py
│   │   ├── loader.py
│   │   ├── models.py
│   │   ├── consultas.py
│   │   └── test_db.py
│   ├── logs/
│   ├── dashboard_app.py
│   ├── dashboard_interactive.py
│   ├── .env
│   └── requirements.txt
│
├── streamlitPrueba/
│   └── Dashboard de clima
│
├── streamlitProyecto/
│   └── Dashboard de películas
│
└── README.md
```

---

# 📂 Descripción de Carpetas

## 🔹 Etl-Prueba

Implementación de un **proceso ETL guiado por el docente** para comprender la estructura básica de un pipeline de datos.

**Características**

- Tipo: ETL de práctica
- Fuente de datos: API de clima (Weatherstack)
- Base de datos: PostgreSQL local
- Ejecución: Local

**Objetivos**

- Consumir datos desde una API
- Transformar y limpiar datos
- Guardar información en PostgreSQL
- Visualizar datos con Streamlit

**Scripts principales**

- `extractor.py` — Extrae datos climáticos de la API Weatherstack
- `loader.py` — Transforma y carga los datos en PostgreSQL
- `models.py` — Define las tablas: `ciudades`, `registros_clima`, `metricas_etl`
- `database.py` — Configura la conexión a PostgreSQL via SQLAlchemy
- `consultas.py` — Consultas de análisis sobre los datos guardados
- `test_db.py` — Verifica la conexión y estado de la base de datos

**Ciudades monitoreadas**

Bogotá, Medellín, Cali, Barranquilla

**Dashboards disponibles**

- `dashboard_app.py` — Vista general con métricas y gráficas
- `dashboard_advanced.py` — Análisis avanzado con histórico y métricas ETL
- `dashboard_interactive.py` — Dashboard con filtros interactivos y descarga CSV

---

## 🔹 Etl-Proyecto

Proyecto principal desarrollado por el grupo.

Se implementa un **pipeline ETL completo** para recolectar información de películas utilizando **OMDb API**.

**Características**

- Tipo: ETL principal del proyecto
- Fuente de datos: OMDb API
- Base de datos: PostgreSQL local
- Ejecución: Local

**Datos obtenidos**

- Título
- Año
- Género
- Director
- Actores
- Duración
- Calificación IMDB
- Recaudación en taquilla
- Idioma y país

**Objetivos**

- Construir un pipeline ETL completo
- Normalizar datos desde la API
- Diseñar una base de datos optimizada en PostgreSQL
- Preparar los datos para análisis y visualización

**Scripts principales**

- `extractor.py` — Extrae datos de películas desde OMDb API
- `loader.py` — Transforma y carga los datos en PostgreSQL
- `models.py` — Define las tablas: `peliculas`, `registro_peliculas`, `metricas_etl`
- `database.py` — Configura la conexión a PostgreSQL via SQLAlchemy
- `consultas.py` — Consultas de análisis: mejor rating, mayor recaudación, etc.
- `test_db.py` — Verifica la conexión y estado de la base de datos

**Dashboards disponibles**

- `dashboard_app.py` — Vista general con métricas, gráficas y histórico
- `dashboard_interactive.py` — Dashboard con filtros por película, fecha y rating

---

## 🔹 streamlitPrueba

Aplicación web desarrollada con **Streamlit** para visualizar datos climáticos obtenidos en el ETL de prueba.

Funcionalidades:

- Visualización de datos
- Gráficas interactivas
- Exploración de información

---

## 🔹 streamlitProyecto

Aplicación web desarrollada con **Streamlit** para visualizar y analizar datos de películas.

Funcionalidades:

- Consulta de películas
- Visualización de géneros
- Análisis exploratorio
- Dashboard interactivo

---

# 🌐 Aplicaciones Desplegadas

Las aplicaciones de visualización están desplegadas en **Streamlit Cloud**.

### Dashboard Clima

🔗 https://grupo6obregonherediamd1-nra4m8mbxsbytij2tds2ji.streamlit.app/#a1fe1fd5

### Dashboard Películas

🔗 https://etl-peliculas-jngme7pzjzfg2tevwzhxzv.streamlit.app/

---

# ⚙️ Tecnologías Utilizadas

- **Python**
- **Pandas**
- **Requests**
- **PostgreSQL**
- **SQLAlchemy**
- **Alembic**
- **Streamlit**
- **Plotly**
- **python-dotenv**
- **JSON**
- **Git**
- **GitHub**

---

# 🔄 Flujo ETL del Proyecto

El pipeline implementado sigue la arquitectura clásica de **Extracción → Transformación → Carga**.
```
    API
     │
     │
 (Extract)
     │
     ▼
Datos en JSON
     │
     │
(Transform)
     │
     ▼
Limpieza y Normalización
     │
     │
  (Load)
     │
     ▼
PostgreSQL
     │
     │
     ▼
  Streamlit
Visualización
```

---

# 🚀 Cómo Ejecutar los Proyectos Localmente

## 1 — Clonar el repositorio
```bash
git clone 
```

## 2 — Entrar al proyecto
```bash
cd Grupo6_Obregon_Heredia_MD1/Etl-Prueba
# o
cd Grupo6_Obregon_Heredia_MD1/Etl-Proyecto
```

## 3 — Crear entorno virtual
```bash
python -m venv venv
```

## 4 — Activar entorno virtual

Windows:
```bash
venv\Scripts\activate
```

Linux / Mac:
```bash
source venv/bin/activate
```

## 5 — Instalar dependencias
```bash
pip install -r requirements.txt
```

## 6 — Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:
```env
# Para Etl-Prueba
DATABASE_URL=postgresql://postgres:tu_contraseña@localhost:5432/weatherstack_etl
API_KEY=tu_api_key
WEATHERSTACK_BASE_URL=http://api.weatherstack.com
CIUDADES=Bogota,Medellin,Cali,Barranquilla

# Para Etl-Proyecto
DATABASE_URL=postgresql://postgres:tu_contraseña@localhost:5432/peliculas_etl
API_KEY=tu_api_key_omdb
BASE_URL=http://www.omdbapi.com/
PELICULAS=Inception,Interstellar,The Dark Knight,Parasite,Avatar
```

## 7 — Crear la base de datos en PostgreSQL
```bash
psql -U postgres
CREATE DATABASE weatherstack_etl;  -- Para Etl-Prueba
CREATE DATABASE peliculas_etl;     -- Para Etl-Proyecto
\q
```

## 8 — Aplicar migraciones
```bash
alembic upgrade head
```

## 9 — Verificar conexión
```bash
python -m scripts.test_db
```

## 10 — Ejecutar el ETL
```bash
python -m scripts.extractor
```

## 11 — Ejecutar consultas de análisis
```bash
python -m scripts.consultas
```

## 12 — Correr los dashboards
```bash
streamlit run dashboard_app.py
streamlit run dashboard_advanced.py      # Solo Etl-Prueba
streamlit run dashboard_interactive.py