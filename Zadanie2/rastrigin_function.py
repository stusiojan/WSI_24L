'''
g(x) = 10 * d + sum(x_i^2 - 10 * cos(2 * pi * x_i)) for i = 1 to d
computed for d = 2
g(x) = 20 + x_1^2 - 10 * cos(2 * pi * x_1) + x_2^2 - 10 * cos(2 * pi * x_2)
'''

import numpy as np

class RastriginFunction:
    def forward(self, x):
        sum = x[0]**2 - 10 * np.cos(2 * np.pi * x[0]) + x[1]**2 - 10 * np.cos(2 * np.pi * x[1])
        
        return 20 + sum
