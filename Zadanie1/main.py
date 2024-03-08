import numpy as np
import matplotlib.pyplot as plt

from gradient_descent import gradient_descent
from griewank_function import GriewankFunction


# Define parameters
griewank = GriewankFunction()
beta_parameters = [0.66, 0.3, 0.1, 0.01, 0.001, 0.0001] # Step size, I chose these values quite randomly
x0 = [0, 0] # Must be in domain of the function
epsilon = 0.0001 # How close to the minimum we want to get

# Run gradient descent
griewank_results = []
# rastrigin_results = []

for beta in beta_parameters:
    griewank_result = gradient_descent(
        f= griewank.griewank_function,
        grad= griewank.griewank_gradient,
        x0= x0,
        beta= beta,
        epsilon= epsilon)
    griewank_results.append(griewank_result)


# Plot results
plt.plot(beta_parameters, griewank_results, label= 'Griewank function')
# plt.plot(beta_parameters, rastrigin_results, label= 'Rastrigin function')
plt.xlabel('Beta')
plt.ylabel('Function value')

plt.legend()

plt.savefig('results.png')

