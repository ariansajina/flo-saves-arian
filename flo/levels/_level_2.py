from pygame import Surface

from flo.base import GameObject

from ._base import LayeredUpdates, LevelBase


class Level2(LevelBase):
    def __init__(
        self,
        sprites: LayeredUpdates,
        screen: Surface,
        flo_x: int,
        flo_y: int,
        goal: GameObject,
    ):
        super().__init__(sprites, screen, flo_x, flo_y, 655)
        self._goal = goal

    def is_level_finished(self):
        return self._goal not in self.sprites
