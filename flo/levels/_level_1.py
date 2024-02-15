from pygame import Surface

from flo.base import GameObject

from ._base import LayeredUpdates, LevelBase


class Level1(LevelBase):
    def __init__(
        self,
        sprites: LayeredUpdates,
        screen: Surface,
        flo_x: int,
        flo_y: int,
        goal: GameObject,
    ):
        super().__init__(sprites, screen, flo_x, flo_y, 640)
        self._goal = goal

    def is_level_finished(self):
        return self.flo.rect.colliderect(self._goal.rect)
