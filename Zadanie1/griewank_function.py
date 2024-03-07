'''
f(x) = 1 + sum(1/4000 * x_i^2) - sum(cos(x_i / sqrt(i))) for i = 1 to d
'''

import numpy as np

def Griewank_function(x):
    d = len(x)
    sum = 0
    product = 1

    for i in range(d):
        sum += x[i]**2 / 4000

    for i in range(d):
        product *= np.cos(x[i] / np.sqrt(i))
    
    return 1 + sum - product
