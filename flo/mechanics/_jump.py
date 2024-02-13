from abc import ABC, abstractmethod

from flo.base import GameObject
from flo.constants.physics import GRAVITY, JUMP_HEIGHT
from flo.constants.settings import floor_pad, screen_height, table_height


class CanJump(GameObject, ABC):

    def __init__(self, image: str, x: int, y: int):
        super().__init__(image, x, y)
        self._is_on_ground = True
        self.y_velocity = 0

    def jump(self):
        if self._is_on_ground:
            self.y_velocity = JUMP_HEIGHT
            self._is_on_ground = False

    def fall(self, environment: list[GameObject]):
        if not self._is_on_ground:
            self.rect.top += self.y_velocity
            self.y_velocity += GRAVITY

        # Assume not on ground until collision detected
        self._is_on_ground = False

        # Check for ground or obstacle beneath
        for obj in environment:
            if self.is_standing_on(obj):
                self.rect.bottom = obj.rect.top
                self._stand()

        # Check for reaching the bottom of the screen
        floor = screen_height - self.rect.height - table_height + floor_pad
        if self.rect.top >= floor:
            self.rect.top = floor
            self._stand()

    @abstractmethod
    def is_standing_on(self, obj: GameObject) -> bool:
        raise NotImplementedError()

    def _stand(self) -> None:
        self._is_on_ground = True
        self.y_velocity = 0
