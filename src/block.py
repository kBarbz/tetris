import pygame
from utils import Dimensions, Colours


class Tetromino:
    shape_index = 0

    def __init__(self, shapes, color, x, y):
        self.shapes = shapes
        self.shape = shapes[0]
        self.color = color
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

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
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]:
                    if self.x + col <= 0:
                        return False
        return True

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

    def rotate_clockwise(self):
        self.shape_index += 1
        if self.shape_index >= len(self.shapes):
            self.shape_index = 0
        self.update_shape()

    def update_shape(self):
        self.shape = self.shapes[self.shape_index]


class TTetromino(Tetromino):
    shapes = [
        [[0, 1, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
        [[0, 1, 0], [1, 1, 0], [0, 1, 0]]
    ]

    def __init__(self, board):
        color = Colours.PURPLE.value
        x, y = self.get_spawn_point(board)
        super().__init__(self.shapes, color, x, y)


class ITetromino(Tetromino):
    shapes = [
        [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
        [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
    ]

    def __init__(self, board):
        color = Colours.LIGHT_BLUE.value
        x, y = self.get_spawn_point(board)
        super().__init__(self.shapes, color, x, y)

    @staticmethod
    def get_spawn_point(board):
        midpoint = board.width // 2
        return midpoint - 2, -1


class JTetromino(Tetromino):
    shapes = [
        [[1, 0, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 1], [0, 1, 0], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 0, 1]],
        [[0, 1, 0], [0, 1, 0], [1, 1, 0]]
    ]

    def __init__(self, board):
        color = Colours.DARK_BLUE.value
        x, y = self.get_spawn_point(board)
        super().__init__(self.shapes, color, x, y)


class LTetromino(Tetromino):
    shapes = [
        [[0, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 1]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 0]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
    ]

    def __init__(self, board):
        color = Colours.ORANGE.value
        x, y = self.get_spawn_point(board)
        super().__init__(self.shapes, color, x, y)


class OTetromino(Tetromino):
    shapes = [
        [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
    ]

    def __init__(self, board):
        color = Colours.YELLOW.value
        x, y = self.get_spawn_point(board)
        super().__init__(self.shapes, color, x, y)


class STetromino(Tetromino):
    shapes = [
        [[0, 1, 1], [1, 1, 0], [0, 0, 0]],
        [[0, 1, 0], [0, 1, 1], [0, 0, 1]],
        [[0, 0, 0], [0, 1, 1], [1, 1, 0]],
        [[1, 0, 0], [1, 1, 0], [0, 1, 0]]
    ]

    def __init__(self, board):
        color = Colours.GREEN.value
        x, y = self.get_spawn_point(board)
        super().__init__(self.shapes, color, x, y)


class ZTetromino(Tetromino):
    shapes = [
        [[1, 1, 0], [0, 1, 1], [0, 0, 0]],
        [[0, 0, 1], [0, 1, 1], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 0], [0, 1, 1]],
        [[0, 1, 0], [1, 1, 0], [1, 0, 0]]
    ]

    def __init__(self, board):
        color = Colours.RED.value
        x, y = self.get_spawn_point(board)
        super().__init__(self.shapes, color, x, y)