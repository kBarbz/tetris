from enum import Enum


class Dimensions(Enum):
    GRID_WIDTH = 10
    GRID_HEIGHT = 20
    CELL_SIZE = 30


class Colours(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    LIGHT_BLUE = (0, 255, 255)
    DARK_BLUE = (0, 0, 139)
    ORANGE = (255, 140, 0)
    GREEN = (0, 128, 0)
    PURPLE = (230, 230, 250)


class TetrominoShapes(Enum):
    I = {
        'shape': [[1, 1, 1, 1]],
        'color': Colours.LIGHT_BLUE
    }
    J = {
        'shape': [[1, 1, 1], [0, 0, 1]],
        'color': Colours.DARK_BLUE
    }
    L = {
        'shape': [[0, 0, 1], [1, 1, 1]],
        'color': Colours.ORANGE
    }
    O = {
        'shape': [[1, 1], [1, 1]],
        'color': Colours.YELLOW
    }
    S = {
        'shape': [[0, 1, 1], [1, 1, 0]],
        'color': Colours.GREEN
    }
    T = {
        'shape': [[0, 1, 0], [1, 1, 1]],
        'color': Colours.PURPLE
    }
    Z = {
        'shape': [[0, 1, 1], [1, 1, 0]],
        'color': Colours.RED
    }