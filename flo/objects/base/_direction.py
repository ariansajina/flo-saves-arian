from abc import ABC

import pygame
from pygame import Surface

from flo.objects.base import GameObject
from flo.constants.physics import Direction


class GameObjectWithDirection(GameObject, ABC):
    def __init__(self, image: Surface, x: int, y: int):
        super().__init__(image, x, y)
        self._sprite_right = self._image
        self._sprite_left = pygame.transform.flip(self._image, True, False)
        self.direction: Direction = Direction.right

    @property
    def image(self) -> Surface:
        return (
            self._sprite_right
            if self.direction is Direction.right
            else self._sprite_left
        )

    def turn_right(self):
        self.direction = Direction.right

    def turn_left(self):
        self.direction = Direction.left
