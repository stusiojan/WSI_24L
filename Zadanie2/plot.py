import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from matplotlib.animation import FuncAnimation

def visualize(f: callable, generations, name: str, mu, p_m, p_c, t_max):
    plt.figure()
    fig, ax = plt.subplots(figsize=(9, 7))

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

    ax.pcolormesh(X, Y, Z, cmap='viridis', shading='auto', zorder=0)
    
    def update(frame):
        ax.clear()
        ax.pcolormesh(X, Y, Z, cmap='viridis', shading='auto', zorder=0)
        ax.scatter(*zip(*generations[frame]), color='yellow')
        
        params_text = f'Parameters: mu={mu}, p_m={p_m}, p_c={p_c}, t_max={t_max}'
        ax.text(0.5, 0.01, params_text, transform=ax.transAxes, ha='center', fontsize=9, bbox=dict(facecolor='white', alpha=0.5))

        ax.set_title(f'{name}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')

    ani = FuncAnimation(fig, update, frames=len(generations), repeat=False)
    
    output_dir = Path(f'results/animation')
    output_dir.mkdir(parents=True, exist_ok=True)

    # ani.save(f'Zadanie2/results/{name}_animation.gif', writer='imagemagick')
    ani.save(output_dir / f'{name}_animation-{mu}-{p_m}-{p_c}-{t_max}.gif', writer='pillow')

    plt.close(fig)