from utils import Dimensions, Colours
import pygame


class Board:
    def __init__(self):
        self.display = pygame.display
        self.height = Dimensions.GRID_HEIGHT.value
        self.width = Dimensions.GRID_WIDTH.value
        self.screen = self.display.set_mode((self.width * Dimensions.CELL_SIZE.value, self.height * Dimensions.CELL_SIZE.value))
        self.color = Colours.BLACK.value

    def draw(self):
        self.screen.fill(self.color)

    def update(self):
        self.display.flip()

    def draw_grid(self):
        for x in range(0, self.width * Dimensions.CELL_SIZE.value, Dimensions.CELL_SIZE.value):
            pygame.draw.line(self.screen, Colours.WHITE.value, (x, 0), (x, self.height * Dimensions.CELL_SIZE.value))
        for y in range(0, self.height * Dimensions.CELL_SIZE.value, Dimensions.CELL_SIZE.value):
            pygame.draw.line(self.screen, Colours.WHITE.value, (0, y), (self.width * Dimensions.CELL_SIZE.value, y))