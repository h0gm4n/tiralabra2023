import unittest
import numpy as np
import math
import src.connect4_ui as connect4
import src.connect4_ai as connect4_ai
import src.connect4_utils as connect4_utils


class TestConnect4(unittest.TestCase):

    def test_ai_chooses_crucial_column_two_pieces(self):
        board = np.zeros((6, 7))
        board[5][3] = 1
        board[4][3] = 2
        board[5][4] = 1
        col, minmax_score = connect4_ai.minimax(board, 5, -math.inf, math.inf, True)
        self.assertTrue(col in [2, 5])

    def test_ai_chooses_winning_column(self):
        board = np.zeros((6, 7))
        board[5][0] = 1
        board[5][3] = 2
        board[5][1] = 1
        board[4][3] = 2
        board[4][0] = 1
        board[3][3] = 2
        board[4][1] = 1
        col, minmax_score = connect4_ai.minimax(board, 5, -math.inf, math.inf, True)
        self.assertTrue(col, 3)

    def test_ai_blocks_players_immediate_win(self):
        board = np.zeros((6, 7))
        board[5][0] = 1
        board[4][0] = 1
        board[3][0] = 1
        col, minmax_score = connect4_ai.minimax(board, 5, -math.inf, math.inf, True)
        self.assertTrue(col, 0)


if __name__ == '__main__':
    unittest.main()