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
├── etl-prueba/
│ └── Proceso ETL de práctica
│
├── etl-proyecto/
│ └── ETL principal del proyecto
│
├── streamlitPrueba/
│ └── Dashboard de clima
│
├── streamlitProyecto/
│ └── Dashboard de películas
│
└── README.md

````

# 📂 Descripción de Carpetas

## 🔹 etl-prueba

Implementación de un **proceso ETL guiado por el docente** para comprender la estructura básica de un pipeline de datos.

**Características**

- Tipo: ETL de práctica  
- Fuente de datos: API de clima  
- Ejecución: Local  

**Objetivos**

- Consumir datos desde una API
- Transformar y limpiar datos
- Guardar información en PostgreSQL

---

## 🔹 etl-proyecto

Proyecto principal desarrollado por el grupo.

Se implementa un **pipeline ETL completo** para recolectar información de películas utilizando **OMDb API**.

**Datos obtenidos**

- Título
- Año
- Género
- Actores
- Director
- Calificación
- Información adicional

**Objetivos**

- Construir un pipeline ETL completo
- Normalizar datos
- Diseñar una base de datos optimizada
- Preparar los datos para análisis

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
- **SQL**
- **Streamlit**
- **JSON**
- **Git**
- **GitHub**

---

# 🔄 Flujo ETL del Proyecto

El pipeline implementado sigue la arquitectura clásica de **Extracción → Transformación → Carga**.
````

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

````


# 🚀 Cómo Ejecutar los Proyectos

## 1 Clonar el repositorio

```bash
git clone <url-del-repositorio>
```
2 Entrar al proyecto
```bash
cd Grupo6_Obregon_Heredia_MD1
```
3 Crear entorno virtual
```bash
python -m venv venv
```
4 Activar entorno virtual

Windows
```bash
venv\Scripts\activate
```
Linux / Mac
```bash
source venv/bin/activate
```
5 Instalar dependencias
```bash
pip install -r requirements.txt
```
6 Ejecutar proceso ETL
```bash
cd etl-proyecto python main.py
```
7 Ejecutar Streamlit localmente
```bash
streamlit run app.py
```