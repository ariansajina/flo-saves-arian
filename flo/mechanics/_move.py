from abc import ABC, abstractmethod

from flo.base import GameObject


class CanMoveHorizontally(GameObject, ABC):
    @property
    @abstractmethod
    def speed(self) -> int:
        raise NotImplementedError()

    def move_left(self):
        self.rect.right -= self.speed

    def move_right(self):
        self.rect.right += self.speed
