import sys
import time
from pathlib import Path

import pygame

from flo.constants.settings import (
    background_layer,
    floor_pad,
    foreground_layer,
    object_layer,
    screen_height,
    screen_width,
    table_height,
)
from flo.levels import LayeredUpdates, Level1, Level2, show_static_image
from flo.levels._animation import (
    AnimationArianComesIn,
    AnimationEvilSmokeDies,
    AnimationFloComesDown,
)
from flo.objects import Obstacle, ObstacleRight, ObstacleToStandOn, Scenery

images = Path(__file__).parent.parent / "images"


# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))

# Game title
pygame.display.set_caption("Flo saves Arian")

# region: set up sprites for level 1

background_1 = Scenery("background_1.png")

foreground_1 = [
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
    "masks/mask-15x1.png",
    560,
    screen_height - chair_img.get_height() - table_height + floor_pad + 5,
)
chair_mask_2 = ObstacleToStandOn(
    "masks/mask-230x1.png",
    590,
    screen_height - chair_img.get_height() - table_height + floor_pad + 35,
)
chair_mask_3 = ObstacleToStandOn(
    "masks/mask-15x1.png",
    827,
    screen_height - chair_img.get_height() - table_height + floor_pad + 5,
)
chair_mask_4 = ObstacleRight(
    "masks/mask-1x5.png",
    570,
    510,
)
chair_mask_5 = Obstacle(
    "masks/mask-1x5.png",
    825,
    514,
)


bottle_img = pygame.image.load(images / "bottle.png").convert_alpha()
bottle = Scenery(
    "bottle.png",
    300,
    screen_height - bottle_img.get_height() - table_height + floor_pad,
)
bottle_mask_1 = ObstacleToStandOn(
    "masks/mask-230x1.png", 310, screen_height - 90 - table_height + floor_pad
)
bottle_mask_2 = ObstacleToStandOn(
    "masks/mask-90x1.png", 560, screen_height - 45 - table_height + floor_pad
)

coat_hanger = Scenery("coat_hanger.png", 850, 395)
coat_hanger_mask = ObstacleToStandOn("masks/mask-260x1.png", 860, 410)

shelf = Scenery("shelf.png", 1000, 283)
shelf_mask = ObstacleToStandOn("masks/mask-230x1.png", 1005, 295)

pineapple_image = pygame.image.load(images / "pineapple.png").convert_alpha()
pineapple = Scenery(
    "pineapple.png", 1060, screen_height - pineapple_image.get_height() - 498
)
pineapple_mask = Scenery("masks/mask-70x80.png", 1080, 210)

level_1_sprites = LayeredUpdates()

level_1_sprites.add(background_1, layer=background_layer)
level_1_sprites.add(
    [
        table,
        chair,
        chair_mask_1,
        chair_mask_2,
        chair_mask_3,
        chair_mask_4,
        chair_mask_5,
        bottle,
        bottle_mask_1,
        bottle_mask_2,
        coat_hanger,
        coat_hanger_mask,
        shelf,
        shelf_mask,
        pineapple,
        pineapple_mask,
    ],
    layer=object_layer,
)
level_1_sprites.add(foreground_1, layer=foreground_layer)

# endregion

# region: set up sprites for level 2

background_2 = Scenery("background_2.jpg")

foreground_2 = Scenery("pineapple_cube.png", 500, 600)

vertical_bar_1 = Obstacle("masks/mask-1x800.png", 50, 0)
vertical_bar_2 = Obstacle("masks/mask-1x800.png", 870, 0)

line_1 = ObstacleToStandOn("masks/mask-70x1.png", 217, 615)
line_2 = ObstacleToStandOn("masks/mask-70x1.png", 322, 512)
line_3 = ObstacleToStandOn("masks/mask-50x1.png", 430, 409)
line_4 = ObstacleToStandOn("masks/mask-90x1.png", 518, 610)
line_5 = ObstacleToStandOn("masks/mask-90x1.png", 620, 630)
line_6 = ObstacleToStandOn("masks/mask-25x1.png", 710, 640)
line_7 = ObstacleToStandOn("masks/mask-70x1.png", 614, 518)

level_2_sprites = LayeredUpdates()

level_2_sprites.add(background_2, layer=background_layer)
level_2_sprites.add(
    [
        vertical_bar_1,
        vertical_bar_2,
        line_1,
        line_2,
        line_3,
        line_4,
        line_5,
        line_6,
        line_7,
    ],
    layer=object_layer,
)
# level_2_sprites.add(foreground_2, layer=foreground_layer)

# endregion


tiramisu = pygame.image.load(images / "tiramisu.jpg").convert_alpha()
senor_p = pygame.image.load(images / "senor_p.jpg").convert_alpha()
yay = pygame.image.load(images / "yay.jpg").convert_alpha()


level_1 = Level1(
    level_1_sprites,
    screen,
    100,
    screen_height - 60 - table_height + floor_pad,
    pineapple_mask,
)

level_2 = Level2(level_2_sprites, screen, 100, 900)

# region: order of game elements

# show_static_image(tiramisu, screen)

level_1.run()

show_static_image(senor_p, screen)

level_2.run()
#
# animation_1 = AnimationEvilSmokeDies(level_2_sprites, screen, level_2.enemy)
# animation_1.run()
#
# animation_2 = AnimationFloComesDown(level_2_sprites, screen, level_2.flo)
# animation_2.run()
#
#
# animation_3 = AnimationArianComesIn(level_2_sprites, screen, level_2.flo)
# animation_3.run()
#
# time.sleep(1)
#
# show_static_image(yay, screen, is_last=True)

# endregion

pygame.quit()
sys.exit()
