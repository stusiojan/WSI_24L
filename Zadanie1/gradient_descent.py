'''
Psuedo code:
1. x <- x_0                                 Start with initial guess x0
2. while! stop                              Repeat until stopping criterion is satisfied: Stopping criterion ||grad g(x)|| < epsilon
    3. d <- -grad g(x)                      Compute search direction
    4. x <- x + beta * d                    Update x
'''

import numpy as np

def gradient_descent(f, grad, x0, beta, epsilon):
    x = np.array(x0)

    for _ in range(1000):
        d = -grad(x)
        if np.linalg.norm(-d) < epsilon:
            break
        x = x + beta * d
    return x
