from flo.graphics import flower_image
from flo.mechanics import (
    CanExitScreen,
    CanMoveHorizontally,
)
from flo.objects import GameObject
from flo.constants.physics import Direction
from flo.objects._collision import PerishWhenHitObstacle
from flo.universe import Environment


class Flower(
    GameObject,
    CanMoveHorizontally,
    CanExitScreen,
    PerishWhenHitObstacle,
):
    _flower_speed = 7

    def __init__(self, x: int, y: int, direction: Direction):
        super().__init__(flower_image.convert_alpha(), x, y)
        self._direction = direction

    def tick(self, environment: Environment) -> None:
        self.move_right()
        self.collisions(environment)
        if self.bound():
            self.perish()

    @property
    def speed(self) -> int:
        return self._direction.value * self._flower_speed
