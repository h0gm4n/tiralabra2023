
import random
import math
import src.connect4_utils as connect4_utils
import src.constants as constants


# Increases or lowers the score of column
def evaluate_window(window, piece, score):

    if window.count(piece) == 4:
        score += 100
    if window.count(piece) == 3 and window.count(constants.EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(constants.EMPTY) == 2:
        score += 2

    if window.count(constants.PLAYER_PIECE) == 3 and window.count(constants.EMPTY) == 1:
        score -= 4

    return score


# Checks for potential horizontal, vertical and diagonal win chances and gives a score for each column
def score_position(board, piece):

    score = 0

    # Score center column
    center_array = [int(i) for i in list(board[:, constants.COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Check amount of pieces in horizontal windows
    for r in range(constants.ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(constants.COLUMN_COUNT-3):
            window = row_array[c:c+constants.WINDOW_LENGTH]
            score = evaluate_window(window, piece, score)

    # Check amount of pieces in vertical windows
    for c in range(constants.COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(constants.ROW_COUNT-3):
            window = col_array[r:r+constants.WINDOW_LENGTH]
            score = evaluate_window(window, piece, score)

    # Check amount of pieces in positive diagonal windows
    for r in range(constants.ROW_COUNT-3):
        for c in range(constants.COLUMN_COUNT-3):
            window = [board[r+i][c+i] for i in range(constants.WINDOW_LENGTH)]
            score = evaluate_window(window, piece, score)

    # Check amount of pieces in negative diagonal windows
    for r in range(constants.ROW_COUNT-3):
        for c in range(constants.COLUMN_COUNT-3):
            window = [board[r+3-i][c+i] for i in range(constants.WINDOW_LENGTH)]
            score = evaluate_window(window, piece, score)

    return score


# Returns true if branch has winning move
def is_terminal_node(board):
    return connect4_utils.winning_move(board, constants.PLAYER_PIECE) \
           or connect4_utils.winning_move(board, constants.AI_PIECE) \
           or len(connect4_utils.get_valid_locations(board)) == 0


# Minimax algorithm with alpha beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):

    valid_locations = connect4_utils.get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if connect4_utils.winning_move(board, constants.AI_PIECE):
                return None, 1000000000000
            elif connect4_utils.winning_move(board, constants.PLAYER_PIECE):
                return None, -1000000000000
            else:
                return None, 0
        else:
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

    else:
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
