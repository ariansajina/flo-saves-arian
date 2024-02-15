import random

from pygame import Surface

from flo.constants.settings import player_layer
from flo.objects import Enemy
from ._base import LayeredUpdates, LevelBase


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

    def enemy_action(self):
        if random.uniform(0, 1) < self.enemy.chance_of_shooting_smoke:
            smoke = self.enemy.shoot_smoke()
            self.sprites.add(smoke, layer=player_layer)
