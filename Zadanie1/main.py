import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from gradient_descent import gradient_descent
from griewank_function import GriewankFunction
from rastrigin_function import RastriginFunction
from plot import visualize

griewank = GriewankFunction()
rastrigin = RastriginFunction()
# Define parameters
beta_parameters = [0.66, 0.3, 0.1, 0.01, 0.001, 0.0001]
## x0 = [a, b]
a = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
b = 2

def plot_vectors(ax, results, function):
    for result in results:
        x, y = result
        z = function([x, y])
        ax.quiver(x, y, z, 0, 0, -z, length=0.1, color='red', arrow_length_ratio=0.3, linestyle='dashed')


for i in a:
    print(f'x0 = {i}')
    for beta in beta_parameters:

        griewank_result = gradient_descent(
            f= griewank.forward,
            grad= griewank.backward,
            x0= [i, b],
            beta= beta)

        rastrigin_result = gradient_descent(
            f= rastrigin.forward,
            grad= rastrigin.backward,
            x0= [i, b],
            beta= beta)

        visualize(griewank.forward, np.array(griewank_result), i, beta, 'Griewank')
        visualize(rastrigin.forward, np.array(rastrigin_result), i, beta, 'Rastrigin')

print('Done. Results saved to files.')
