'''
f(x) = 10 * d + sum(x_i^2 - 10 * cos(2 * pi * x_i)) for i = 1 to d
'''

import numpy as np

def rastrigin_function(x):
    d = 2 # len(x), but it will be used in 2D space
    sum = 0

    for i in range(d):
        sum += x[i]**2 - 10 * np.cos(2 * np.pi * x[i])
    
    return 10 * d + sum
