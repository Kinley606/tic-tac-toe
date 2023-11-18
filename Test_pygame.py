import pygame
import numpy as np
import unittest

# Constants
WIDTH = 600
HEIGHT = 600
BOARD_ROWS = 3
BOARD_COLUMNS = 3

# (existing code)

class TicTacToeGame:
    def __init__(self):
        self.board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))
        self.player = 1
        self.game_over = False

    def mark_square(self, row, col):
        self.board[row][col] = self.player

    def switch_player(self):
        self.player = 3 - self.player  # Switch between players 1 and 2

    def play(self, row, col):
        if not self.game_over and TicTacToeGame.available_square(self.board, row, col):
            self.mark_square(row, col)
           
    def is_game_over(self):
        return self.game_over


    @staticmethod
    def available_square(board, row, col):
        return board[row][col] == 0

   
   

# Now, unit tests

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = TicTacToeGame()

    def tearDown(self):
        pygame.quit()

    def test_mark_square(self):
        self.game.mark_square(0, 0)
        self.assertEqual(self.game.board[0][0], 1)

    def test_switch_player(self):
        initial_player = self.game.player
        self.game.switch_player()
        self.assertEqual(self.game.player, 3 - initial_player)

    def test_play(self):
        self.game.play(0, 0)
        self.assertEqual(self.game.board[0][0], 1)
        self.assertFalse(self.game.is_game_over())


if __name__ == '__main__':
    unittest.main()
