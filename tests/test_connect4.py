import unittest
import src.connect4 as connect4
import src.connect4_ai as connect4_ai


class TestConnect4(unittest.TestCase):

    def test_four_in_a_row_wins(self):
        board = connect4.create_board()
        connect4_ai.drop_piece(board, 0, 0, 1)
        connect4_ai.drop_piece(board, 0, 1, 1)
        connect4_ai.drop_piece(board, 0, 2, 1)
        connect4_ai.drop_piece(board, 0, 3, 1)
        self.assertEqual(connect4.winning_move(board, 1), True)

    def test_horizontal_pressure_suggests_best_move(self):
        board = connect4.create_board()
        connect4_ai.drop_piece(board, 0, 0, 1)
        connect4_ai.drop_piece(board, 0, 1, 1)
        connect4_ai.drop_piece(board, 0, 2, 1)

        self.assertEqual(connect4_ai.pick_best_move(board, 2), 3)

    def test_vertical_pressure_suggests_best_move(self):
        board = connect4.create_board()
        connect4_ai.drop_piece(board, 0, 0, 1)
        connect4_ai.drop_piece(board, 1, 0, 1)
        connect4_ai.drop_piece(board, 2, 0, 1)

        self.assertEqual(connect4_ai.pick_best_move(board, 2), 0)


if __name__ == '__main__':
    unittest.main()