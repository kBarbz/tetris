import pygame
from utils import Dimensions, Colours


class GameDisplay:
    def __init__(self, board):
        self.board = board
        self.display = pygame.display
        self.screen = self.display.get_surface()
        self.board_width = self.board.width * Dimensions.CELL_SIZE.value
        self.board_height = self.board.height * Dimensions.CELL_SIZE.value
        self.font = pygame.font.SysFont('Arial', 24)
        self.score = 0
        self.queue = []
        self.text_color = Colours.BLACK.value
        self.background_color = Colours.WHITE.value

    def set_score(self, score):
        self.score = score

    def set_queue(self, queue):
        self.queue = queue

    def draw_score(self):
        score_text = self.font.render(f'Score: {self.score}', True, self.text_color)
        self.screen.blit(score_text, (self.board_width + 20, 20))

    def draw_queue(self):
        for index, tetromino in enumerate(self.queue):
            tetromino.draw(self.screen)

    def update_display(self):
        # Fill the right side of the screen where the extra display is
        self.screen.fill(self.background_color,
                         (self.board_width, 0, self.board.extra_width, self.screen.get_height()))
        self.draw_score()
        self.draw_queue()

