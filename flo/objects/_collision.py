from abc import ABC

from flo.base import GameObject
from flo.constants.physics import Direction
from flo.mechanics import CanCollide

from ._trivial import Obstacle, ObstacleRight


class CannotGoThroughObstacles(CanCollide, ABC):
    def _collision_with_object(self, obj: GameObject):
        if isinstance(obj, ObstacleRight):
            if self.direction is Direction.left:
                self._horizontal_collision_with_obstacle(obj, left=False)
        elif isinstance(obj, Obstacle):
            self._horizontal_collision_with_obstacle(obj)
        else:
            pass

    def _horizontal_collision_with_obstacle(
        self, obstacle: Obstacle, left=True, right=True
    ):
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
            if dx > 0 and right:
                # Entity is to the right of the obstacle, push it right
                self.rect.left = obstacle.rect.right
            elif dx < 0 and left:
                # Entity is to the left of the obstacle, push it left
                self.rect.right = obstacle.rect.left
