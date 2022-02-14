# Formula lineal
# wp + b => 0 t - a = e

# Captura de valores iniciales
w1 = float(input('W1: '))
w2 = float(input('W2: '))
b = float(input('(BIAS)b: '))
alpha = float(input('alpha: '))

# Captura de la matriz
matriz = []
ecuacion = []
for i in range(0, 4):
    print("Fila {0}".format(i))
    x1 = float(input('x1: '))
    x2 = float(input('x2: '))
    target = float(input('target: '))
    ecuacion = [x1, x2, target]

    matriz.append(ecuacion)

    # Cálculo de 'y'
    y = (w1 * x1) + (w2*x2) + b

    print(y)
