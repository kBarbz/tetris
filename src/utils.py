from enum import Enum

SCORE_MULTIPLIER = 1000

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


WALL_KICK_DICT = {
    (0, 1): 0,
    (1, 0): 1,
    (1, 2): 2,
    (2, 1): 3,
    (2, 3): 4,
    (3, 2): 5,
    (3, 0): 6,
    (0, 3): 7
}