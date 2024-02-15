import math

import pygame
from pygame import Rect

from flo.base import GameObject
from flo.mechanics import CanCollide, CanMoveHorizontally, CannotExitScreen

from ._flower import Flower


class Enemy(
    CanMoveHorizontally,
    CanCollide,
):
    _gait_speed = 2
    _flower_damage = 20

    def __init__(self, x: int, y: int):
        super().__init__("evil_smoke.png", x, y)
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

    def update(self, environment: list[GameObject]) -> None:
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
        match obj:
            case Flower() as flower:
                if self.core.colliderect(flower.rect):
                    flower.kill()

                    self.is_hurt = True
                    self.hurt_timer = 10
                    self.health -= self._flower_damage
                    self._x_prior_hurt = self.rect.x
                    self._y_prior_hurt = self.rect.y

                    if self.health <= 0:
                        self.alive = False
            case _:
                pass
