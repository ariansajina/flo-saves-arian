from typing import Collection, Self

from flo.graphics import flo_image
from flo.mechanics import (
    CanJump,
    CanMoveHorizontally,
    CannotExitScreen,
)
from flo.constants.physics import Direction
from ._collision import CannotGoThroughObstacles

from ._flower import Flower
from .base import GameObjectWithDirection
from ..universe import Environment


class Flo(
    GameObjectWithDirection,
    CanMoveHorizontally,
    CannotExitScreen,
    CanJump,
    CannotGoThroughObstacles,
):
    _gait_speed = 5

    def __init__(self, x: int, y: int):
        super().__init__(flo_image.convert_alpha(), x, y)

    def tick(self, environment: Environment) -> None:
        self.collisions(environment)
        self.fall(environment)
        _ = self.bound()

    @property
    def speed(self) -> int:
        return self._gait_speed

    def shoot_flower(self) -> Flower:
        x, y = self.xy
        return Flower(
            x + (self.rect.width if self.direction is Direction.right else 0),
            y + (self.rect.height // 2),
            self.direction,
        )
