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
            print(f"{cell if cell else ' - '}", end="")
            if column_num < 2:
                print("|", end="")
        print()
        if row_num < 2:
            print("   ---------")


def get_move() -> tuple:
    row_num = input("Enter row number: ")
    column_num = input("Enter column number: ")
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

# print_board(create_board())
# print(get_move())