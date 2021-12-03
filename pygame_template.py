import pygame
import random
from os import path

# Assets folder settings
img_dir = path.join(path.dirname(__file__), 'img')
background = pygame.image.load(path.join(img_dir, 'background.png'))
background_rect = background.get_rect()
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join('img/p1_jump.ico'))

WIDTH = 480
HEIGHT = 600
FPS = 60

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.speedx = -8
        if event.key == pygame.K_RIGHT:
            pla
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
# Game
pygame.init()   # create game and window
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game process
running = True
while running:
    # Visualisation (build)
    clock.tick(FPS)     # control process on true speed
    # Enter process (date)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # try again close this window
            running = False
    # Update
    all_sprites.update()

    # Paint
    screen.fill(GREEN)  # Render
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()  # After all

pygame.quit()
