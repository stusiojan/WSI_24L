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
