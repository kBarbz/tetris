import pygame
from tetris import TetrisGame
from board import Board
from utils import Colours
from game_display import GameDisplay

# pygame setup
pygame.init()
board = Board()
clock = pygame.time.Clock()
running = True
dt = 0

tetris_game = TetrisGame(board)
tetrominos = [tetris_game.generate_tetromino()]
current_tetromino = 0

game_display = GameDisplay(board)
game_display.set_queue(tetrominos)

move_delay = 20
delay_counter = move_delay
move_y_speed = 1
move_x_speed = 1
fast_speed_multiplier = 3
collision_delay = 500  # Delay in milliseconds after collision
collision_timer = 0  # Timer to keep track of the delay

font = pygame.font.Font(None, 36)

game_over = False

while running:
    if game_over:
        break

    live_t = tetrominos[0]
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and live_t.can_go_left() and not tetris_game.check_for_collision(live_t.shape, live_t.x - 1, live_t.y):
                live_t.move(-move_x_speed, 0)
            elif event.key == pygame.K_RIGHT and live_t.can_go_right(board) and not tetris_game.check_for_collision(live_t.shape, live_t.x + 1, live_t.y):
                live_t.move(move_x_speed, 0)
            elif event.key == pygame.K_UP:  # Rotate the sprite when 'R' is pressed
                live_t.rotate_clockwise(board)
            elif event.key == pygame.K_z:  # Rotate the sprite when 'R' is pressed
                live_t.rotate_c_clockwise(board)
            elif event.key == pygame.K_SPACE:
                while not live_t.is_at_bottom(board) and not tetris_game.check_for_collision(live_t.shape, live_t.x,
                                                                                             live_t.y + 1):
                    live_t.move(0, move_y_speed)
                    collision_timer = 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        delay_counter -= move_y_speed * fast_speed_multiplier
    else:
        delay_counter -= move_y_speed

    if delay_counter <= move_y_speed:
        if not live_t.is_at_bottom(board) and not tetris_game.check_for_collision(live_t.shape, live_t.x, live_t.y + 1):
            live_t.move(0, move_y_speed)
        if collision_timer <= 0 and (live_t.is_at_bottom(board) or tetris_game.check_for_collision(live_t.shape, live_t.x, live_t.y + 1)):
            collision_timer = pygame.time.get_ticks()  # Start collision delay timer

        delay_counter = move_delay

    # Check if collision delay timer is active
    if collision_timer > 0:
        current_time = pygame.time.get_ticks()
        if current_time - collision_timer >= collision_delay:
            if live_t.is_at_bottom(board) or tetris_game.check_for_collision(live_t.shape, live_t.x, live_t.y + 1):
                tetris_game.add_to_landed(live_t)
                new_tetromino = tetris_game.generate_tetromino()
                if new_tetromino is None:
                    game_over = True
                else:
                    tetrominos[0] = new_tetromino
                collision_timer = 0  # Reset collision timer

    # DEBUGGER
    text = font.render(f"x:{live_t.x} | y:{live_t.y} | s:{tetris_game.score}", True, Colours.WHITE.value)
    text_rect = text.get_rect()
    text_rect.center = (55, 45)

    game_display.set_score(tetris_game.score)
    game_display.set_queue(tetris_game.queue)
    board.draw()
    game_display.update_display()
    for t in tetrominos:
        t.draw(board.screen)
    board.draw_grid()
    tetris_game.draw_game_grid()
    board.screen.blit(text, text_rect)
    board.update()

    clock.tick(60)

pygame.quit()