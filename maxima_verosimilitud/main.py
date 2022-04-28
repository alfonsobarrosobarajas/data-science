import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt

population_rate = 3
sample_size = 100

get_sample = lambda n: np.random.exponential(population_rate, n)
xs = np.arange(0, 20, 0.001)
ys = expon.pdf(xs, scale=population_rate)
plt.plot(xs, ys, label='population')

sample = get_sample(sample_size)
plt.hist(sample, density=True, label='sample')

plt.legend()
plt.show()