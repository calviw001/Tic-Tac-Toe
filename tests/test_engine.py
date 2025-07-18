import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from engine import create_board


class TestGameEngine(unittest.TestCase):

    def test_board_structure(self):
        # Test the exact structure of the board
        board = create_board()
        expected = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(board, expected)
        for row in board:
            for cell in row:
                self.assertIsNone(cell)


if __name__ == '__main__':
    unittest.main()
