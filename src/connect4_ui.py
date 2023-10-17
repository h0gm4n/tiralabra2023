import sys
import math
import numpy as np
import pygame
from src import connect4_ai
from src import connect4_utils
from src import constants
import time


def run_game(depth, max_waiting_time):
    """
    Is called when the game is run and has all the functions related to the UI.
    Contains the game loop.

    Args:
        depth: The maximum depth chosen by player
        max_waiting_time: The maximum time the player is willing to wait for the AI's calculations to complete.
    """
    def create_board():
        board = np.zeros((constants.ROW_COUNT, constants.COLUMN_COUNT))
        return board

    def print_board(board):
        print(np.flip(board, 0))

    def draw_board(board):
        for col in range(constants.COLUMN_COUNT):
            for row in range(constants.ROW_COUNT):
                pygame.draw.rect(screen, constants.BLUE,
                                (col * constants.SQUARESIZE,
                                row * constants.SQUARESIZE + constants.SQUARESIZE,
                                constants.SQUARESIZE, constants.SQUARESIZE))
                pygame.draw.circle(screen, constants.BLACK, (
                int(col * constants.SQUARESIZE + constants.SQUARESIZE / 2),
                int(row * constants.SQUARESIZE + constants.SQUARESIZE + constants.SQUARESIZE / 2)),
                                constants.RADIUS)

        for col in range(constants.COLUMN_COUNT):
            for row in range(constants.ROW_COUNT):
                if board[row][col] == 1:
                    pygame.draw.circle(screen, constants.RED, (
                    int(col * constants.SQUARESIZE + constants.SQUARESIZE / 2),
                    height - int(row * constants.SQUARESIZE + constants.SQUARESIZE / 2)),
                                       constants.RADIUS)
                elif board[row][col] == 2:
                    pygame.draw.circle(screen, constants.YELLOW, (
                    int(col * constants.SQUARESIZE + constants.SQUARESIZE / 2),
                    height - int(row * constants.SQUARESIZE + constants.SQUARESIZE / 2)),
                                       constants.RADIUS)
        pygame.display.update()

    board = create_board()
    print_board(board)
    game_over = False
    game_over_screen = False
    turn = constants.PLAYER

    pygame.init()

    width = constants.COLUMN_COUNT * constants.SQUARESIZE
    height = (constants.ROW_COUNT + 1) * constants.SQUARESIZE

    size = (width, height)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 55)
    restart_font = pygame.font.SysFont("monospace", 25)

    while not game_over_screen:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, constants.BLACK, (0, 0, width, constants.SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, constants.RED,
                                       (posx, int(constants.SQUARESIZE / 2)), constants.RADIUS)
                else:
                    pygame.draw.circle(screen, constants.YELLOW,
                                       (posx, int(constants.SQUARESIZE / 2)), constants.RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, constants.BLACK, (0, 0, width, constants.SQUARESIZE))

                # Ask for Player 1 Input
                if turn == constants.PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx / constants.SQUARESIZE))

                    if connect4_utils.is_valid_location(board, col):
                        row = connect4_utils.get_next_open_row(board, col)
                        connect4_utils.drop_piece(board, row, col, constants.PLAYER_PIECE)

                        if connect4_utils.winning_move(board, constants.PLAYER_PIECE):
                            label = myfont.render("Player wins!", 1, constants.RED)
                            screen.blit(label, (200, 10))
                            game_over_screen = True

                        turn += 1
                        turn = turn % 2

                        print_board(board)
                        draw_board(board)


        """
        Calls the iterative deepening function, which then calls the minimax function etc.
        """
        if turn == constants.AI and not game_over:

            # Run minimax with chosen depth
            start = time.time()
            # col, minimax_score = connect4_ai.minimax(board, depth, -math.inf, math.inf, True)
            col, minimax_score = connect4_ai.iterative_deepening(board, depth, max_waiting_time)
            print(col, minimax_score)
            end = time.time()

            print("Elapsed time:", end - start)

            if connect4_utils.is_valid_location(board, col):
                # pygame.time.wait(500)
                row = connect4_utils.get_next_open_row(board, col)
                connect4_utils.drop_piece(board, row, col, constants.AI_PIECE)

                if connect4_utils.winning_move(board, constants.AI_PIECE):
                    label = myfont.render("AI wins!", 1, constants.YELLOW)
                    screen.blit(label, (200, 10))
                    restart = restart_font.render("Play again", 1, constants.RED)
                    screen.blit(restart, (10, 10))
                    game_over_screen = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over_screen:

            while not game_over:
                restart = restart_font.render("Play again", 1, constants.RED)
                yes = restart_font.render("Yes", 1, constants.RED)
                no = restart_font.render("No", 1, constants.YELLOW)
                screen.blit(restart, (10, 10))
                screen.blit(yes, (10, 50))
                screen.blit(no, (80, 50))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 120 > event.pos[0] >= 80 and 80 >= event.pos[1] >= 50:
                            game_over = True
                        elif 60 > event.pos[0] >= 10 and 80 >= event.pos[1] >= 50:
                            run_game(depth, max_waiting_time)
                #pygame.time.wait(3000)
