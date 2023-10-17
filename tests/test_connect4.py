import unittest
import numpy as np
import math
import src.connect4_ui as connect4
import src.connect4_ai as connect4_ai
import src.connect4_utils as connect4_utils


class TestConnect4(unittest.TestCase):

    def test_ai_chooses_crucial_column_two_pieces(self):
        """
        Tests if AI chooses the column that is crucial to avoid loss (2 player pieces)
        """
        board = np.zeros((6, 7))
        board[0][3] = 1
        board[1][3] = 2
        board[0][4] = 1
        col, minmax_score = connect4_ai.minimax(board, 5, -math.inf, math.inf, True)
        self.assertTrue(col in [2, 5])

    def test_ai_chooses_winning_column(self):
        """
        Tests if AI chooses the column that wins the game automatically
        """
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[0][3] = 2
        board[0][1] = 1
        board[1][3] = 2
        board[1][0] = 1
        board[2][3] = 2
        board[1][1] = 1
        col, minmax_score = connect4_ai.minimax(board, 5, -math.inf, math.inf, True)
        self.assertEqual(col, 3)

    def test_ai_blocks_players_immediate_win(self):
        """
        Tests if AI chooses the column that is crucial to avoid loss (3 player pieces)
        """
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[1][0] = 1
        board[2][0] = 1
        col, minmax_score = connect4_ai.minimax(board, 5, -math.inf, math.inf, True)
        self.assertEqual(col, 0)

    def test_ai_wins_automatically_in_depth_8(self):
        """
        Test if heuristic scoring gives a column a winning score (1000000000000) if automatic victory can be seen 8 turns ahead, when chosen depth is 8
        """
        board = np.zeros((6, 7))
        # Initiate board with a situation that's beatable in 8 moves by the AI (according to connect4.gamesolver.org)
        board[0][0] = 1
        board[1][0] = 1
        board[0][2] = 1
        board[1][2] = 1
        board[0][3] = 1
        board[3][4] = 1
        board[0][5] = 1
        board[1][2] = 1
        board[2][0] = 1
        board[0][1] = 2
        board[2][2] = 2
        board[1][3] = 2
        board[4][4] = 2
        board[2][4] = 2
        board[1][4] = 2
        board[0][4] = 2
        board[2][2] = 2
        board[3][0] = 2
        board[1][5] = 1
        print(np.flip(board, 0))
        col, max_score = connect4_ai.iterative_deepening(board, 8, 60)
        print(max_score)
        self.assertEqual(max_score, 1000000000000)




if __name__ == '__main__':
    unittest.main()