from abc import ABC, abstractmethod

from flo.universe import GameAtom


class CanMoveHorizontally(GameAtom, ABC):

    def __init__(self):
        super().__init__()
        self._animation_counter = 0

    @property
    @abstractmethod
    def speed(self) -> int:
        raise NotImplementedError()

    def move_left(self):
        self.rect.right -= self.speed
        self._animation_counter += 1

    def move_right(self):
        self.rect.right += self.speed
        self._animation_counter += 1
