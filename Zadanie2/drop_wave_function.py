'''
g(x) = - (1 + cos(12 * sqrt(x_1^2 + x_2^2))) / (0.5 * (x_1^2 + x_2^2) + 2)
'''

import numpy as np

class DropWaveFunction:
    def forward(self, x):
        sum = x[0]**2 + x[1]**2
        cos = np.cos(12 * np.sqrt(sum))
        
        return - (1 + cos) / (0.5 * sum + 2)
