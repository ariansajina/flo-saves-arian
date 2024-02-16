from typing import List

from flo.base import GameObject
from flo.constants.physics import Direction
from flo.mechanics import CanExitScreen, CanMoveHorizontally


class Flower(
    CanMoveHorizontally,
    CanExitScreen,
    GameObject,
):
    _flower_speed = 7

    def __init__(self, x: int, y: int, direction: Direction):
        super().__init__("flower.png", x, y)
        self._direction = direction

    def update(self, environment: List[GameObject]) -> None:
        self.move_right()
        self.bound()

    @property
    def speed(self) -> int:
        return self._direction.value * self._flower_speed


class Smoke(
    CanMoveHorizontally,
    CanExitScreen,
    GameObject,
):
    _speed = 6

    def __init__(self, x: int, y: int):
        super().__init__("small_smoke.png", x, y)

    def update(self, environment: List[GameObject]) -> None:
        self.move_left()
        self.bound()

    @property
    def speed(self) -> int:
        return self._speed
