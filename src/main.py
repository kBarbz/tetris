import pygame
from tetris import TetrisGame
from board import Board
from utils import Colours

# pygame setup
pygame.init()
board = Board()
clock = pygame.time.Clock()
running = True
dt = 0

tetris_game = TetrisGame(board)
tetrominos = [tetris_game.generate_tetromino()]
current_tetromino = 0

move_delay = 20
move_speed = 1
delay_counter = move_delay

font = pygame.font.Font(None, 36)

while running:
    live_t = tetrominos[0]
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and live_t.can_go_left() and not tetris_game.check_for_collision(live_t.shape, live_t.x - 1, live_t.y):
                live_t.move(-move_speed, 0)
            elif event.key == pygame.K_RIGHT and live_t.can_go_right(board) and not tetris_game.check_for_collision(live_t.shape, live_t.x + 1, live_t.y):
                live_t.move(move_speed, 0)
            elif event.key == pygame.K_UP:  # Rotate the sprite when 'R' is pressed
                live_t.rotate_clockwise(board)
            elif event.key == pygame.K_SPACE:  # Rotate the sprite when 'R' is pressed
                live_t.move(0, 100)
            elif event.key == pygame.K_z:  # Rotate the sprite when 'R' is pressed
                live_t.rotate_c_clockwise(board)

    delay_counter -= move_speed
    if delay_counter <= move_speed:
        live_t.move(0, 1)
        if live_t.is_at_bottom(board) or tetris_game.check_for_collision(live_t.shape, live_t.x, live_t.y + 1):
            tetris_game.add_to_landed(live_t)
            tetrominos[0] = tetris_game.generate_tetromino()
        delay_counter = move_delay

    # DEBUGGER
    text = font.render(f"x:{live_t.x} | y:{live_t.y}", True, Colours.WHITE.value)
    text_rect = text.get_rect()
    text_rect.center = (55, 45)

    board.draw()
    for t in tetrominos:
        t.draw(board.screen)
    board.draw_grid()
    tetris_game.draw_game_grid()
    board.screen.blit(text, text_rect)
    board.update()

    clock.tick(60)

pygame.quit()