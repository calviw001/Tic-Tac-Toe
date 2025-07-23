# Engine.py


def create_board() -> list:
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    return board


def print_board(board: list) -> None:
    print("   0   1   2")
    for row_num in range(3):
        print(f"{row_num}", end=" ")
        for column_num in range(3):
            cell = board[row_num][column_num]
            #print(f"{cell if cell else ' - '}", end="")
            if cell:
                print(f" {cell} ", end="")
            else:
                print(f" - ", end="")
            if column_num < 2:
                print("|", end="")
        print()
        if row_num < 2:
            print("   ---------")


def get_move() -> tuple:
    row_num = input("Enter row number: ").strip()
    column_num = input("Enter column number: ").strip()
    return (row_num, column_num)


def is_move_valid(move: tuple, board: list) -> bool:
    # Move is of length 2
    if len(move) == 2:
        row_num = move[0]
        column_num = move[1]
        # Move consists of numbers
        try:
            row_num = int(move[0])
            column_num = int(move[1])
        except ValueError:
            return False
        # Move numbers are in bounds
        if not (0 <= row_num < 3 and 0 <= column_num < 3):
            return False
        # Move is not taken already
        if board[row_num][column_num] is not None:
            return False
        return True
    else:
        return False
    

def update_board(move: tuple, board: list, player_piece: str) -> None:
    board[int(move[0])][int(move[1])] = player_piece


def is_board_full(board: list) -> bool:
    for row in board:
        if None in row:
            return False
    return True 


def check_winner(board: list):
    winning_piece = None
    # Check rows
    for row_num in range(3):
        if board[row_num][0] == board[row_num][1] == board[row_num][2] and board[row_num][0] is not None:
            winning_piece = board[row_num][0]
            return winning_piece
    # Check columns
    for column_num in range(3):
        if board[0][column_num] == board[1][column_num] == board[2][column_num] and board[0][column_num] is not None:
            winning_piece = board[0][column_num]
            return winning_piece
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winning_piece = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][0] is not None:
        winning_piece = board[0][2]
    return winning_piece


# print_board(create_board())
# print(get_move())