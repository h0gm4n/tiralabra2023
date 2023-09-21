import unittest
import numpy as np
import math
import src.connect4_ui as connect4
import src.connect4_ai as connect4_ai
import src.connect4_utils as connect4_utils


class TestConnect4(unittest.TestCase):

    def test_minimax(self):
        board = np.zeros((6, 7))
        board[5][3] = 1
        board[4][3] = 2
        board[5][4] = 1
        print(board)
        col, minmax_score = connect4_ai.minimax(board, 5, -math.inf, math.inf, True)
        self.assertEqual((col, minmax_score), (5, 9))
        #connect4_ai.minimax()
        #pass


if __name__ == '__main__':
    unittest.main()