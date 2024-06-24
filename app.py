import streamlit as st 
import pandas as pd
import plotly_express as px

data_base = pd.read_csv('vehicles_us.csv') ## Lee el archivo CSV

hist_button = st.button('construir histograma')

build_histogram = st.button('tipo de transmision')

build_histogram_type = st.button('tipo')



if hist_button:
    
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(data_base,x='odometer')

    st.plotly_chart(fig,use_container_width=True)
    
if build_histogram: # si la casilla de verificación está seleccionada
    
    st.write('Construir un histograma para la columna odómetro')
    
    fig = px.histogram(data_base,x='transmission')

    st.plotly_chart(fig,use_container_width=True)

if build_histogram_type: # si la casilla de verificación está seleccionada
    
    st.write('Construir un histograma para la columna odómetro')
    
    fig = px.histogram(data_base,x='type')

    st.plotly_chart(fig,use_container_width=True)



