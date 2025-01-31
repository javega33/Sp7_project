import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos con ruta nueva 
#hist_button = st.button('Construir histograma') # crear un botón
#disp_button = st.button('Construir Dispersión') # crear un botón

# crear una casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_disp = st.checkbox('Construir Dispersión') 

#print(car_data.head(10))

st.header('Analisis de Venta de Coches')
       
if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma el rango de precios de los autos con los que cuenta la agencia')
            
    # crear un histograma
    fig = px.histogram(car_data, x='price')
       
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_disp: # al hacer clic en el botón
    #Filtramos informacion, contamos los tipos de coches que actualmente cuenta la agencia
    types_car = car_data.groupby(by='type')['price'].agg('count')
    types_car = types_car.reset_index()
    
    # escribir un mensaje
    st.write('Creación de un Gráfico de Dispersión para ver los diferentes tipos de autos con los que cuenta la agencia.')
    
            
    # crear un dispersion
    fig = px.bar(types_car,x='type', y='price')
       
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

