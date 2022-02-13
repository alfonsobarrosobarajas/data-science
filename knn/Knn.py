# Sklearn -> KNN
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Se incluye el algoritmo de clasificación KNN
from sklearn.neighbors import KNeighborsClassifier

# Datos(Modelo)
data = {
    'Masa': [50, 80, 90, 45, 60],
    'Altura': [1.48, 1.82, 1.85, 1.55, 1.60],
    'Genero': ['m', 'h', 'h', 'm', 'm']
}

punto_nuevo = {
    'Masa': [70],
    'Altura': [1.82]
}

# Matriz de datos
df = pd.DataFrame(data)
punto_nuevo = pd.DataFrame(punto_nuevo)

# Comenzamos con la graficación de los datos
ax = plt.axes()
# Para el conjunto de 'Hombres'
ax.scatter(
    df.loc[df['Genero'] == 'h', 'Masa'],
    df.loc[df['Genero'] == 'h', 'Altura'],
    c='red',
    label='Hombre'
)

# Para el conjunto de 'Mujeres'
ax.scatter(
    df.loc[df['Genero'] == 'm', 'Masa'],
    df.loc[df['Genero'] == 'm', 'Altura'],
    c='blue',
    label='Mujer'
)

# Para el elemento a inferir
ax.scatter(
    punto_nuevo['Masa'],
    punto_nuevo['Altura'],
    c='black'
)

# Mostrar gráfica
plt.xlabel('Masa')
plt.ylabel('Hombre')
plt.legend()
plt.show()

# Aquí se da respuesta -v
# Se crea objeto de la clase KNN
knn = KNeighborsClassifier(n_neighbors=3)
X = df[['Masa', 'Altura']]
y = df[['Genero']]

# Ajuste del modelo
knn.fit(X, y)

# Predicción del punto nuevo, con base en los datos de entrenamiento
prediction = knn.predict(punto_nuevo)
print('El dato corresponde a:', prediction)
