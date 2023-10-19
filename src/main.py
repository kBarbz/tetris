import pygame
import tetris
from board import Board
from utils import Colours

# pygame setup
pygame.init()
board = Board()
clock = pygame.time.Clock()
running = True
dt = 0

tetromino = tetris.generate_tetromino(board)

move_delay = 20
move_speed = 1
delay_counter = move_delay

font = pygame.font.Font(None, 36)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and tetromino.can_go_left():
                tetromino.move(-move_speed, 0)
            elif event.key == pygame.K_RIGHT and tetromino.can_go_right(board):
                tetromino.move(move_speed, 0)
            elif event.key == pygame.K_UP:  # Rotate the sprite when 'R' is pressed
                tetromino.rotate(board)

    delay_counter -= move_speed
    if delay_counter <= move_speed:
        tetromino.move(0, 1)
        if tetromino.is_at_bottom(board):
            tetromino = tetris.generate_tetromino(board) # Wrap to the top
        delay_counter = move_delay

    # DEBUGGER
    text = font.render(f"x:{tetromino.x} | y:{tetromino.y}", True, Colours.WHITE.value)
    text_rect = text.get_rect()
    text_rect.center = (100, 100)

    board.draw()
    tetromino.draw(board.screen)
    board.draw_grid()
    board.screen.blit(text, text_rect)
    board.update()

    clock.tick(60)

pygame.quit()