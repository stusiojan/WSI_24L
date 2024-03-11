import matplotlib.pyplot as plt
import numpy as np

def visualize(f: callable, trajectory: np.array, i: int, beta, name: str):
    plt.figure()

    print('Trajectory:[-1]',trajectory[-1])
    min_x, min_y = trajectory[-1]
    if name == 'Rastrigin':
        MIN_X = -5.12
        MAX_X = 5.12
    else:
        MIN_X = -5
        MAX_X = 5
    PLOT_STEP = 400 # points between -5 and 5

    x1 = np.linspace(MIN_X, MAX_X, PLOT_STEP)
    x2 = np.linspace(MIN_X, MAX_X, PLOT_STEP)
    X1, X2 = np.meshgrid(x1, x2)
    Z = f([X1, X2])

    plt.figure(figsize=(9, 7))
    plt.pcolormesh(X1, X2, Z, cmap='viridis', shading='auto', zorder=0)
    plt.colorbar(label=f'{name} Function Value')
    plt.xlabel('a')
    plt.ylabel('b')
    plt.title(f'{name} Function')

    plt.scatter(min_x, min_y, color='yellow', label='Found Minimum', zorder=1)
    plt.plot(trajectory[:, 0], trajectory[:, 1], marker='o', color='red', label='Gradient Descent Steps', alpha=0.5)

    plt.legend()
    plt.savefig(f'Zadanie1/results3D/{name}_beta-{beta}_x0-{i}_12.png')
    plt.close()