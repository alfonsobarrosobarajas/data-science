import matplotlib.pyplot as plt

# Meses
x = [1, 2, 3, 4, 5]
# Ventas x 10000
y = [2, 4, 1, 5, 2]

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

plt.bar(x, y, tick_label=labels, width=0.8, color=['red', 'green'])

plt.xlabel('Mes')
plt.ylabel('Ventas')

plt.title('Ventas primeros 5 meses')
plt.show()
