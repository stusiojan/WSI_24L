import numpy as np
import matplotlib.pyplot as plt

from gradient_descent import gradient_descent
from griewank_function import GriewankFunction
from rastrigin_function import RastriginFunction


# Define parameters
griewank = GriewankFunction()
rastrigin = RastriginFunction()
beta_parameters = [0.66, 0.3, 0.1, 0.01, 0.001, 0.0001] # Step size, I chose these values quite randomly
x0 = [0.5, 0.5] # Must be in domain of the function

# Run gradient descent
griewank_results = []
rastrigin_results = []

for beta in beta_parameters:
    griewank_result = gradient_descent(
        f= griewank.forward,
        grad= griewank.backward,
        x0= x0,
        beta= beta)
    griewank_results.append(griewank_result)

    rastrigin_result = gradient_descent(
        f= rastrigin.forward,
        grad= rastrigin.backward,
        x0= x0,
        beta= beta)
    rastrigin_results.append(rastrigin_result)


# Plot results
plt.plot(beta_parameters, griewank_results, label= 'Griewank function')
plt.plot(beta_parameters, rastrigin_results, label= 'Rastrigin function')
plt.xlabel('Beta')
plt.ylabel('Function value')

plt.legend()

plt.savefig('results.png')

