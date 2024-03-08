'''
f(x) = 1 + sum(1/4000 * x_i^2) - sum(cos(x_i / sqrt(i))) for i = 1 to d
'''

import numpy as np

class GriewankFunction:
    def griewank_function(x):
        d = 2 # len(x), but it will be used in 2D space
        sum = 0
        product = 1

        for i in range(d):
            sum += x[i]**2 / 4000

        for i in range(d):
            product *= np.cos(x[i] / np.sqrt(i))
        
        return 1 + sum - product

    def griewank_gradient(x):
        d = len(x)
        grad = np.zeros(d)
        for i in range(d):
            sum_derivative = x[i] / 2000
            product_derivative = np.sin(x[i] / np.sqrt(i + 1)) / np.sqrt(i + 1)
            for j in range(d):
                if i != j:
                    product_derivative *= np.cos(x[j] / np.sqrt(j + 1))
            grad[i] = sum_derivative - product_derivative
        return grad