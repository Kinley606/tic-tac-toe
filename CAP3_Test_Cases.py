import pygame
import numpy as np
import sys
import unittest

mixer = pygame.mixer
pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLUMNS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((640, 480))

mixer.music.load('Luke-Bergs-Take-It-Easy(chosic.com).mp3')
mixer.music.play()

background = pygame.image.load("xo.jpg").convert()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')

board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))


def draw_lines():
    pygame.draw.line(background, WHITE, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(background, WHITE, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(background, WHITE, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(background, WHITE, (400, 0), (400, 600), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 1:
                pygame.draw.circle(background, RED, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(background, BLUE, (col * 200 + SPACE, row * 200 + 200 - SPACE),
                                 (col * 200 - SPACE + 200, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(background, BLUE, (col * 200 + SPACE, row * 200 + SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    for col in range(BOARD_COLUMNS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    return False



class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        mixer.init()

    def test_mark_square(self):
        mark_square(0, 0, 1)
        self.assertEqual(board[0][0], 1)
        mark_square(1, 1, 2)
        self.assertEqual(board[1][1], 2)

    def test_available_square(self):
        self.assertTrue(available_square(0, 0))
        mark_square(0, 0, 1)
        self.assertFalse(available_square(0, 0))

    def test_is_board_full(self):
        self.assertFalse(is_board_full())
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLUMNS):
                mark_square(i, j, 1)
        self.assertTrue(is_board_full())

    def test_check_win(self):
        self.assertFalse(check_win(1))
        mark_square(0, 0, 1)
        mark_square(0, 1, 1)
        mark_square(0, 2, 1)
        self.assertTrue(check_win(1))

    def tearDown(self):
        mixer.quit()


if __name__ == '__main__':
    unittest.main()

   