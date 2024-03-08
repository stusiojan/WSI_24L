'''
f(x) = 1 + sum(1/4000 * x_i^2) - sum(cos(x_i / sqrt(i))) for i = 1 to d
'''

import numpy as np

class GriewankFunction:
    def forward(self, x):
        sum = 0
        product = 1

        for i in range(2):
            sum += x[i]**2 / 4000

        for i in range(2):
            product *= np.cos(x[i] / np.sqrt(i))
        
        return 1 + sum - product

    def backward(self, x):
        grad = np.zeros(2)
        for i in range(2):
            sum_derivative = x[i] / 2000
            product_derivative = np.sin(x[i] / np.sqrt(i + 1)) / np.sqrt(i + 1)
            for j in range(2):
                if i != j:
                    product_derivative *= np.cos(x[j] / np.sqrt(j + 1))
            grad[i] = sum_derivative - product_derivative
        return grad