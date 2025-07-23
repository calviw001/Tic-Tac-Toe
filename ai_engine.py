# AI_engine.py
import random 
from engine import is_move_valid


def get_move_ai_temp(board: list):
    row_num = random.randint(0, 2)
    column_num = random.randint(0, 2)
    ai_move = (row_num, column_num)
    while not is_move_valid(ai_move, board):
        row_num = random.randint(0, 2)
        column_num = random.randint(0, 2)
        ai_move = (row_num, column_num)
    return ai_move
