import matplotlib.pyplot as plt

# Meses
x = [1, 2, 3, 4, 5, 6]
# Ventas x 10000
y = [2, 4, 1, 5, 2, 6]

plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)


plt.xlim(1, 8)
plt.ylim(1, 8)

plt.xlabel('Mes')
plt.ylabel('Ventas x 10000')


plt.title('Ventas del primer semestre')
plt.show()
