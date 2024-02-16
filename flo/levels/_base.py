from abc import ABC, abstractmethod

import pygame
from pygame import Surface

from flo.constants.settings import fps, player_layer
from flo.objects import Enemy, Flo, Obstacle, ObstacleRight, ObstacleToStandOn


class LayeredUpdates(pygame.sprite.LayeredUpdates):
    def update(self):
        sprites = set(self.sprites())
        for _sprite in self.sprites():
            other_sprites = sprites.difference([_sprite])
            _sprite.update(other_sprites)


class LevelBase(ABC):
    _is_development = False

    def __init__(
        self,
        sprites: LayeredUpdates,
        screen: Surface,
        flo_x: int,
        flo_y: int,
        floor: int,
    ):
        self.sprites = sprites
        self._screen = screen

        self.floor = floor
        self.flo = Flo(flo_x, flo_y, self.floor)
        self.sprites.add(self.flo, layer=player_layer)
        self._clock = pygame.time.Clock()

    def run(self):
        running = True
        space_pressed_last_frame = True
        show_instructions = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.flo.turn_left()
                self.flo.move_left()
                show_instructions = False
            elif keys[pygame.K_RIGHT]:
                self.flo.turn_right()
                self.flo.move_right()
                show_instructions = False

            if keys[pygame.K_UP]:
                self.flo.jump()
                show_instructions = False

            space_currently_pressed = keys[pygame.K_SPACE]
            if space_currently_pressed and not space_pressed_last_frame:
                flower = self.flo.shoot_flower()
                self.sprites.add(flower, layer=player_layer)
                show_instructions = False
            space_pressed_last_frame = space_currently_pressed

            self.enemy_action()

            self.sprites.update()

            self.sprites.draw(self._screen)

            if show_instructions:
                font = pygame.font.Font(None, 26)
                instructions, ix, iy = self.get_instructions_and_xy()
                text_surface = font.render(instructions, True, (200, 200, 200))
                self._screen.blit(text_surface, (ix, iy))

            if self._is_development:
                font = pygame.font.Font(None, 32)
                text_surface = font.render(
                    f"use the arrow keys to move", True, (255, 255, 255)
                )
                self._screen.blit(text_surface, (10, 10))
                for sprite in self.sprites.sprites():
                    if isinstance(sprite, (Obstacle, ObstacleToStandOn, ObstacleRight)):
                        pygame.draw.rect(
                            self._screen,
                            (0, 255, 0),
                            sprite.rect,
                        )
                    if isinstance(sprite, Enemy):
                        pygame.draw.rect(
                            self._screen,
                            (0, 255, 0),
                            sprite.core,
                        )

            pygame.display.flip()
            self._clock.tick(fps)

            if self.is_level_finished():
                running = False

        # self.sprites.empty()

    @abstractmethod
    def is_level_finished(self):
        raise NotImplementedError()

    @abstractmethod
    def enemy_action(self):
        raise NotImplementedError()

    @abstractmethod
    def get_instructions_and_xy(self):
        raise NotImplementedError()
