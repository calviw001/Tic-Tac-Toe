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


def minimax_score(board: list, current_player_piece: str) -> int:
    # player_piece = 'X'
    # ai_piece = 'O'
    # Base cases
    if engine.check_winner(board):
        winning_piece = engine.check_winner(board)
        if winning_piece == 'X':
            return -10
        else:
            return 10
    elif engine.is_board_full(board):
        return 0
    # Recursive case
    all_moves = get_all_available_moves(board)
    scores = []
    for each_move in all_moves:
        new_board = make_board_copy(board)
        engine.update_board(each_move, new_board, current_player_piece)
        if current_player_piece == 'X':
            score = minimax_score(new_board, 'O')
        else:
            score = minimax_score(new_board, 'X')
        scores.append(score)
    if current_player_piece == 'X':
        return min(scores)
    else:
        return max(scores)


def get_move_ai(board: list) -> tuple:
    move = None
    move_score = -99
    ai_piece = 'O' 
    all_moves = get_all_available_moves(board)
    for each_move in all_moves:
        new_board = make_board_copy(board)
        engine.update_board(each_move, new_board, ai_piece)
        current_move_score = minimax_score(new_board, ai_piece)
        if current_move_score > move_score:
            move = each_move
            move_score = current_move_score
    return move
