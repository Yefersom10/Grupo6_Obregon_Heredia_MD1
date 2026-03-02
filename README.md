#  Grupo6_Obregon_Heredia_MD1  

Repositorio correspondiente a la materia **Minería de Datos**.  
En este proyecto se desarrollan procesos de **Extracción, Transformación y Carga (ETL)** utilizando APIs públicas, aplicando los conocimientos adquiridos en clase.

---

## 👥 Integrantes

- Nicolas Obregón  
- Yeferson Heredia  

---

## 📁 Estructura del Repositorio
~~~
Grupo6_Obregon_Heredia_MD1/
│
├── Etl-Prueba/
├── Etl-Projecto/
├── SteamlitPrueba/
├── SteamlitProyecto/
└── README.md
~~~

---

##  Descripción de Carpetas

### 🔹 Etl-Prueba

Proyecto desarrollado siguiendo la guía del docente.

- **Tipo:** ETL guiado  
- **API utilizada:** API de Clima  
- **Objetivo:**  
  Implementar un proceso ETL básico para:
  - Extraer datos desde una API pública
  - Transformar y limpiar los datos
  - Cargar la información en una base de datos  

- **Enfoque:**  
  Comprender la estructura y funcionamiento de un proceso ETL, incluyendo manejo básico de errores.

---

### 🔹 Etl-Projecto

Proyecto desarrollado de manera autónoma por el grupo.

- **Tipo:** ETL implementado por el equipo  
- **API utilizada:** API de Películas (OMDb API)  
- **Objetivo:**  
  Construir un proceso ETL completo que:
  - Extraiga información de películas (género, actores, calificaciones, año, etc.)
  - Transforme y normalice los datos
  - Almacene la información en una base de datos estructurada  

- **Enfoque:**  
  - Manejo de errores  
  - Normalización de datos  
  - Diseño optimizado de base de datos  
  - Preparación de datos para análisis en minería de datos  

---

### 🔹 SteamlitPrueba

Aplicación desarrollada con **Streamlit** para visualizar los datos del proyecto de prueba (clima).

- Visualización de datos climáticos  
- Gráficas dinámicas  
- Interfaz web interactiva  

---

### 🔹 SteamlitProyecto

Aplicación desarrollada con **Streamlit** para visualizar los datos del proyecto principal (películas).

- Consulta de películas  
- Visualización de géneros y calificaciones  
- Análisis exploratorio de datos  
- Interfaz amigable para el usuario  

---

## ⚙️ Tecnologías Utilizadas

- Python  
- Requests  
- Pandas  
- PostgreSQL  
- SQL  
- Streamlit  
- JSON  
- Git & GitHub  

---

## 🔄 Flujo ETL Implementado

### 1️⃣ Extract (Extracción)
Consumo de API mediante solicitudes HTTP para obtener datos en formato JSON.

### 2️⃣ Transform (Transformación)
- Limpieza de datos  
- Conversión de tipos de datos  
- Eliminación o tratamiento de valores nulos  
- Normalización de estructuras  

### 3️⃣ Load (Carga)
- Inserción de datos en PostgreSQL  
- Diseño de tablas optimizado para análisis posterior  

---

## 🚀 Cómo Ejecutar los Proyectos

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
```
### 2. Crear entorno virtual
```bash
python -m venv venv
```
### 3. Activar entorno virtual
```bash
venv\Scripts\activate
```
### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 5. Ejecutar proceso ETL
```bash
python main.py
```
### 6. Ejecutar aplicación Streamlit
````bash
streamlit run app.py
````
## 🎯 bjetivo Académico

Aplicar conceptos de:

- Procesamiento de datos

- Minería de datos

- Modelado de bases de datos

- Automatización de procesos ETL

- Visualización de información
