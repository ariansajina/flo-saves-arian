from abc import ABC, abstractmethod

import pygame
from pygame import Surface

from flo.constants.settings import fps, player_layer
from flo.levels import LayeredUpdates
from flo.objects import Arian, Enemy, Flo


class AnimationBase(ABC):
    def __init__(self, sprites: LayeredUpdates, screen: Surface):
        self.sprites = sprites
        self._screen = screen
        self._clock = pygame.time.Clock()

    def run(self):
        running = True

        while running:
            self.animate()
            self.sprites.update()
            self.sprites.draw(self._screen)
            pygame.display.flip()
            self._clock.tick(fps)

            if self.is_finished():
                running = False

    @abstractmethod
    def animate(self) -> None:
        pass

    @abstractmethod
    def is_finished(self) -> bool:
        pass


class AnimationEvilSmokeDies(AnimationBase):
    def __init__(self, sprites: LayeredUpdates, screen: Surface, evil_smoke: Enemy):
        super().__init__(sprites, screen)
        self.evil_smoke = evil_smoke

    def animate(self) -> None:
        self.evil_smoke.rect.bottom -= 3

    def is_finished(self) -> bool:
        return self.evil_smoke.rect.bottom < 0


class AnimationFloComesDown(AnimationBase):
    def __init__(self, sprites: LayeredUpdates, screen: Surface, flo: Flo):
        super().__init__(sprites, screen)
        self.flo = flo

    def animate(self) -> None:
        self.flo.turn_right()
        self.flo.move_right()

    def is_finished(self) -> bool:
        return self.flo.rect.top >= self.flo.floor


class AnimationArianComesIn(AnimationBase):
    def __init__(self, sprites: LayeredUpdates, screen: Surface, flo: Flo):
        super().__init__(sprites, screen)
        self.flo = flo
        self.arian = Arian(1200, flo.floor)
        self.sprites.add(self.arian, layer=player_layer)

    def animate(self) -> None:
        self.arian.move_left()

    def is_finished(self) -> bool:
        return self.arian.rect.colliderect(self.flo.rect)
