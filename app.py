import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')  # Ajusta la ruta si es necesario

# Crear encabezado
st.header('Análisis de Datos de Vehículos')

# Crear botón para construir histograma
hist_button = st.button('Construir histograma')

if hist_button:  # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    scatter_fig = px.scatter(car_data, x='odometer', y='price', color='fuel', title='Gráfico de dispersión de precio vs. odómetro')
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(scatter_fig, use_container_width=True)

# Crear casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Crear casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de dispersión para el precio y el odómetro')
    scatter_fig = px.scatter(car_data, x='odometer', y='price', color='fuel', title='Gráfico de dispersión de precio vs. odómetro')
    st.plotly_chart(scatter_fig, use_container_width=True)

# Crear botón para construir box plot
box_plot_button = st.button('Construir Box Plot')

if box_plot_button:  # al hacer clic en el botón
    st.write('Creación de un Box Plot de Precio por Modelo')
    
    # Crear un box plot
    fig_box = px.box(car_data, x='model', y='price', title='Box Plot de Precio por Modelo', 
                     color='model', hover_name='model')
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_box, use_container_width=True)
