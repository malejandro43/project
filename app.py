import streamlit  as st
import pandas as pd 
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
st.header('Vehicles')
hist_button = st.button('Construir histograma') # crear un botón   
   
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')            
            # crear un histograma
    #fig = px.histogram(car_data, x="odometer") # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    fig.show()
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
hist_button_dispertion= st.button('Construir grafico de dispersion')
if hist_button_dispertion: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')            
            # crear un histograma
    #fig = px.histogram(car_data, x="odometer") # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")
    fig.show()
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
if build_histogram: # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')            
            # crear un histograma
    #fig = px.histogram(car_data, x="odometer") # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    fig.show()
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_graphic = st.checkbox('Construir un grafico de dispersion')
if build_graphic:
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')            
            # crear un histograma
    #fig = px.histogram(car_data, x="odometer") # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")
    fig.show()
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
