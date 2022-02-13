"""
Regresión lineal
Cinco niños de 2, 3, 5, 7 y 8 años de edad, pesan 14, 20, 32, 42, 44 Kilos
1. Encontrar la ecuación de la recta de regresión
2. ¿Cuál sería el peso de un niño de seis años?


***** Imprimir el resultado del punto 2
***** Imprimir la gráfica



Solución:


1. Obtener los promedios

px = (x1 + ...xn)/n

2. Obtener x*y

"""
import numpy as np
import matplotlib.pyplot as plt

# Saludo en pantalla
print("¡Hola Mundo!")

# Generación de los arreglos con numpy
edades = np.array([2, 3, 5, 7, 8])
pesos = np.array([14, 20, 32, 42, 44])

# Calcular promedios
prom_edades = np.average(edades)
prom_pesos = np.average(pesos)

# Impresión de los promedios
print("Promedio de las edades", prom_edades)
print("Promedio de los pesos", prom_pesos)

# Obtener X * Y
e_x_p = np.sum(np.multiply(edades, pesos))
# print(e_x_p)


e_2 = np.sum(np.power(edades, 2))
# print(e_2)
p_2 = np.sum(np.power(pesos, 2))

# print(p_2)
# Calcular
s_xy = (e_x_p/prom_edades) - (prom_edades*prom_pesos)
s_y2 = (p_2/prom_edades)-pow(prom_pesos, 2)

m = s_xy/s_y2

# edad - prom_edades = m * (peso - prom_pesos)

# La recta de regresión de la edad sobre el pesos pasa por
# el punto (x, y) con pendiente m = s_xy/s_y2


# edad - prom_edades = m(peso - prom_pesos)

# Solicitad edad del sujeto:
edad = float(input("Edad: "))

peso = (edad + (m * prom_edades))/m

print("Peso:", peso)

# Graficar
plt.scatter(edades, pesos, label="Datos", color="blue")
plt.title("Datos")
plt.show()