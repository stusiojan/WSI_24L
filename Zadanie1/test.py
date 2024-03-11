''' Check if the functions are implemented correctly '''

import numpy as np
import matplotlib.pyplot as plt

from rastrigin_function import RastriginFunction
from griewank_function import GriewankFunction

griewank_function = GriewankFunction().forward
rastrigin_function = RastriginFunction().forward


rastrigin_x = np.linspace(-5, 5, 400)
rastrigin_y = np.linspace(-5, 5, 400)
griewank_x = np.linspace(-5, 5, 400)
griewank_y = np.linspace(-5, 5, 400)

rastrigin_X, rastrigin_Y = np.meshgrid(rastrigin_x, rastrigin_y)
griewank_X, griewank_Y = np.meshgrid(griewank_x, griewank_y)

rastrigin_Z = rastrigin_function([rastrigin_X, rastrigin_Y])
griewank_Z = griewank_function([griewank_X, griewank_Y])
print('rastrigin\n',rastrigin_Z)
print('griewank\n', griewank_Z)

# Plot
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.pcolormesh(rastrigin_X, rastrigin_Y, rastrigin_Z, cmap='viridis', shading='auto', zorder=0)
plt.colorbar(label='Rastrigin Function Value')
plt.title('Rastrigin Function Contour')

plt.subplot(1, 2, 2)
plt.pcolormesh(griewank_X, griewank_Y, griewank_Z, cmap='viridis', shading='auto', zorder=0)
plt.colorbar(label='Griewank Function Value')
plt.title('Griewank Function Contour')

plt.tight_layout()
plt.show()
