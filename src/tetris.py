import block
import random
from utils import TetrominoShapes


def generate_tetromino(board):
    block_values = random.choice(list(TetrominoShapes)).value
    return block.Tetromino(block_values['shape'], block_values['color'].value, board)
