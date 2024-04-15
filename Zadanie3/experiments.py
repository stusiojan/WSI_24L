from tic_tac_toe import TicTacToe
from min_max import MinMax
import numpy as np
import matplotlib.pyplot as plt
import itertools


mid_game_states = [
    np.array([[1, -1, 0], [0, 1, 0], [-1, 0, 0]]),
    np.array([[1, 0, -1], [-1, 1, 0], [0, 0, 1]]),
    np.array([[0, -1, 1], [-1, 1, 0], [1, 0, 0]])
]

def simulate_moves(game, moves):
    for move in moves:
        game.make_move(move, 1)
        if not game.is_draw() and not game.check_win(1):
            game.make_move(move, -1)

def run_experiment(game, ai, state, use_alpha_pruning):
    game.board = state.copy()
    if use_alpha_pruning:
        _, _, nodes_visited, execution_time = ai.alpha_pruning_measure(game.board, 0, True, float('-inf'), float('inf'))
    else:
        _, _, nodes_visited, execution_time = ai.minmax_measure(game.board, 0, True)
    
    print(f"{'Alpha-Beta' if use_alpha_pruning else 'MinMax'} - Nodes Visited: {nodes_visited}, Execution Time: {execution_time:.5f}s")
    return nodes_visited, execution_time

def run_experiment_time(game, ai, use_alpha_pruning):
    if use_alpha_pruning:
        _, _, nodes_visited, execution_time = ai.alpha_pruning_measure(game.board, 0, True, float('-inf'), float('inf'))
    else:
        _, _, nodes_visited, execution_time = ai.minmax_measure(game.board, 0, True)
    
    print(f"{'Alpha-Beta' if use_alpha_pruning else 'MinMax'} - Nodes Visited: {nodes_visited}, Execution Time: {execution_time:.5f}s")
    return execution_time

def main():
    game = TicTacToe()
    ai = MinMax(game)

    available_moves = list(itertools.product(range(3), repeat=2))

    times_minmax = []
    times_alpha_beta = []

    initial_states = [np.zeros((3, 3)) for _ in range(9)]
    for i, (row, col) in enumerate([(row, col) for row in range(3) for col in range(3)]):
        initial_states[i][row, col] = 1

    all_states = initial_states + mid_game_states

    execution_times_minmax, execution_times_alpha_beta = [], []
    nodes_visited_minmax, nodes_visited_alpha_beta = [], []

    for state in all_states:
        nodes_minmax, time_minmax = run_experiment(game, ai, state, use_alpha_pruning=False)
        execution_times_minmax.append(time_minmax)
        nodes_visited_minmax.append(nodes_minmax)

        nodes_alpha_beta, time_alpha_beta = run_experiment(game, ai, state, use_alpha_pruning=True)
        execution_times_alpha_beta.append(time_alpha_beta)
        nodes_visited_alpha_beta.append(nodes_alpha_beta)

    for move_number in range(1, len(available_moves) + 1):
        game.board = np.zeros((3, 3), dtype=int)
        simulate_moves(game, available_moves[:move_number])

        time_minmax = run_experiment_time(game, ai, use_alpha_pruning=False)
        times_minmax.append(time_minmax)

        game.board = np.zeros((3, 3), dtype=int)
        simulate_moves(game, available_moves[:move_number])

        time_alpha_beta = run_experiment_time(game, ai, use_alpha_pruning=True)
        times_alpha_beta.append(time_alpha_beta)

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(available_moves) + 1), times_minmax, label='MinMax', marker='o')
    plt.plot(range(1, len(available_moves) + 1), times_alpha_beta, label='Alpha-Beta', marker='x')
    plt.xlabel('Move Number')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time by Move Number')
    plt.legend()
    plt.grid(True)
    plt.savefig('execution_time.png')


if __name__ == '__main__':
    main()
