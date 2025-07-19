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
        
        self.assertTrue(engine.is_move_valid(('0', '0'), board))
        self.assertTrue(engine.is_move_valid(('1', '2'), board))
        
        self.assertFalse(engine.is_move_valid(('-1', '0'), board))
        self.assertFalse(engine.is_move_valid(('4', '1'), board))
        
        self.assertFalse(engine.is_move_valid(('a', '1'), board))
        
        board[1][1] = 'X'
        self.assertFalse(engine.is_move_valid(('1', '1'), board))
        
        self.assertFalse(engine.is_move_valid(('1'), board))
        self.assertFalse(engine.is_move_valid(('1', '2', '3'), board))


if __name__ == '__main__':
    unittest.main()
