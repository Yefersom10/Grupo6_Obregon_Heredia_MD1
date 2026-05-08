# 📊 Grupo6_Obregon_Heredia_MD1

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-purple)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange)
![API](https://img.shields.io/badge/API-Data%20Source-green)
![Status](https://img.shields.io/badge/Status-Academic%20Project-orange)

Repositorio del proyecto desarrollado para la asignatura **Minería de Datos**.

En este proyecto se implementan procesos **ETL (Extract, Transform, Load)** utilizando **APIs públicas**, almacenamiento en **PostgreSQL**, visualización de datos mediante **Streamlit** y modelos de **Machine Learning** usando **scikit-learn**.

El repositorio contiene:

- Procesos ETL ejecutados en local
- Dashboards interactivos con Streamlit
- Modelos de Machine Learning supervisado
- Notebooks de análisis y evaluación

---

# 👥 Integrantes

- **Nicolás Obregón**
- **Yeferson Heredia**

---

# 📁 Estructura del Repositorio

```text
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
├── notebooks/
│   ├── arbol_decision_regresion.ipynb
│   ├── arbol_clasificacion_binaria.ipynb
│   ├── regresion_logistica_binaria.ipynb
│   └── regresion_peliculas.ipynb
│
├── data/
│   └── graficas/
│       ├── arbol_decision_regresion/
│       ├── arbol_clasificacion_binaria/
│       └── regresion_logistica_binaria/
│
├── streamlitPrueba/
│   └── Dashboard de clima
│
├── streamlitProyecto/
│   └── Dashboard de películas
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📂 Descripción de Carpetas

## 🔹 Etl-Prueba

Implementación de un proceso ETL guiado por el docente para comprender la estructura básica de un pipeline de datos.

### Características

- Tipo: ETL de práctica
- Fuente de datos: API Weatherstack
- Base de datos: PostgreSQL local
- Ejecución: Local

### Objetivos

- Consumir datos desde una API
- Transformar y limpiar datos
- Guardar información en PostgreSQL
- Visualizar datos con Streamlit

### Scripts principales

- `extractor.py` — Extrae datos climáticos desde Weatherstack
- `loader.py` — Transforma y carga datos en PostgreSQL
- `models.py` — Define las tablas del sistema
- `database.py` — Configuración SQLAlchemy
- `consultas.py` — Consultas analíticas
- `test_db.py` — Verificación de conexión

### Dashboards disponibles

- `dashboard_app.py`
- `dashboard_advanced.py`
- `dashboard_interactive.py`

---

## 🔹 Etl-Proyecto

Proyecto principal desarrollado por el grupo utilizando la API OMDb para análisis de películas.

### Datos obtenidos

- Título
- Año
- Género
- Director
- Actores
- Duración
- Rating IMDB
- Recaudación
- Idioma
- País

### Objetivos

- Construir un pipeline ETL completo
- Normalizar datos desde API
- Diseñar una base de datos optimizada
- Preparar los datos para análisis predictivo

### Scripts principales

- `extractor.py`
- `loader.py`
- `models.py`
- `database.py`
- `consultas.py`
- `test_db.py`

### Dashboards disponibles

- `dashboard_app.py`
- `dashboard_interactive.py`

---

# 🤖 Modelos de Machine Learning

El proyecto incluye notebooks desarrollados con **scikit-learn** para aplicar técnicas de aprendizaje supervisado sobre los datos almacenados en PostgreSQL.

---

## 🌳 Árbol de Decisión para Regresión

Modelo implementado utilizando:

```python
DecisionTreeRegressor
```

### Objetivo

Predecir variables numéricas relacionadas con películas utilizando árboles de decisión.

### Incluye

- Entrenamiento del modelo
- Evaluación de métricas
- Visualización del árbol
- Predicciones
- Exportación de gráficas

---

## 🌳 Árbol de Decisión para Clasificación Binaria (1-0)

Modelo implementado utilizando:

```python
DecisionTreeClassifier
```

### Objetivo

Clasificar películas en categorías binarias utilizando variables numéricas del dataset.

### Incluye

- Creación de variable objetivo binaria
- Accuracy
- Precision
- Recall
- F1-Score
- Matriz de confusión
- Visualización del árbol de decisión

---

## 📊 Regresión Logística Binaria (1-0)

Modelo implementado utilizando:

```python
LogisticRegression
```

### Objetivo

Predecir probabilidades de clasificación binaria usando regresión logística.

### Incluye

- Escalado de variables con StandardScaler
- Entrenamiento y validación
- Curvas ROC
- ROC-AUC
- Matrices de confusión
- Comparación de métricas
- Importancia de variables

---

# 📈 Gráficas Generadas

Los notebooks generan automáticamente gráficas almacenadas en:

```text
data/graficas/
```

### Gráficas incluidas

- Árboles de decisión
- Curvas ROC
- Matrices de confusión
- Comparación de métricas
- Distribución de clases
- Importancia de variables
- Predicciones y resultados

---

# 🌐 Aplicaciones Desplegadas

Las aplicaciones están desplegadas en Streamlit Cloud.

## Dashboard Clima

🔗 https://grupo6obregonherediamd1-nra4m8mbxsbytij2tds2ji.streamlit.app/#a1fe1fd5

## Dashboard Películas

🔗 https://etl-peliculas-jngme7pzjzfg2tevwzhxzv.streamlit.app/

---

# ⚙️ Tecnologías Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- Requests
- PostgreSQL
- SQLAlchemy
- Alembic
- Streamlit
- Plotly
- python-dotenv
- JSON
- Git
- GitHub

---

# 🔄 Flujo ETL del Proyecto

El pipeline implementado sigue la arquitectura clásica:

```text
        API
         │
         ▼
     Extracción
         │
         ▼
   Datos en JSON
         │
         ▼
   Transformación
         │
         ▼
 Limpieza y Normalización
         │
         ▼
      PostgreSQL
         │
         ▼
    Machine Learning
         │
         ▼
      Streamlit
```

---

# 🚀 Cómo Ejecutar el Proyecto

## 1 — Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

---

## 2 — Entrar al proyecto

```bash
cd Grupo6_Obregon_Heredia_MD1
```

---

## 3 — Crear entorno virtual

```bash
python -m venv venv
```

---

## 4 — Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5 — Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 6 — Configurar variables de entorno

Crear archivo `.env`

```env
# Weatherstack
DATABASE_URL=postgresql://postgres:password@localhost:5432/weatherstack_etl
API_KEY=tu_api_key_weatherstack
WEATHERSTACK_BASE_URL=http://api.weatherstack.com

# OMDb
DATABASE_URL=postgresql://postgres:password@localhost:5432/peliculas_etl
API_KEY=tu_api_key_omdb
BASE_URL=http://www.omdbapi.com/
```

---

## 7 — Crear bases de datos

```sql
CREATE DATABASE weatherstack_etl;
CREATE DATABASE peliculas_etl;
```

---

## 8 — Ejecutar migraciones

```bash
alembic upgrade head
```

---

## 9 — Ejecutar ETL

```bash
python -m scripts.extractor
```

---

## 10 — Ejecutar dashboards

```bash
streamlit run dashboard_app.py
```

---

## 11 — Ejecutar notebooks

Abrir la carpeta `notebooks/` en:

- Jupyter Notebook
- VSCode
- JupyterLab

y ejecutar las celdas secuencialmente.

---

# 📌 Resultados del Proyecto

El proyecto integra:

- ETL completo desde APIs públicas
- PostgreSQL como almacenamiento principal
- Dashboards interactivos
- Modelos de Machine Learning
- Evaluación comparativa de modelos
- Exportación de gráficas y métricas
- Notebooks documentados para análisis académico

---

# 📄 Licencia

Proyecto académico desarrollado para fines educativos en la asignatura de Minería de Datos.