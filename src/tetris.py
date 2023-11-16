import block
import random
import pygame
from utils import Dimensions

class TetrisGame():
    def __init__(self, board):
        self.board = board
        self.game_grid = self.generate_grid()

    def generate_tetromino(self):
        block_class = random.choice(block.Tetromino.__subclasses__())
        return block_class(self.board)

    def generate_grid(self):
        return [[0 for _ in range(self.board.width)] for _ in range(self.board.height)]

    def add_to_landed(self, tetromino):
        for row in range(len(tetromino.shape)):
            for col in range(len(tetromino.shape[row])):
                if tetromino.shape[row][col]:
                    self.game_grid[tetromino.y + row][tetromino.x + col] = tetromino.color

    def draw_game_grid(self):
        for row in range(len(self.game_grid)):
            for col in range(len(self.game_grid[row])):
                if self.game_grid[row][col]:
                    pygame.draw.rect(self.board.screen, self.game_grid[row][col], (col * Dimensions.CELL_SIZE.value, row * Dimensions.CELL_SIZE.value, Dimensions.CELL_SIZE.value, Dimensions.CELL_SIZE.value))

    def check_for_collision(self, shape, x, y):
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col]:
                    if self.game_grid[y + row][x + col]:
                        return True
