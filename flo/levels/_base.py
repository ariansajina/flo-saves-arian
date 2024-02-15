from abc import ABC, abstractmethod

import pygame
from pygame import Surface

from flo.constants.settings import fps, player_layer
from flo.objects import Flo, Obstacle, ObstacleRight, ObstacleToStandOn


class LayeredUpdates(pygame.sprite.LayeredUpdates):
    def update(self, *args, **kwargs):
        sprites = set(self.sprites())
        for _sprite in self.sprites():
            other_sprites = sprites.difference([_sprite])
            _sprite.update(other_sprites)


class LevelBase(ABC):
    _is_development = True

    def __init__(
        self, sprites: LayeredUpdates, screen: Surface, flo_x: int, flo_y: int, floor: int
    ):
        self.sprites = sprites
        self._screen = screen

        self.flo = Flo(flo_x, flo_y, floor)
        self.sprites.add(self.flo, layer=player_layer)
        self._clock = pygame.time.Clock()

    def run(self):
        running = True
        space_pressed_last_frame = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.flo.turn_left()
                self.flo.move_left()
            elif keys[pygame.K_RIGHT]:
                self.flo.turn_right()
                self.flo.move_right()

            if keys[pygame.K_UP]:
                self.flo.jump()

            space_currently_pressed = keys[pygame.K_SPACE]
            if space_currently_pressed and not space_pressed_last_frame:
                flower = self.flo.shoot_flower()
                self.sprites.add(flower, layer=player_layer)
            space_pressed_last_frame = space_currently_pressed

            self.sprites.update()

            self.sprites.draw(self._screen)

            if self._is_development:
                font = pygame.font.Font(None, 36)
                text_surface = font.render(
                    f"# objects: {len(self.sprites.sprites())}", True, (255, 255, 255)
                )
                self._screen.blit(text_surface, (10, 10))
                for sprite in self.sprites.sprites():
                    if isinstance(sprite, (Obstacle, ObstacleToStandOn, ObstacleRight)):
                        pygame.draw.rect(
                            self._screen,
                            (0, 255, 0),
                            sprite.rect,
                        )

            pygame.display.flip()
            self._clock.tick(fps)

            if self.is_level_finished():
                running = False

        self.sprites.empty()

    @abstractmethod
    def is_level_finished(self, *args, **kwargs):
        raise NotImplementedError()
