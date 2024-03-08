'''
f(x) = 10 * d + sum(x_i^2 - 10 * cos(2 * pi * x_i)) for i = 1 to d
'''

import numpy as np

class RastriginFunction:
    def forward(self, x):
        sum = 0

        for i in range(d2):
            sum += x[i]**2 - 10 * np.cos(2 * np.pi * x[i])
        
        return 10 * 2 + sum


    def backward(self, x):
        grad = np.zeros(2)
        for i in range(2):
            grad[i] = 2 * x[i] + 20 * np.pi * np.sin(2 * np.pi * x[i])
        return grad