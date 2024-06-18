import pygame
from utils import Dimensions, Colours, WALL_KICK_DICT


class Tetromino:
    shape_index = 0
    prev_shape_index = 0
    wall_kicks = [
        [[0, 0], [-1, 0], [-1, 1], [0, -2], [-1, -2]],  # 0->1
        [[0, 0], [1, 0], [1, -1], [0, 2], [1, 2]],  # 1->0
        [[0, 0], [1, 0], [1, -1], [0, 2], [1, 2]],  # 1->2
        [[0, 0], [-1, 0], [-1, 1], [0, -2], [-1, -2]],  # 2->1
        [[0, 0], [1, 0], [1, 1], [0, -2], [1, -2]],  # 2->3
        [[0, 0], [-1, 0], [-1, -1], [0, 2], [-1, 2]],  # 3->2
        [[0, 0], [-1, 0], [-1, -1], [0, 2], [-1, 2]],  # 3->0
        [[0, 0], [1, 0], [1, 1], [0, -2], [1, -2]]  # 0->3
    ]

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
                    if self.y + row + 1 >= grid.height:
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

    @staticmethod
    def get_queue_point(board, index):
        midpoint = (board.width // 2)
        return midpoint + 6, index * 3 + 2

    @staticmethod
    def get_start_point(board):
        midpoint = board.width // 2
        return midpoint - 2, 0

    def set_start_point(self, board):
        self.x, self.y = self.get_start_point(board)

    def set_to_queue_point(self, board, index):
        self.x, self.y = self.get_queue_point(board, index)

    def rotate_clockwise(self, grid):
        self.prev_shape_index = self.shape_index
        self.shape_index += 1
        if self.shape_index >= len(self.shapes):
            self.shape_index = 0
        self.update_shape(grid)

    def rotate_c_clockwise(self, grid):
        self.prev_shape_index = self.shape_index
        self.shape_index -= 1
        if self.shape_index < 0:
            self.shape_index = len(self.shapes) - 1
        self.update_shape(grid)

    def update_shape(self, grid):
        x, y = self.get_location_post_wall_kick(grid)
        self.x = x
        self.y = y
        self.shape = self.shapes[self.shape_index]

    def get_location_post_wall_kick(self, grid):
        new_x, new_y = 0, 0
        for test in range(5):
            n = self.get_rotation()
            new_x, new_y = self.wall_kicks[n][test]
            if self.valid_wall_kick(self.x + new_x, self.y + new_y, grid):
                break
        return self.x + new_x, self.y + new_y

    def valid_wall_kick(self, x, y, grid):
        return not self.out_of_bounds(self.shapes[self.shape_index], grid, x, y)

    @staticmethod
    def out_of_bounds(shape, grid, x, y):
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col]:
                    if x + col + 1 > grid.width:
                        return True
                    if x + col < 0:
                        return True
                    if y + row + 1 > grid.height:
                        return True
                    if y + row < 0:
                        return True
        return False

    def get_rotation(self):
        return WALL_KICK_DICT[(self.prev_shape_index, self.shape_index)]

class TTetromino(Tetromino):
    shapes = [
        [[0, 1, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
        [[0, 1, 0], [1, 1, 0], [0, 1, 0]]
    ]

    def __init__(self, board):
        color = Colours.PURPLE.value
        x, y = self.get_start_point(board)
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
        x, y = self.get_start_point(board)
        super().__init__(self.shapes, color, x, y)


class JTetromino(Tetromino):
    shapes = [
        [[1, 0, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 1], [0, 1, 0], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 0, 1]],
        [[0, 1, 0], [0, 1, 0], [1, 1, 0]]
    ]

    def __init__(self, board):
        color = Colours.DARK_BLUE.value
        x, y = self.get_start_point(board)
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
        x, y = self.get_start_point(board)
        super().__init__(self.shapes, color, x, y)


class OTetromino(Tetromino):
    shapes = [
        [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
    ]

    def __init__(self, board):
        color = Colours.YELLOW.value
        x, y = self.get_start_point(board)
        super().__init__(self.shapes, color, x, y)

    def update_shape(self, grid):
        self.shape = self.shapes[self.shape_index]


class STetromino(Tetromino):
    shapes = [
        [[0, 1, 1], [1, 1, 0], [0, 0, 0]],
        [[0, 1, 0], [0, 1, 1], [0, 0, 1]],
        [[0, 0, 0], [0, 1, 1], [1, 1, 0]],
        [[1, 0, 0], [1, 1, 0], [0, 1, 0]]
    ]

    def __init__(self, board):
        color = Colours.GREEN.value
        x, y = self.get_start_point(board)
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
        x, y = self.get_start_point(board)
        super().__init__(self.shapes, color, x, y)