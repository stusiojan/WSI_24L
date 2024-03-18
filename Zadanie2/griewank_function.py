'''
g(x) = 1 + sum(1/4000 * x_i^2) - prod(cos(x_i / sqrt(i))) for i = 1 to d
computed for d = 2
g(x) = 1 + 1/4000 * x_1^2 + 1/4000 * x_2^2 - cos(x_1) * cos(x_2 / sqrt(2))
'''

import numpy as np

class GriewankFunction:
    def forward(self, x):
        sum = x[0]**2 / 4000 + x[1]**2 / 4000
        product = np.cos(x[0]) * np.cos(x[1] / np.sqrt(1))
        
        return 1 + sum - product

    def backward(self, x):
        grad = np.zeros_like(x) # np.array([0, 0])
        grad[0] = x[0] / 2000 - np.sin(x[0]) * np.cos(x[1] / np.sqrt(2))
        grad[1] = x[1] / 2000 - np.cos(x[0]) * np.sin(x[1] / np.sqrt(2)) / np.sqrt(2)
        return grad