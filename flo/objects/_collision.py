from abc import ABC

from pygame import Rect

from flo.base import GameObject
from flo.constants.settings import floor_pad, table_height
from flo.mechanics import CanCollide

from ._trivial import Obstacle, ObstacleToStandOn


class CannotGoThroughObstacles(CanCollide, ABC):

    chair_monitor = Rect(585, 800 - 200 - table_height + floor_pad + 5, 230, 1)

    def _collision_with_object(self, obj: GameObject):
        match obj:
            case Obstacle() | ObstacleToStandOn() as obstacle:
                if self._is_on_the_chair():
                    self._horizontal_collision_with_obstacle(obstacle)
            case _:
                pass

    def _is_on_the_chair(self):
        return self.rect.colliderect(self.chair_monitor)

    def _horizontal_collision_with_obstacle(self, obstacle: Obstacle):
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
