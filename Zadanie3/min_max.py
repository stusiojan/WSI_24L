'''
s in S - Stan gry i informacja która osoba ma teraz ruch
p in P - funkcja następnika, która reprezentuje możliwe ruchy
s_0 in S - początkowy stan gry
T in S - funkcja, która zwraca wynik gry (stany terminalne)
w - funkcja wypłaty, która zwraca wynik gry (1, 0, -1)
h(s) - funkcja heurystyczna, która zwraca wartość stanu gry
d - głębokość drzewa

state - tablica 3x3, która reprezentuje stan gry
maximizing - Min / Max move
depth - głębokość drzewa

alpha - wartość dla gracza maksymalizującego
beta - wartość dla gracza minimalizującego
'''

'''
def Minimax(s,d ):
    if s ∈ T or d=0 :
        return h(s)
    U := successors(s)
    for u in U :
        w(u) = Minimax(u, d-1)
    if Max-move :
        return max(w(u))
    else:
        return min(w(u))

def AlfaBeta(s,d,α,β) :
    if s ∈ T or d = 0 then :
        return h(s)
    U := successors(s)
    if Max-move then :
        for u in U :
            α := max(α, AlfaBeta (u, d-1, α, β) )
            if α⩾β then :
                return β
        return α
    else :
        for u in U :
            β := min(β, AlfaBeta(u, d-1, α, β) )
            if α⩾β then :
                return α
        return β
'''

import numpy as np
import time

class MinMax:
    def __init__(self, game):
        self.game = game
        self.nodes_visited = 0
    
    def evaluate_game(self, state: np.ndarray, depth: int) -> int:
        if self.game.check_win(1):
            return 10 - depth
        elif self.game.check_win(-1):
            return depth - 10
        else:
            return 0
    
    def minmax_measure(
        self, 
        state, 
        depth, 
        maximizing
        ):
        start_time = time.time()
        self.nodes_visited = 0
        result = self.minmax(state, depth, maximizing)
        execution_time = time.time() - start_time
        return result + (self.nodes_visited, execution_time)

    def minmax(
        self, 
        state: np.ndarray, 
        depth: int, 
        maximizing: bool
        ) -> tuple:
        self.nodes_visited += 1
        if self.game.check_win(1) or self.game.check_win(-1) or self.game.is_draw():
            return self.evaluate_game(state, depth), None
        
        if maximizing:
            maxEval = float('-inf')
            best_move = None
            for move in self.game.get_available_moves():
                self.game.make_move(move, 1) 
                eval, _ = self.minmax(state, depth + 1, False)
                self.game.board[move] = 0 
                if eval > maxEval:
                    maxEval = eval
                    best_move = move
            return maxEval, best_move
        else:
            minEval = float('inf')
            best_move = None
            for move in self.game.get_available_moves():
                self.game.make_move(move, -1)
                eval, _ = self.minmax(state, depth + 1, True)
                self.game.board[move] = 0
                if eval < minEval:
                    minEval = eval
                    best_move = move
            return minEval, best_move
    
    def alpha_pruning_measure(
        self, 
        state, 
        depth, 
        maximizing, 
        alpha, 
        beta
        ):
        start_time = time.time()
        self.nodes_visited = 0
        result = self.alpha_pruning(state, depth, maximizing, alpha, beta)
        execution_time = time.time() - start_time
        return result + (self.nodes_visited, execution_time)

    def alpha_pruning(
        self, 
        state: np.ndarray,
        depth: int, 
        maximizing: bool,
        alpha: int,
        beta: int
        ) -> tuple:
        self.nodes_visited += 1
        if self.game.check_win(1) or self.game.check_win(-1) or self.game.is_draw():
            return self.evaluate_game(state, depth), None
        
        if maximizing:
            maxEval = float('-inf')
            best_move = None
            for move in self.game.get_available_moves():
                self.game.make_move(move, 1)
                eval, _ = self.alpha_pruning(state, depth + 1, False, alpha, beta)
                self.game.board[move] = 0
                if eval > maxEval:
                    maxEval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval, best_move
        else:
            minEval = float('inf')
            best_move = None
            for move in self.game.get_available_moves():
                self.game.make_move(move, -1)
                eval, _ = self.alpha_pruning(state, depth + 1, True, alpha, beta)
                self.game.board[move] = 0
                if eval < minEval:
                    minEval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval, best_move
