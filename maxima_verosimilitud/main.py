import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize
import scipy.stats as stats

import pymc3 as pm3
import numdifftools as ndt
import statsmodels.api as sm


N = 1000
x = np.linspace(0, 200, N)
e = np.random.normal(loc=0.0, scale=5.0, size=N)
y = 3*x + e

df = pd.DataFrame({'y': y, 'x': x})
df['constante'] = 1


sns.regplot(df.x, df.y)


# Dividir las características y el objetivo
X = df[['constante', 'x']]
# Ajuste el modelo y resuma
sm.OLS(y, X).fit().summary()
