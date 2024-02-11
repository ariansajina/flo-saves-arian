from flo.constants.physics import Direction
from flo.graphics import enemy_image
from flo.mechanics import (
    CanMoveHorizontally,
    CannotExitScreen,
    CanCollide,
)
from flo.universe import GameAtom, Environment
from . import ObstacleToStandOn

from .base import GameObjectWithDirection
from ._flower import Flower


class Enemy(
    GameObjectWithDirection,
    CanMoveHorizontally,
    CannotExitScreen,
    CanCollide,
):
    _gait_speed = 2

    def __init__(self, x: int, y: int):
        super().__init__(enemy_image.convert_alpha(), x, y)
        self.health = 100

    @property
    def speed(self) -> int:
        return self._gait_speed

    def tick(self, environment: Environment) -> None:
        if self.direction is Direction.right:
            self.move_right()
        else:
            self.move_left()
        self.collisions(environment)
        self.bound()

    def _collision_with_atom(self, game_atom: GameAtom):
        match game_atom:
            case ObstacleToStandOn() as obstacle:
                self._collision_with_obstacle(obstacle)
            case Flower() as flower:
                flower.perish()
                self.health -= 25
                if self.health <= 0:
                    self.perish()
            case _:
                pass

    # TODO refactor
    def _collision_with_obstacle(self, obstacle: ObstacleToStandOn):
        # Determine the center point of the entity and the obstacle
        entity_center = self.rect.center
        obstacle_center = obstacle.rect.center

        # Calculate the difference in x and y coordinates
        dx = entity_center[0] - obstacle_center[0]
        dy = entity_center[1] - obstacle_center[1]

        # Calculate the overlap in x and y dimensions
        overlap_x = self.rect.width / 2 + obstacle.rect.width / 2 - abs(dx)
        overlap_y = self.rect.height / 2 + obstacle.rect.height / 2 - abs(dy)

        # Resolve the collision based on the minimum overlap
        if overlap_x < overlap_y:
            # Horizontal collision
            if dx > 0:
                # Entity is to the right of the obstacle, push it right
                self.rect.left = obstacle.rect.right
            else:
                # Entity is to the left of the obstacle, push it left
                self.rect.right = obstacle.rect.left
        # # Vertical collision
        elif dy > 0:
            # Entity is below the obstacle, push it down
            self.rect.top = obstacle.rect.bottom
            self.y_velocity = 0
