from abc import ABC, abstractmethod
from typing import List

from flo.base import GameObject
from flo.constants.physics import GRAVITY, JUMP_HEIGHT


class CanJump(GameObject, ABC):
    def __init__(self, image: str, x: int, y: int):
        super().__init__(image, x, y)
        self._is_on_ground = True
        self.y_velocity = 0

    def jump(self):
        if self._is_on_ground:
            self.y_velocity = JUMP_HEIGHT
            self._is_on_ground = False

    def fall(self, environment: List[GameObject]):
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
        if self.rect.top >= self.floor:
            self.rect.top = self.floor
            self._stand()

    @abstractmethod
    def is_standing_on(self, obj: GameObject) -> bool:
        raise NotImplementedError()

    @property
    @abstractmethod
    def floor(self) -> int:
        raise NotImplementedError()

    def _stand(self) -> None:
        self._is_on_ground = True
        self.y_velocity = 0
