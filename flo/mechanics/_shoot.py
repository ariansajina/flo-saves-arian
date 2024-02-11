from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from flo.universe import GameAtom
from flo.constants.physics import Direction

T = TypeVar("T", bound=GameAtom)


class CanShoot(GameAtom, Generic[T], ABC):

    def shoot(self, direction: Direction) -> T:
        return self._make_shot(direction)

    @abstractmethod
    def _make_shot(self, direction: Direction) -> T:
        raise NotImplementedError()
