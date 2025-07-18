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
        print(f"{row_num} ", end=" ")
        for column_num in range(3):
            cell = board[row_num][column_num]
            print(f"{cell if cell else '-'} ", end="")
            if column_num < 2:
                print("| ", end="")
        print()
        if row_num < 2:
            print("   ---------")
