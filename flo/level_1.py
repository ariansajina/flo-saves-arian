import sys
from pathlib import Path

import pygame

from flo.constants.colors import white
from flo.constants.settings import (floor_pad, screen_height, screen_width,
                                    table_height)
from flo.graphics import flo_height
from flo.objects import Flo, Obstacle, ObstacleToStandOn, Scenery

images = Path(__file__).parent.parent / "images"

DEVELOPMENT = True

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))


background = Scenery("background.png")

foreground_sprites = [
    Scenery("beers-ashtrays.png"),
    Scenery("vase.png"),
    Scenery("lamp.png"),
]

table = Scenery("table.png", 0, screen_height - table_height)

chair_img = pygame.image.load(images / "chair.png").convert_alpha()
# chair_mask = pygame.mask.from_surface(chair_img)
chair = Scenery(
    "chair.png", 550, screen_height - chair_img.get_height() - table_height + floor_pad
)
chair_mask_1 = ObstacleToStandOn(
    "mask-25x1.png",
    552,
    screen_height - chair_img.get_height() - table_height + floor_pad + 5,
)
chair_mask_2 = ObstacleToStandOn(
    "mask-230x1.png",
    585,
    screen_height - chair_img.get_height() - table_height + floor_pad + 35,
)
chair_mask_3 = ObstacleToStandOn(
    "mask-25x1.png",
    823,
    screen_height - chair_img.get_height() - table_height + floor_pad + 5,
)
chair_mask_4 = Obstacle(
    "mask-230x1.png",
    585,
    800 - 200 - table_height + floor_pad + 5,
)


bottle_img = pygame.image.load(images / "bottle.png").convert_alpha()
bottle = Scenery(
    "bottle.png",
    300,
    screen_height - bottle_img.get_height() - table_height + floor_pad,
)
bottle_mask_1 = ObstacleToStandOn(
    "mask-230x1.png", 310, screen_height - 100 - table_height + floor_pad
)
bottle_mask_2 = ObstacleToStandOn(
    "mask-90x1.png", 560, screen_height - 45 - table_height + floor_pad
)

pineapple_image = pygame.image.load(images / "pineapple.png").convert_alpha()
pineapple = Scenery(
    "pineapple.png", 1060, screen_height - pineapple_image.get_height() - 488
)


font = pygame.font.Font(None, 36)

# Game title
pygame.display.set_caption("Flo saves Aki")

# Set up game clock
clock = pygame.time.Clock()
fps = 60

# Character initial placement
girl_x = 100
girl_y = screen_height - flo_height - table_height + floor_pad

flo = Flo(
    girl_x,
    girl_y,
)


class LayeredUpdates(pygame.sprite.LayeredUpdates):
    def update(self, *args, **kwargs):
        sprites = set(self.sprites())
        for _sprite in self.sprites():
            other_sprites = sprites.difference([_sprite])
            _sprite.update(other_sprites)


all_sprites = LayeredUpdates()

all_sprites.add(background, layer=0)
all_sprites.add(
    [
        table,
        chair,
        chair_mask_1,
        chair_mask_2,
        chair_mask_3,
        chair_mask_4,
        bottle,
        bottle_mask_1,
        bottle_mask_2,
        trombone_placeholder,
        pineapple,
    ],
    layer=1,
)
all_sprites.add(flo, layer=2)
all_sprites.add(foreground_sprites, layer=3)


# start_image = pygame.image.load(images / "pineapple.png").convert_alpha()


# def show_start_image():
#     screen.blit(start_image, (0, 0))  # Draw the image on the screen
#     pygame.display.flip()  # Update the display
#
#     # Wait for the player to press space
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     waiting = False
#
#
# show_start_image()

# add animation to transition to level


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
        all_sprites.add([flower], layer=1)
    space_pressed_last_frame = space_currently_pressed

    all_sprites.update()

    all_sprites.draw(screen)

    if DEVELOPMENT:
        text_surface = font.render(
            f"# objects: {len(all_sprites.sprites())}", True, white
        )
        screen.blit(text_surface, (10, 10))
        for sprite in all_sprites.sprites():
            if isinstance(sprite, (Obstacle, ObstacleToStandOn)):
                pygame.draw.rect(
                    screen,
                    (0, 255, 0),
                    sprite.rect,
                )

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

pygame.quit()
sys.exit()
