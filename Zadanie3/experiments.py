import numpy as np
import time
import matplotlib.pyplot as plt
from min_max import MinMax

def simulate_game_progression():
    """Symuluje progresję gry, zwracając listę stanów gry."""
    game_progression = []
    current_state = np.zeros((3, 3), dtype=int)
    moves = [(0, 0), (1, 1), (0, 1), (1, 0), (0, 2), (2, 2), (1, 2), (2, 1), (2, 0)]
    for i, move in enumerate(moves):
        current_state[move] = 1 if i % 2 == 0 else -1
        game_progression.append(np.copy(current_state))
    return game_progression

def measure_execution_time(states, use_alpha_beta=False):
    """Mierzy czas wykonania algorytmu dla każdego stanu."""
    times = []
    minmax = MinMax()
    for state in states:
        start_time = time.time()
        if use_alpha_beta:
            minmax.alpha_pruning(state, (0, 0), True, -np.inf, np.inf, 9)
        else:
            minmax.minmax(state, (0, 0), True, 9)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def main():
    states = simulate_game_progression()
    times_minmax = measure_execution_time(states, use_alpha_beta=False)
    times_alpha_beta = measure_execution_time(states, use_alpha_beta=True)

    moves = list(range(1, len(states) + 1))
    plt.plot(moves, times_minmax, label='Minmax', marker='o')
    plt.plot(moves, times_alpha_beta, label='Alpha-Beta', marker='x')
    plt.xlabel('Move number')
    plt.ylabel('Execution time (s)')
    plt.title('Execution Time Comparison')
    plt.legend()
    plt.savefig('execution_time_comparison2.png')

if __name__ == "__main__":
    main()