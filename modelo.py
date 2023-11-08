import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('data_books.csv')

# Codificar las columas 'title' y 'authors'
le = preprocessing.LabelEncoder()
data['title'] = le.fit_transform(data['title'])
data['authors'] = le.fit_transform(data['authors'])

# Dividir los datos en X e y
X = data.drop(['average_rating'], axis = 1)
y = data['average_rating']

# 80% para entrenamiento y 20% para testeo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 10)

# Instanciar el objeto
lr = LinearRegression()
lr.fit(X_train, y_train)

# Utilizar datos de la prueba para verificar con precisión que el algoritmo predice el puntaje.
predictions = lr.predict(X_test)

import joblib

joblib.dump(lr, 'modelo_regresion.pkl')