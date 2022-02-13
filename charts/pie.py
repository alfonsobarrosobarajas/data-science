import matplotlib.pyplot as plt

activities = ['Comer', 'Mimir', 'Programar', 'Pasear']
s = [1, 1, 21, 1]

colors = ['r', 'y', 'g', 'b']

plt.pie(s, labels=activities, colors=colors,
        startangle=90, shadow=True, explode=(0, 0, 0.1, 0), radius=1.2, autopct='%1.1f%%')

plt.legend()
plt.show()
