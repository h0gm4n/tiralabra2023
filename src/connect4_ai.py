import random
import math
import time
from src import connect4_utils
from src import constants

counter = 0


def evaluate_window(window, piece, score):
    """
    Checks four-slot window for potential four-piece lines.

    Args:
        window: Four slot window that is evaluated
        piece: AI's or player's piece
        score: Current score for the column under evaluation
    Return:
        Current score for the column that has been changed during the window's evaluation
    """

    if window.count(piece) == 4:
        score += 100
    if window.count(piece) == 3 and window.count(constants.EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(constants.EMPTY) == 2:
        score += 2

    if window.count(constants.PLAYER_PIECE) == 3 and window.count(constants.EMPTY) == 1:
        score -= 4

    return score


def score_position(board, piece):
    """
    Generates a score heuristically for each column depending on how favorable it is for the AI.

    Args:
        board: Matrix indicating the current state of the board
        piece: AI's or player's piece
    Return:
        Final score of evaluated column
    """
    score = 0

    # Score center column
    center_array = [int(i) for i in list(board[:, constants.COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Check amount of pieces in horizontal windows
    for row in range(constants.ROW_COUNT):
        row_array = [int(i) for i in list(board[row,:])]
        for col in range(constants.COLUMN_COUNT-3):
            window = row_array[col:col+constants.WINDOW_LENGTH]
            score = evaluate_window(window, piece, score)

    # Check amount of pieces in vertical windows
    for col in range(constants.COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, col])]
        for row in range(constants.ROW_COUNT-3):
            window = col_array[row:row+constants.WINDOW_LENGTH]
            score = evaluate_window(window, piece, score)

    # Check amount of pieces in positive diagonal windows
    for row in range(constants.ROW_COUNT-3):
        for col in range(constants.COLUMN_COUNT-3):
            window = [board[row+i][col+i] for i in range(constants.WINDOW_LENGTH)]
            score = evaluate_window(window, piece, score)

    # Check amount of pieces in negative diagonal windows
    for row in range(constants.ROW_COUNT-3):
        for col in range(constants.COLUMN_COUNT-3):
            window = [board[row+3-i][col+i] for i in range(constants.WINDOW_LENGTH)]
            score = evaluate_window(window, piece, score)

    return score


def is_terminal_node(board):
    """
    Checks if next move wins or if no valid locations left

    Args:
        board: Matrix indicating the current state of the board
    Return:
        Boolean
    """
    return connect4_utils.winning_move(board, constants.PLAYER_PIECE) \
           or connect4_utils.winning_move(board, constants.AI_PIECE) \
           or len(connect4_utils.get_valid_locations(board)) == 0


def iterative_deepening(board, max_depth, max_calculation_time):
    """
    Adds search depth one by one until maximum calculation time is exceeded.

    Args:
        board: Matrix indicating the current state of the board
        max_depth: Maximum depth chosen by the player
        max_calculation_time: Maximum calculation time chosen by the player
    Return:
        Best possible move for the AI
    """
    start_time = time.time()
    best_move = None

    for depth in range(1, max_depth + 1):

        if time.time() - start_time > max_calculation_time:
            print("Depth reached:", depth - 1)
            print("Elapsed time:", time.time() - start_time)
            break

        move, minimax_score = minimax(board, depth, -math.inf, math.inf, True)

        if move is not None:
            best_move = move, minimax_score

    return best_move


def minimax(board, depth, alpha, beta, maximizing_player):
    """
    The minimax algorithm that chooses the best possible move for the AI using a binary tree.
    Contains alpha beta pruning, which skips the checking of unnecessary nodes and branches, thus significantly
    speeding up the calculations.

    Args:
        board: Matrix indicating the current state of the board
        depth: The current depth that the iterative deepening function uses when minimax is called
        alpha: Minimum score that the maximizing player is assured of
        beta: Maximum score that the minimizing player is assured of
        maximizing_player: Boolean indicating whether maximizing player's move is being checked
    Return:
        Tuple, (Column that is most favorable for the AI, Score of column)
    """

    valid_locations = connect4_utils.get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if connect4_utils.winning_move(board, constants.AI_PIECE):
                return None, 1000000000000
            if connect4_utils.winning_move(board, constants.PLAYER_PIECE):
                return None, -1000000000000
            return None, 0
        return None, score_position(board, constants.AI_PIECE)

    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = connect4_utils.get_next_open_row(board, col)
            b_copy = board.copy()
            connect4_utils.drop_piece(b_copy, row, col, constants.AI_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    value = math.inf
    column = random.choice(valid_locations)
    for col in valid_locations:
        row = connect4_utils.get_next_open_row(board, col)
        b_copy = board.copy()
        connect4_utils.drop_piece(b_copy, row, col, constants.PLAYER_PIECE)
        new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
        if new_score < value:
            value = new_score
            column = col
        beta = min(beta, value)
        if alpha >= beta:
            break
    return column, value
