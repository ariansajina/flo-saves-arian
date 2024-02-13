from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, Self

import pygame.sprite
from pygame import Mask, Rect, Surface

from flo.constants.physics import Direction

images = Path(__file__).parent.parent / "images"


class GameObject(pygame.sprite.Sprite, ABC):
    def __init__(self, image: str, x: Optional[int] = 0, y: Optional[int] = 0):
        super().__init__()
        self._image = pygame.image.load(images / image).convert_alpha()
        self._mask = pygame.mask.from_surface(self._image)
        self._rect = self._image.get_rect()
        self._rect.x = x
        self._rect.y = y

    @property
    def rect(self) -> Rect:
        return self._rect

    @property
    def image(self) -> Surface:
        return self._image

    @property
    def mask(self) -> Mask:
        return self._mask

    @abstractmethod
    def update(self, environment: list[Self]):
        raise NotImplementedError()


class GameObjectWithDirection(GameObject, ABC):
    def __init__(self, image: str, x: int, y: int):
        super().__init__(image, x, y)
        self._image_facing_right = self._image
        self._image_facing_left = pygame.transform.flip(self._image, True, False)
        self.direction: Direction = Direction.right

    @property
    def image(self) -> Surface:
        return (
            self._image_facing_right
            if self.direction is Direction.right
            else self._image_facing_left
        )

    def turn_right(self):
        self.direction = Direction.right

    def turn_left(self):
        self.direction = Direction.left
