import math
import random
from typing import List

import pygame
from pygame import Rect, Surface

from flo.base import GameObject, images
from flo.mechanics import CanCollide, CanMoveHorizontally, CannotExitScreen

from ._flower import Flower, Smoke


class Enemy(
    CanMoveHorizontally,
    CanCollide,
):
    _gait_speed = 2
    _flower_damage = 5
    chance_of_shooting_smoke = 0.025

    def __init__(self, x: int, y: int):
        super().__init__("evil_smoke.png", x, y)
        self._image_alive = super().image
        self._image_dead = pygame.image.load(images / "evil_smoke_dead.png").convert_alpha()

        self.health = 100
        self.is_hurt = False
        self.hurt_timer = 0
        self._x_prior_hurt = x
        self._y_prior_hurt = y
        core_width, core_height = 1, self.rect.height // 2
        self.core = Rect(
            900,
            140,
            core_width,
            core_height,
        )
        self.alive = True

    @property
    def speed(self) -> int:
        return self._gait_speed

    def update(self, environment: List[GameObject]) -> None:
        self._hurt()
        self.collisions(environment)

    def _hurt(self):
        if self.alive and self.is_hurt:
            self.rect.x += 4 * math.sin(pygame.time.get_ticks() * 0.1)
            self.hurt_timer -= 1
            if self.hurt_timer <= 0:
                self.is_hurt = False
                self.rect.x = self._x_prior_hurt
                self.rect.y = self._y_prior_hurt

    def _collision_with_object(self, obj: GameObject):
        if isinstance(obj, Flower) and self.core.colliderect(obj.rect):
            obj.kill()
            self.is_hurt = True
            self.hurt_timer = 10
            self.health -= self._flower_damage
            self._x_prior_hurt = self.rect.x
            self._y_prior_hurt = self.rect.y
            if self.health <= 0:
                self.alive = False
        else:
            pass

    @property
    def image(self) -> Surface:
        if self.alive:
            return self._image_alive
        return self._image_dead

    def shoot_smoke(self) -> Smoke:
        x, y = self.rect.x, self.rect.y
        height = random.randint(self.rect.height // 5, self.rect.height)
        return Smoke(
            x,
            y + height,
        )
