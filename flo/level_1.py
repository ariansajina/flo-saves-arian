import sys
from pathlib import Path

import pygame

from flo.graphics import flo_height, flo_width
from flo.objects import Enemy, Flo, ObstacleToStandOn
from flo.universe import Universe
from flo.constants.colors import white
from flo.constants.settings import screen_height, screen_width, table_height

images = Path(__file__).parent.parent / "katica_drawings"

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))


background = [
    pygame.image.load(images / "background.png").convert_alpha(),
    # pygame.image.load(images / "pineapple.png").convert_alpha(),
]

foreground = [
    pygame.image.load(images / "beers-ashtrays.png").convert_alpha(),
    pygame.image.load(images / "vase.png").convert_alpha(),
    pygame.image.load(images / "lamp.png").convert_alpha(),
]

table = pygame.image.load(images / "table.png").convert_alpha()

chair_img = pygame.image.load(images / "chair.png").convert_alpha()
# chair_mask = pygame.mask.from_surface(chair_img)
chair = ObstacleToStandOn(chair_img, 550, screen_height - chair_img.get_height() - table_height)

bottle_img = pygame.image.load(images / "bottle.png").convert_alpha()
bottle = ObstacleToStandOn(bottle_img, 300, screen_height - bottle_img.get_height() - table_height)

empty_glass_img = pygame.image.load(images / "empty-glass.png").convert_alpha()
empty_glass = ObstacleToStandOn(empty_glass_img, 870, screen_height - empty_glass_img.get_height() - table_height)

pineapple_image = pygame.image.load(images / "pineapple.png").convert_alpha()
pineapple = ObstacleToStandOn(pineapple_image, 1060, screen_height - pineapple_image.get_height() - 488)


font = pygame.font.Font(None, 36)

# Game title
pygame.display.set_caption("Flo saves Aki")

# Set up game clock
clock = pygame.time.Clock()
fps = 60

# Character initial placement
girl_x = 100
girl_y = screen_height - flo_height - table_height

flo = Flo(
    girl_x,
    girl_y,
)

obstacles = [
    chair,
    bottle,
    empty_glass,
    pineapple,
]

# enemy = Enemy(500, girl_y)


universe = Universe([flo] + obstacles)

running = True
space_pressed_last_frame = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        flo.turn_left()
        flo.move_left()
    elif keys[pygame.K_RIGHT]:
        flo.turn_right()
        flo.move_right()

    if keys[pygame.K_UP]:
        flo.jump()

    space_currently_pressed = keys[pygame.K_SPACE]
    if space_currently_pressed and not space_pressed_last_frame:
        flower = flo.shoot_flower()
        universe.add(flower)
    space_pressed_last_frame = space_currently_pressed

    universe.tick()

    # Draw everything
    for b in background:
        screen.blit(b, (0, 0))

    screen.blit(table, (0, screen_height - table.get_height()))

    # debug - remove later
    text_surface = font.render(f"# objects: {len(universe.atoms)}", True, white)
    screen.blit(text_surface, (10, 10))

    for o in universe.atoms:
        screen.blit(o.image, o.rect)  # TODO

    screen.blit(flo.image, flo.rect)

    for f in foreground:
        screen.blit(f, (0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

pygame.quit()
sys.exit()
