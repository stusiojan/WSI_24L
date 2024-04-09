import numpy as np
import random
from min_max import MinMax

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.minmax = MinMax()

    def print_board(self):
        print('-------------')
        for i in range(3):
            print('|', self.board[i*3], '|', self.board[i*3 + 1], '|', self.board[i*3 + 2], '|')
            print('-------------')

    def check_win(self, player):
        for i in range(3):
            if self.board[i*3] == self.board[i*3 + 1] == self.board[i*3 + 2] == player:
                return True
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                return True
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        return False

    def state_from_board(self):
        state = np.zeros((3, 3))
        for i, cell in enumerate(self.board):
            if cell == 'X':
                state[i // 3, i % 3] = 1
            elif cell == 'O':
                state[i // 3, i % 3] = -1
        return state

    def evaluate_moves(self):
        state = self.state_from_board()
        evaluations = {'minmax': {}, 'alpha_pruning': {}}
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                evaluations['minmax'][i] = self.minmax.minmax(state, (0, 0), False, 5)
                evaluations['alpha_pruning'][i] = self.minmax.alpha_pruning(state, (0, 0), False, -np.inf, np.inf, 5)
                self.board[i] = ' '
        return evaluations

    def play_game(self):
        current_player = 'X'

        while True:
            self.print_board()
            if current_player == 'X':
                position = int(input('Enter a position (1-9): ')) - 1
                if self.board[position] == ' ':
                    self.board[position] = current_player
                    if self.check_win(current_player):
                        self.print_board()
                        print(f'Player {current_player} wins!')
                        break
                    elif ' ' not in self.board:
                        self.print_board()
                        print('It\'s a tie!')
                        break
                    evaluations = self.evaluate_moves()
                    print("Evaluations:", evaluations)
                    current_player = 'O'
                else:
                    print('Invalid move. Try again.')
            else: # play random move from the best moves
                best_score = -np.inf
                best_move = None
                for i in range(9):
                    if self.board[i] == ' ':
                        self.board[i] = 'O'
                        score = self.minmax.minmax(self.state_from_board(), (0, 0), True, 5)
                        self.board[i] = ' '
                        if score > best_score:
                            best_score = score
                            best_move = i
                self.board[best_move] = 'O'
                print(f'AI moves to position {best_move + 1}')
                if self.check_win('O'):
                    self.print_board()
                    print('AI wins!')
                    break
                elif ' ' not in self.board:
                    self.print_board()
                    print('It\'s a tie!')
                    break
                evaluations = self.evaluate_moves()
                print("Evaluations:", evaluations)
                current_player = 'X'
