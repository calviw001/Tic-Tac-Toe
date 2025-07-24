# AI_engine.py
import random 
import engine


def get_move_ai_temp(board: list) -> tuple:
    row_num = random.randint(0, 2)
    column_num = random.randint(0, 2)
    ai_move = (row_num, column_num)
    while not engine.is_move_valid(ai_move, board):
        row_num = random.randint(0, 2)
        column_num = random.randint(0, 2)
        ai_move = (row_num, column_num)
    return ai_move


def get_all_available_moves(board: list) -> list:
    available_moves = []
    for row_num in range(3):
        for column_num in range(3): 
            if board[row_num][column_num] is None:
                available_moves.append((row_num, column_num))
    return available_moves


def make_board_copy(board: list) -> list:
    board_copy = engine.create_board()
    for row_num in range(3):
        for column_num in range(3):
            board_copy[row_num][column_num] = board[row_num][column_num]
    return board_copy
