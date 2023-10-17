# Example file showing a circle moving on screen
import pygame


class BlockSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.image = pygame.image.load('assets/images/blocks/t_block.webp')  # Set the image of the sprite
        self.rect = self.image.get_rect()  # Get the rectangular shape of the sprite

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    def rotate_right(self):
        # Rotate the sprite by 90 degrees
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect(center=self.rect.center)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

block_sprite = BlockSprite()
all_sprites = pygame.sprite.Group()
all_sprites.add(block_sprite)

# Set the initial movement speed
move_speed = 5

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Rotate the sprite when 'R' is pressed
                block_sprite.rotate_right()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Check for key presses to move the sprite
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        block_sprite.rect.x -= move_speed
    if keys[pygame.K_RIGHT]:
        block_sprite.rect.x += move_speed

    block_sprite.rect.y += move_speed

    block_mask = block_sprite.get_mask()
    if block_sprite.rect.y > screen.get_height() - block_mask.get_size()[1]:
        block_sprite.rect.y = 0  # Wrap to the top

    # Update and draw all sprites in the group
    all_sprites.update()
    all_sprites.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()