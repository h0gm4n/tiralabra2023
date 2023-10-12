from src import constants


def drop_piece(board, row, col, piece):
    """
    Assigns player's piece to chosen column

    Args:
        board: Matrix indicating the current state of the board
        row: Row in which piece is dropped
        col: Column in which piece is dropped
        piece: AI's or player's piece
    """
    board[row][col] = piece


def is_valid_location(board, col):
    """
    Returns boolean that indicates whether chosen column is full

    Args:
        board: Matrix indicating the current state of the board
        col: Column chosen by player
    Return:
        Boolean
    """
    return board[constants.ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    """
    Returns row in which the dropped piece lands

    Args:
        board: Matrix indicating the current state of the board
        col: Column chosen by player
    Return:
        Int
    """
    for row in range(constants.ROW_COUNT):
        if board[row][col] == 0:
            return row


def winning_move(board, piece):
    """
    Checks the whole board for a win

    Args:
        board: Matrix indicating the current state of the board
        piece: AI's or player's piece
    Return:

    """
    # Check horizontal locations for win
    for col in range(constants.COLUMN_COUNT - 3):
        for row in range(constants.ROW_COUNT):
            if board[row][col] == piece and board[row][col + 1] == piece \
                    and board[row][col + 2] == piece and board[row][col + 3] == piece:
                return True

    # Check vertical locations for win
    for col in range(constants.COLUMN_COUNT):
        for row in range(constants.ROW_COUNT - 3):
            if board[row][col] == piece and board[row + 1][col] == piece \
                    and board[row + 2][col] == piece and board[row + 3][col] == piece:
                return True

    # Check positively sloped diagonals
    for col in range(constants.COLUMN_COUNT - 3):
        for row in range(constants.ROW_COUNT - 3):
            if board[row][col] == piece and board[row + 1][col + 1] == piece \
                    and board[row + 2][col + 2] == piece and board[row + 3][col + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for col in range(constants.COLUMN_COUNT - 3):
        for row in range(3, constants.ROW_COUNT):
            if board[row][col] == piece and board[row - 1][col + 1] == piece \
                    and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece:
                return True


# Returns the columns that have empty slots
def get_valid_locations(board):
    """
    Checks each column whether they have empty slots

    Args:
        board: Matrix indicating the current state of the board
    Return:
        List of columns that have empty slots
    """
    valid_locations = []
    for col in range(constants.COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations
