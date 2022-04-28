import random
from bat_algorithm import BatAlgorithm

def Fun(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val

# For reproducive results
#random.seed(5)

for i in range(6):
    Algorithm = BatAlgorithm(2, 6, 150, 0.001, 0.9, 0.0, 1.0, -1.0, 1.0, Fun)
    Algorithm.move_bat()