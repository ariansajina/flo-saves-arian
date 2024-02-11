from abc import ABC

from pygame import Rect

from flo.universe import GameAtom, Environment
from flo.constants.physics import GRAVITY, JUMP_HEIGHT
from flo.constants.settings import screen_height, table_height


class CanJump(GameAtom, ABC):

    def __init__(self):
        super().__init__()
        self._is_on_ground = True

    def jump(self):
        if self._is_on_ground:
            self.y_velocity = JUMP_HEIGHT
            self._is_on_ground = False

    def fall(self, environment: Environment):
        if not self._is_on_ground:
            self.rect.top += self.y_velocity
            self.y_velocity += GRAVITY

        # Assume not on ground until collision detected
        self._is_on_ground = False

        # Check for ground or obstacle beneath
        for obj in environment:
            if self._is_standing_on(obj.rect):
                self.rect.bottom = obj.rect.top
                self._stand()

        # Check for reaching the bottom of the screen
        if self.rect.top >= screen_height - self.rect.height - table_height:
            self.rect.top = screen_height - self.rect.height - table_height
            self._stand()

    def _is_standing_on(self, rect: Rect) -> bool:
        return (
            self.rect.colliderect(rect)
            and self.rect.bottom <= rect.top + self.y_velocity
        )

    def _stand(self) -> None:
        self._is_on_ground = True
        self.y_velocity = 0
