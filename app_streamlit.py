import streamlit as st
import pandas as pd
import joblib
from sklearn import preprocessing

# Configuración de la página
st.set_page_config(page_icon="https://www.flaticon.es/icono-gratis/libros-de-texto_1081025",
                   layout="wide")

# Título y descripción de la app
st.title("App de Predicción de Rating de Libros")
st.write("Esta app predice el rating promedio de un libro según su título, autores, páginas y cantidad de ratings y reseñas")
st.markdown("""---""")

# Logo en la barra lateral
st.sidebar.image('HarryPotter.jpeg', use_column_width=True)

# Función para ingresar datos y generar predicciones
def ingresar_datos():
    title = st.sidebar.text_input('Ingrese Título del libro')
    authors = st.sidebar.text_input('Ingrese Autores del libro')
    num_pages = st.sidebar.number_input('Ingrese Número de páginas', min_value=1)
    ratings_count = st.sidebar.number_input('Ingrese Cantidad de ratings', min_value=0)
    text_reviews_count = st.sidebar.number_input('Ingrese Cantidad de reseñas', min_value=0)

    data = {
        'title': title,
        'authors': authors,
        'num_pages': num_pages,
        'ratings_count': ratings_count,
        'text_reviews_count': text_reviews_count
    }

    return data
    

# Función para convertir los datos ingresados en un dataframe
def crear_dataframe(data):
    df = pd.DataFrame([data])
    return df

# función de preprocesamiento y predicción
def preprocesamiento_y_prediccion(data):
    le = preprocessing.LabelEncoder()
    data['title'] = le.fit_transform(data['title'])
    data['authors'] = le.fit_transform(data['authors'])
    
    # Cargar el modelo previamente entrenado
    modelo_entrenado = joblib.load('modelo_regresion.pkl')

    # Aplicar el modelo para predecir el rating promedio
    prediction = modelo_entrenado.predict(data)
    return prediction

# Obtener datos ingresados por el usuario
nuevos_datos = ingresar_datos()

# Crear DataFrame con los datos ingresados por el usuario
nuevos_df = crear_dataframe(nuevos_datos)
prediccion = preprocesamiento_y_prediccion(nuevos_df)

# Mostrar los datos ingresados por el usuario
st.header('Datos del Libro Ingresados por el Usuario')
st.write(nuevos_df)

# Mostrar la predicción del rating promedio
st.header('Predicción de Rating Promedio')
st.write(f'La predicción del rating promedio es: {prediccion[0]}')