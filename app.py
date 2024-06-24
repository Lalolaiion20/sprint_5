import streamlit as st 
import pandas as pd
import plotly_express as px

st.heater('informacion para la venta de coches')

data_base = pd.read_csv('vehicles_us.csv') ## Lee el archivo CSV

hist_button = st.button('construir histograma')

build_histogram = st.button('tipo de transmision')

build_histogram_type = st.button('tipo')

disp_cost = st.button('Construir gráfico de dispersión'):

if disp_cost:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

if hist_button:
    
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches por kilometraje')

    fig = px.histogram(data_base,x='odometer')

    st.plotly_chart(fig,use_container_width=True)
    
if build_histogram: # si la casilla de verificación está seleccionada
    
    st.write('Construir un histograma para los tipos de transmisiones')
    
    fig = px.histogram(data_base,x='transmission')

    st.plotly_chart(fig,use_container_width=True)

if build_histogram_type: # si la casilla de verificación está seleccionada
    
    st.write('Construir un histograma para la columna tipos de vehiculos')
    
    fig = px.histogram(data_base,x='type')

    st.plotly_chart(fig,use_container_width=True)



