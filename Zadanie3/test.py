import numpy as np

from min_max import MinMax

def test_game_states():
    minmax = MinMax()
    initial_states = [np.zeros((3, 3)) for _ in range(9)]
    mid_game_states = [
        np.array([[ 1, -1,  0],
                  [ 0,  1,  0],
                  [-1,  0,  0]]),
        np.array([[ 1,  0, -1],
                  [-1,  1,  0],
                  [ 0,  0,  1]]),
        np.array([[ 0, -1,  1],
                  [-1,  1,  0],
                  [ 1,  0,  0]])
    ]

    # Badanie w stanach początkowych
    for i, state in enumerate(initial_states):
        minmax.n_visited_nodes = 0
        state[int(i / 3), i % 3] = 1 
        minmax.minmax(state, (0, 0), False, 9)
        print(f"Initial state {i+1}, Visited nodes: {minmax.n_visited_nodes}")

    # Badanie w stanach ze środka gry
    for i, state in enumerate(mid_game_states):
        minmax.n_visited_nodes = 0
        minmax.minmax(state, (0, 0), False, 9 - (i * 2 + 3))
        print(f"Mid-game state {i+1}, Visited nodes: {minmax.n_visited_nodes}")

def test_game_states_ap():
    minmax = MinMax()
    initial_states = [np.zeros((3, 3)) for _ in range(9)]
    mid_game_states = [
        np.array([[ 1, -1,  0],
                  [ 0,  1,  0],
                  [-1,  0,  0]]),
        np.array([[ 1,  0, -1],
                  [-1,  1,  0],
                  [ 0,  0,  1]]),
        np.array([[ 0, -1,  1],
                  [-1,  1,  0],
                  [ 1,  0,  0]])
    ]

    # Badanie w stanach początkowych
    for i, state in enumerate(initial_states):
        minmax.n_visited_nodes = 0
        state[int(i / 3), i % 3] = 1 
        minmax.minmax(state, (0, 0), False, 9)
        minmax.alpha_pruning(state, (0, 0), False, -np.inf, np.inf, 9)
        print(f"Initial state {i+1}, Visited nodes: {minmax.n_visited_nodes}")
        if minmax.n_leaves > 0:
            avg_depth = minmax.total_leaf_depth / minmax.n_leaves
            print(f"Average leaf depth: {avg_depth}")

    # Badanie w stanach ze środka gry
    for i, state in enumerate(mid_game_states):
        minmax.n_visited_nodes = 0
        minmax.alpha_pruning(state, (0, 0), False, -np.inf, np.inf, 9 - (i * 2 + 3))
        print(f"Mid-game state {i+1}, Visited nodes: {minmax.n_visited_nodes}")
        if minmax.n_leaves > 0:
            avg_depth = minmax.total_leaf_depth / minmax.n_leaves
            print(f"Average leaf depth: {avg_depth}")

if __name__ == "__main__":
    print('MinMax:')
    test_game_states()
    print('Alpha pruning:')
    test_game_states_ap()