import pygame
from utils import Dimensions


class Tetromino:
    def __init__(self, shape, color, grid):
        self.shape = shape
        self.color = color
        self.x = grid.width // 2 - len(shape[0]) // 2
        self.y = 0

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
