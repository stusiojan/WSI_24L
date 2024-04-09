'''
Tic Tac Toe:

s in S - Stan gry i informacja która osoba ma teraz ruch
p in P - funkcja następnika, która reprezentuje możliwe ruchy
s_0 in S - początkowy stan gry
T in S - funkcja, która zwraca wynik gry (stany terminalne)
w - funkcja wypłaty, która zwraca wynik gry (1, 0, -1)
h(s) - funkcja heurystyczna, która zwraca wartość stanu gry
d - głębokość drzewa
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
'''

'''
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

'''
state - tablica 3x3, która reprezentuje stan gry
action - ruch, który chcemy wykonać, pierwszy element to wiersz, drugi to kolumna
maximizing - czy maksymalizujemy wartość
depth - głębokość drzewa

alpha - wartość dla gracza maksymalizującego
beta - wartość dla gracza minimalizującego
'''
import numpy as np

class MinMax:
    def __init__(self):
        self.n_visited_nodes = 0
        self.total_leaf_depth = 0
        self.n_leaves = 0

    def evaluate_game(self, state: np.ndarray) -> int:
        for i in range(3):
            if state[i, 0] == state[i, 1] == state[i, 2] and state[i, 0] != 0:
                return state[i, 0]
        for i in range(3):
            if state[0, i] == state[1, i] == state[2, i] and state[0, i] != 0:
                return state[0, i]
        if state[0, 0] == state[1, 1] == state[2, 2] and state[0, 0] != 0:
            return state[0, 0]
        if state[0, 2] == state[1, 1] == state[2, 0] and state[0, 2] != 0:
            return state[0, 2]
        return 0

    def minmax(
        self,
        state: np.ndarray,
        action: tuple[int, int],
        maximizing: bool,
        depth: int,
    ) -> int:
        self.n_visited_nodes += 1

        if self.evaluate_game(state) != 0 or depth == 0:
            return self.evaluate_game(state)
        if maximizing:
            max_eval = -np.inf
            for i in range(3):
                for j in range(3):
                    if state[i, j] == 0:
                        state[i, j] = 1
                        eval = self.minmax(state, (i, j), False, depth - 1)
                        state[i, j] = 0
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = np.inf
            for i in range(3):
                for j in range(3):
                    if state[i, j] == 0:
                        state[i, j] = -1
                        eval = self.minmax(state, (i, j), True, depth - 1)
                        state[i, j] = 0
                        min_eval = min(min_eval, eval)
            return min_eval

    def alpha_pruning(
        self,
        state: np.ndarray,
        action: tuple[int, int],
        maximizing: bool,
        alpha: int,
        beta: int,
        depth: int,
    ) -> int:
        self.n_visited_nodes += 1

        if self.evaluate_game(state) != 0 or depth == 0:
            self.total_leaf_depth += (9 - depth)
            self.n_leaves += 1
            return self.evaluate_game(state)
        if maximizing:
            for i in range(3):
                for j in range(3):
                    if state[i, j] == 0:
                        state[i, j] = 1
                        alpha = max(alpha, self.alpha_pruning(state, (i, j), False, alpha, beta, depth - 1))
                        state[i, j] = 0
                        if alpha >= beta:
                            return beta
            return alpha
        else:
            for i in range(3):
                for j in range(3):
                    if state[i, j] == 0:
                        state[i, j] = -1
                        beta = min(beta, self.alpha_pruning(state, (i, j), True, alpha, beta, depth - 1))
                        state[i, j] = 0
                        if alpha >= beta:
                            return alpha
            return beta
