# Modelo de Predicción de Rating de Libros

![](https://github.com/federicomolina86/ModeloPredictivoLibros/blob/main/src/libros.jpg)

Este proyecto consiste en la creación de un modelo de predicción para estimar el rating de libros basado en diferentes características y variables. El modelo utiliza técnicas de aprendizaje automático para predecir el rating que un libro podría recibir.

## Objetivo

El propósito principal de este proyecto es proporcionar a los usuarios una herramienta que, dada la información de un libro, prediga el posible rating que este libro podría obtener. 

## Características

El modelo de predicción se basa en una serie de características extraídas de los libros, que podrían incluir (aunque no se limitan a) lo siguiente:
- Título del libro
- Autor
- Idioma del libro
- Reseñas y calificaciones anteriores
- Páginas del libro
- Fecha de publicación

## Estructura del Proyecto

El repositorio está organizado de la siguiente manera:
- `books.csv`: dataset original.
- `data_books.csv`: contiene los conjuntos de datos utilizados para entrenar y evaluar el modelo.
- `Modelo de Predicción de Rating de Libros.ipynb`: Jupyter Notebook que detalla el proceso de ETL, EDA, entrenamiento, evaluación y visualización de resultados.
- `modelo_regresion.pkl`: archivo 'pickle' con el modelo entrenado.
- `modelo.py`: script de Python con el código del modelo de predicción.
- `app_streamlit.py`: script de Python con el código del deploy en Streamlit.
- `src`: carpeta con imágenes.
- `README.md`: Documentación detallada sobre el proyecto.
- `requirements.txt`: librerías usadas en el proyecto

## Requisitos

Para ejecutar el código o utilizar el modelo, se requiere:
- Python
- Bibliotecas Python: Pandas, Numpy, Scikit-learn, Matplotlib, Seaborn. (se especifican en el archivo `requirements.txt`)


![](https://github.com/federicomolina86/ModeloPredictivoLibros/blob/main/src/Comparaci%C3%B3n%20valores%20reales%20y%20predichos.png)

![](https://github.com/federicomolina86/ModeloPredictivoLibros/blob/main/src/Libros%20con%20m%C3%A1s%20rese%C3%B1as.png)
