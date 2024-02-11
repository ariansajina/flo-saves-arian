from abc import ABC

from flo.mechanics import CanCollide
from flo.objects import ObstacleToStandOn
from flo.universe import GameAtom


class CannotGoThroughObstacles(CanCollide, ABC):
    def _collision_with_atom(self, game_atom: GameAtom):
        match game_atom:
            case ObstacleToStandOn() as obstacle:
                pass
                # self._collision_with_obstacle_to_stand_on(obstacle)
            case _:
                pass

    def _collision_with_obstacle_to_stand_on(self, obstacle: ObstacleToStandOn):
        # Determine the center point of the entity and the obstacle
        entity_center = self.rect.center
        obstacle_center = obstacle.rect.center

        dy = entity_center[1] - obstacle_center[1]

        # Vertical collision
        if dy > 0:
            # Entity is below the obstacle, push it down
            self.rect.top = obstacle.rect.bottom
            self.y_velocity = 0

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


class PerishWhenHitObstacle(CanCollide, ABC):
    def _collision_with_atom(self, game_atom: GameAtom):
        match game_atom:
            case ObstacleToStandOn():
                self.perish()
            case _:
                pass
