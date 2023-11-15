import block
import random


class TetrisGame():
    def __init__(self, board):
        self.board = board

    def generate_tetromino(self):
        block_class = random.choice(block.Tetromino.__subclasses__())
        return block_class(self.board)
