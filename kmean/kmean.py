from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
np.random.seed(123)


def circulo(num_datos=100, R=1, minimo=0, maximo=1, center_x=0, center_y=0):
    pi = math.pi
    r = R * np.sqrt(np.random.uniform(minimo, maximo, size=num_datos))
    theta = np.random.uniform(minimo, maximo, size=num_datos) * 2 * pi

    x = center_x + np.cos(theta) * r
    y = center_y + np.sin(theta) * r

    x = np.round(x, 3)
    y = np.round(y, 3)

    df = np.column_stack([x, y])
    df = pd.DataFrame(df)
    df.columns = ['x', 'y']
    return(df)


# Create data
datos_1 = circulo(num_datos=20, R=10, center_x=5, center_y=30)
datos_2 = circulo(num_datos=20, R=10, center_x=20, center_y=10)
datos_3 = circulo(num_datos=20, R=10, center_x=50, center_y=50)

data = datos_1.append(datos_2).append(datos_3)

print(data.head())

plt.scatter(datos_1['x'], datos_1['y'], c='b')
plt.scatter(datos_2['x'], datos_2['y'], c='r')
plt.scatter(datos_3['x'], datos_3['y'], c='g')
plt.show()
