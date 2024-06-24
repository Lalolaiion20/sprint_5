# Proyecto: SPRINT_5
Descripción
Este proyecto consiste en la creación y despliegue de un panel de control para una aplicación web utilizando Streamlit.

Funcionalidad de la Aplicación
La aplicación web permite visualizar y analizar datos de un conjunto de anuncios de venta de coches. Incluye las siguientes características:

Encabezado: Un encabezado que describe brevemente la aplicación.
Botones/Casillas de verificación: Para seleccionar y generar gráficos interactivos.
Histograma: Visualización de un histograma utilizando Plotly Express.
Gráfico de Dispersión: Visualización de un gráfico de dispersión utilizando Plotly Express.
Requisitos
La aplicación requiere las siguientes librerías de Python:

pandas
plotly_express
streamlit

Estructura del Proyecto
El repositorio del proyecto contiene los siguientes archivos y directorios:
``` bash
.
├── `README.md`
├── `app.py`
├── `vehicles_us.csv`
├── `requirements.txt`
└── `notebooks`
    └── `EDA.ipynb`
└── `.streamlit`
    └── `config.toml`
```

Configurar los comandos de Build y Start para la pagina render.com:

```Build Command:
bash
pip install --upgrade pip && pip install -r requirements.txt
```

```Start Command:
bash
streamlit run app.py
```

Desplegar la aplicación y verificar que sea accesible a través de la URL proporcionada por Render.
