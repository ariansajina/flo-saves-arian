from flo.base import GameObject
from flo.constants.physics import Direction
from flo.mechanics import CanJump, CanMoveHorizontally, CannotExitScreen

from ._collision import CannotGoThroughObstacles
from ._flower import Flower
from ._trivial import ObstacleToStandOn


class Flo(
    CanMoveHorizontally,
    CannotExitScreen,
    CanJump,
    CannotGoThroughObstacles,
):
    _gait_speed = 5

    def __init__(self, x: int, y: int, floor: int):
        super().__init__("flo.png", x, y)
        self._floor = floor

    def update(self, environment: list[GameObject]) -> None:
        self.collisions(environment)
        self.fall(environment)
        self.bound()

    @property
    def floor(self) -> int:
        return self._floor

    @property
    def speed(self) -> int:
        return self._gait_speed

    def shoot_flower(self) -> Flower:
        x, y = self.rect.x, self.rect.y
        return Flower(
            x + (self.rect.width if self.direction is Direction.right else 0),
            y + (self.rect.height // 2),
            self.direction,
        )

    def is_standing_on(self, obj: GameObject) -> bool:
        return (
            isinstance(obj, ObstacleToStandOn)
            and self.rect.colliderect(obj.rect)
            and self.rect.bottom <= obj.rect.top + self.y_velocity
        )
