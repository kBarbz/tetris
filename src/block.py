import pygame
from utils import Dimensions, Colours


class Tetromino:
    def __init__(self, shape, color, x, y):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, grid):
        rotated_shape = [[self.shape[y][x] for y in range(len(self.shape))] for x in range(len(self.shape[0]))]
        self.shape = rotated_shape
        if self.out_of_bounds_right(grid):
            self.move(-1, 0)

    def draw(self, surface):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]:
                    pygame.draw.rect(surface, self.color, (self.x * Dimensions.CELL_SIZE.value + col * Dimensions.CELL_SIZE.value, self.y * Dimensions.CELL_SIZE.value + row * Dimensions.CELL_SIZE.value, Dimensions.CELL_SIZE.value, Dimensions.CELL_SIZE.value))

    def is_at_bottom(self, grid):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]:
                    if self.y + row >= grid.height:
                        return True
        return False

    def can_go_left(self):
        if self.x > 0:
            return True
        return False

    def can_go_right(self, grid):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]:
                    if self.x + col + 1 >= grid.width:
                        return False
        return True

    def out_of_bounds_right(self, grid):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]:
                    if self.x + col + 1 > grid.width:
                        return True
        return False

    @staticmethod
    def get_spawn_point(board):
        midpoint = board.width // 2
        return midpoint - 2, 0


class TTetromino(Tetromino):
    def __init__(self, board):
        shape = [[0, 1, 0], [1, 1, 1]]
        color = Colours.PURPLE.value
        x, y = self.get_spawn_point(board)
        super().__init__(shape, color, x, y)


class ITetromino(Tetromino):
    def __init__(self, board):
        shape = [[1, 1, 1, 1]]
        color = Colours.LIGHT_BLUE.value
        x, y = self.get_spawn_point(board)
        super().__init__(shape, color, x, y)


class JTetromino(Tetromino):
    def __init__(self, board):
        shape = [[1, 0, 0], [1, 1, 1]]
        color = Colours.DARK_BLUE.value
        x, y = self.get_spawn_point(board)
        super().__init__(shape, color, x, y)


class LTetromino(Tetromino):
    def __init__(self, board):
        shape = [[0, 0, 1], [1, 1, 1]]
        color = Colours.ORANGE.value
        x, y = self.get_spawn_point(board)
        super().__init__(shape, color, x, y)


class OTetromino(Tetromino):
    def __init__(self, board):
        shape = [[1, 1], [1, 1]]
        color = Colours.YELLOW.value
        x, y = self.get_spawn_point(board)
        super().__init__(shape, color, x, y)

    @staticmethod
    def get_spawn_point(board):
        midpoint = board.width // 2
        return midpoint - 1, 0


class STetromino(Tetromino):
    def __init__(self, board):
        shape = [[0, 1, 1], [1, 1, 0]]
        color = Colours.GREEN.value
        x, y = self.get_spawn_point(board)
        super().__init__(shape, color, x, y)


class ZTetromino(Tetromino):
    def __init__(self, board):
        shape = [[1, 1, 0], [0, 1, 1]]
        color = Colours.RED.value
        x, y = self.get_spawn_point(board)
        super().__init__(shape, color, x, y)