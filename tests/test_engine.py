import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import patch
from io import StringIO
import engine


class TestGameEngine(unittest.TestCase):

    def test_board_structure(self):
        # Test the exact structure of the board
        board = engine.create_board()
        expected = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(board, expected)
        for row in board:
            for cell in row:
                self.assertIsNone(cell)


    @patch('builtins.input', side_effect=['0', '2'])
    def test_get_move(self, mock_input):
        # Test that get_move returns correct tuple with normal input
        result = engine.get_move()
        self.assertEqual(result, ('0', '2'))

    
    def test_is_move_valid(self):
        # Test move validation
        board = engine.create_board()
        # Valid move
        self.assertTrue(engine.is_move_valid(('0', '0'), board))
        self.assertTrue(engine.is_move_valid(('1', '2'), board))
        # Out of bounds move
        self.assertFalse(engine.is_move_valid(('-1', '0'), board))
        self.assertFalse(engine.is_move_valid(('4', '1'), board))
        # Move contains non numbers
        self.assertFalse(engine.is_move_valid(('a', '1'), board))
        # Move tries to take up occupied space
        board[1][1] = 'X'
        self.assertFalse(engine.is_move_valid(('1', '1'), board))
        # Move tuple is not length 2
        self.assertFalse(engine.is_move_valid(('1'), board))
        self.assertFalse(engine.is_move_valid(('1', '2', '3'), board))


    def test_update_move(self):
        # Test updating board with move
        board = engine.create_board()
        engine.update_board(('1', '1'), board, 'X')
        self.assertEqual(board[1][1], 'X')
        engine.update_board(('0', '2'), board, 'O')
        self.assertEqual(board[0][2], 'O')


    def test_is_board_full(self):
        # Test checking of a board is full or not
        # Not full
        board = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]
        self.assertFalse(engine.is_board_full(board))
        board = [['X', None, 'O'],
                 [None, 'X', None],
                 ['O', None, 'X']]
        self.assertFalse(engine.is_board_full(board))
        # Is full
        board = [['X', 'O', 'X'],
                 ['O', 'X', 'O'],
                 ['O', 'X', 'O']]
        self.assertTrue(engine.is_board_full(board))


    def test_check_winner(self):
        # Test checking of a winner or not
        # Rows
        board = [['X', 'X', 'X'],
                 ['O', None, 'O'],
                 ['O', 'X', None]]
        self.assertEqual(engine.check_winner(board), 'X')
        # Columns
        board = [['O', None, 'X'],
                 ['O', 'X', 'O'],
                 ['O', 'X', None]]
        self.assertEqual(engine.check_winner(board), 'O')
        # Top-left to bottom-right
        board = [['X', 'O', 'X'],
                 ['O', 'X', 'O'],
                 ['O', 'X', 'X']]
        self.assertEqual(engine.check_winner(board), 'X')
        # Top-right to bottom-left
        board = [['X', 'O', 'O'],
                 ['O', 'O', 'X'],
                 ['O', 'X', None]]
        self.assertEqual(engine.check_winner(board), 'O')
        # Partially filled board with no winner
        board = [['X', 'O', 'X'],
                 ['O', 'X', 'O'],
                 ['O', 'X', None]]
        self.assertIsNone(engine.check_winner(board))
        # Full board with no winner
        board = [['X', 'O', 'X'],
                 ['X', 'X', 'O'],
                 ['O', 'X', 'O']]
        self.assertIsNone(engine.check_winner(board))


if __name__ == '__main__':
    unittest.main()
