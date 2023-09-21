import src.constants as constants


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[constants.ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(constants.ROW_COUNT):
        if board[r][col] == 0:
            return r


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(constants.COLUMN_COUNT - 3):
        for r in range(constants.ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(constants.COLUMN_COUNT):
        for r in range(constants.ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(constants.COLUMN_COUNT - 3):
        for r in range(constants.ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(constants.COLUMN_COUNT - 3):
        for r in range(3, constants.ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


# Returns the columns that have empty slots
def get_valid_locations(board):
    valid_locations = []
    for col in range(constants.COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations