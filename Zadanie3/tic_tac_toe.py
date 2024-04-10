import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)

    def print_board(self):
        print('-------------')
        for i in range(3):
            print('|', end=' ')
            for j in range(3):
                print(self.board[i, j], end=' | ')
            print('\n-------------')

    
    def is_valid_move(self, action):
        row, col = action
        return self.board[row, col] == 0
    
    def make_move(self, action, player):
        if self.is_valid_move(action):
            self.board[action] = player
            return True
        return False
    
    def check_win(self, player):
        for i in range(3):
            if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                return True
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False
    
    def is_draw(self):
        return np.all(self.board != 0)
    
    def get_available_moves(self):
        return [(row, col) for row in range(3) for col in range(3) if self.board[row, col] == 0]
