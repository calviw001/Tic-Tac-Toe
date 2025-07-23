# Main.py
import engine
import ai_engine


def main() -> None:
    play()


def play() -> None:
    print("Welcome to Tic-Tac-Toe!")
    # Ask player if they want to go first
    while True:
        player_turn_choice = input("Do you want to go first or second? (Enter 'first' or 'second'): ").lower()
        if player_turn_choice in ['first', 'second']:
            break
        print("Invalid answer. Try again!")
    # Start the game
    board = engine.create_board()
    player_piece = 'X'
    ai_piece = 'O'
    # Initialize the current player
    if player_turn_choice == 'first':
        current_player = 'Player'
    else:
        current_player = 'AI'
    # Game loop
    while True:
        # Get and process move
        if current_player == 'Player':
            engine.print_board(board)
            print("\nYour turn (X)")
            while True:
                move = engine.get_move()
                if engine.is_move_valid(move, board):
                    break
                print("Invalid move. Try again.")
            engine.update_board(move, board, player_piece)
            current_player = 'AI'
        else:
            engine.print_board(board)
            print("\nAI's turn (O)")
            ai_move = ai_engine.get_move_ai_temp(board)
            engine.update_board(ai_move, board, ai_piece)
            current_player = 'Player'
        # Check for winner or tie
        has_winner = engine.check_winner(board)
        if has_winner:
            engine.print_board(board)
            if has_winner == 'X':
                print("You win!")
            else:
                print("You lose!")
            break
        elif engine.is_board_full(board):
            engine.print_board(board)
            print("It's a tie!")
            break


if __name__ == '__main__':
    main()