import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import patch
from io import StringIO
import ai_engine


class TestAIGameEngine(unittest.TestCase):
    def test_get_all_available_moves(self):
        # Empty board
        board = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]
        expected = [(0, 0), (0, 1), (0, 2),
                    (1, 0), (1, 1), (1, 2),
                    (2, 0), (2, 1), (2, 2)]
        self.assertEqual(ai_engine.get_all_available_moves(board), expected)
        # Partially filled boards
        board = [['X', None, 'O'],
                 [None, 'X', None],
                 ['O', None, 'X']]
        expected = [(0, 1), (1, 0), (1, 2), (2, 1)]
        self.assertEqual(ai_engine.get_all_available_moves(board), expected)
        board = [['X', 'X', 'X'],
                 ['O', 'O', 'O'],
                 ['X', 'O', None]]
        expected = [(2,2)]
        self.assertEqual(ai_engine.get_all_available_moves(board), expected)
        # Full board
        board = [['X', 'O', 'X'],
                 ['O', 'X', 'O'],
                 ['O', 'X', 'O']]
        expected = []
        self.assertEqual(ai_engine.get_all_available_moves(board), expected)


if __name__ == '__main__':
    unittest.main()
