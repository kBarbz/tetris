import block
import random
import pygame
from utils import Dimensions, SCORE_MULTIPLIER, SCORE_AMOUNT_BY_ROWS


class TetrisGame():
    def __init__(self, board):
        self.board = board
        self.game_grid = self.generate_grid()
        self.score = 0
        self.queue = []
        self.fill_queue()

    def add_new_tetromino_to_queue(self):
        block_class = random.choice(block.Tetromino.__subclasses__())
        new_tetromino = block_class(self.board)
        self.queue.append(new_tetromino)

    def fill_queue(self):
        while len(self.queue) < 3:
            self.add_new_tetromino_to_queue()
        self.update_queue()

    def update_queue(self):
        for i, t in enumerate(self.queue):
            t.set_to_queue_point(self.board, i)

    def get_latest_tetromino(self):
        next_tetromino = self.queue.pop(0)
        self.fill_queue()
        next_tetromino.set_start_point(self.board)
        return next_tetromino

    def generate_tetromino(self):
        next_tetromino = self.get_latest_tetromino()
        if self.check_for_collision(next_tetromino.shape, next_tetromino.x, next_tetromino.y):
            return None
        return next_tetromino

    def generate_grid(self):
        return [[0 for _ in range(self.board.width)] for _ in range(self.board.height)]

    def add_to_landed(self, tetromino):
        for row in range(len(tetromino.shape)):
            for col in range(len(tetromino.shape[row])):
                if tetromino.shape[row][col]:
                    self.game_grid[tetromino.y + row][tetromino.x + col] = tetromino.color

        self.check_for_clear()

    def check_for_clear(self):
        rows_to_clear = []
        for row in range(len(self.game_grid)):
            if all(cell != 0 for cell in self.game_grid[row]):
                rows_to_clear.append(row)

        total_cleared_rows = len(rows_to_clear)
        if total_cleared_rows > 0:
            self.update_score(total_cleared_rows)
            for row in rows_to_clear:
                del self.game_grid[row]
                self.game_grid.insert(0, [0] * self.board.width)

    def update_score(self, total_cleared_rows):
        self.score += SCORE_AMOUNT_BY_ROWS[total_cleared_rows] * SCORE_MULTIPLIER

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
