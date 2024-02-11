from pathlib import Path

import pygame

images = Path(__file__).parent.parent.parent / "katica_drawings"

flo_image = pygame.image.load(images / "floV1.png")
flo_width = flo_image.get_width()
flo_height = flo_image.get_height()

flower_image = pygame.image.load(images / "flower.png")

enemy_image = pygame.image.load(images / "enemy.png")
