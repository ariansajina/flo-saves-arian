from abc import ABC

from pygame import Rect

from flo.base import GameObject
from flo.mechanics import CanCollide

from ._trivial import Obstacle, ObstacleToStandOn, ObstacleRight
from ..constants.physics import Direction


class CannotGoThroughObstacles(CanCollide, ABC):

    def _collision_with_object(self, obj: GameObject):
        match obj:
            case ObstacleRight() as obstacle:
                if self.direction is Direction.left:
                    self._horizontal_collision_with_obstacle(obstacle, left=False)
            case Obstacle() as obstacle:
                self._horizontal_collision_with_obstacle(obstacle)
            case _:
                pass

    def _horizontal_collision_with_obstacle(self, obstacle: Obstacle, left=True, right=True):
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
        # Vertical collision
        elif dy > 0:
            # Entity is below the obstacle, push it down
            self.rect.top = obstacle.rect.bottom
            self.y_velocity = 0
