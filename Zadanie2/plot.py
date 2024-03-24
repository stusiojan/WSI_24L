import matplotlib.pyplot as plt
import numpy as np

def visualize(f: callable, generations, name: str):
    plt.figure()

    if name == "Drop Wave Function":
        x = np.linspace(-5.12, 5.12, 400)
        y = np.linspace(-5.12, 5.12, 400)
    elif name == "Griewank Function":
        x = np.linspace(-50, 50, 400)
        y = np.linspace(-50, 50, 400)
    elif name == "Rastrigin Function":
        x = np.linspace(-5.12, 5.12, 400)
        y = np.linspace(-5.12, 5.12, 400)

    X, Y = np.meshgrid(x, y)
    Z = f([X, Y])

    plt.figure(figsize=(9, 7))
    for i in range(len(generations)):
        plt.scatter(*zip(*generations[i-1]), color='yellow')
        plt.scatter(*zip(*generations[-1]), color='red')
    
    plt.pcolormesh(X, Y, Z, cmap='viridis', shading='auto', zorder=0)
    plt.colorbar(label=f'{name} Value')
    plt.title(f'{name}')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend()
    plt.savefig(f'Zadanie2/results/{name}')
    plt.close()