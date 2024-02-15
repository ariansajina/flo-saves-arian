from pygame import Surface

from flo.base import GameObject

from ._base import LayeredUpdates, LevelBase
from ..constants.settings import player_layer
from ..objects import Enemy


class Level2(LevelBase):
    def __init__(
        self,
        sprites: LayeredUpdates,
        screen: Surface,
        flo_x: int,
        flo_y: int,
    ):
        super().__init__(sprites, screen, flo_x, flo_y, 655)
        self.enemy = Enemy(700, 0)
        self.sprites.add(self.enemy, layer=player_layer)

    def is_level_finished(self):
        return not self.enemy.alive
