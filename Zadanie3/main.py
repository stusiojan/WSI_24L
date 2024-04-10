from min_max import MinMax
from tic_tac_toe import TicTacToe

def main():
    game = TicTacToe()
    ai = MinMax(game)
    current_player = 1
    
    while not game.check_win(1) and not game.check_win(-1) and not game.is_draw():
        print("Current board:")
        game.print_board()
        
        if current_player == 1:
            _, suggested_move_tuple = ai.alpha_pruning(game.board, 0, True, float('-inf'), float('inf')) # first move with 1
            suggested_move = suggested_move_tuple[0] * 3 + suggested_move_tuple[1] + 1
            print(f"Suggested move: {suggested_move}")

            user_input = int(input("Enter move (1-9): "))
            row = (user_input - 1) // 3
            col = (user_input - 1) % 3
            move = (row, col)
            if not game.make_move(move, current_player):
                print("Invalid move, try again.")
                continue
        else:
            _, move = ai.alpha_pruning(game.board, 0, False, float('-inf'), float('inf'))
            game.make_move(move, current_player)
            display_move = move[0] * 3 + move[1] + 1
            print(f"AI chose: {display_move}")
        
        current_player = -current_player
    
    print("Final board:")
    game.print_board()
    if game.check_win(1):
        print("You win!")
    elif game.check_win(-1):
        print("AI wins!")
    else:
        print("Draw!")

if __name__ == "__main__":
    main()

