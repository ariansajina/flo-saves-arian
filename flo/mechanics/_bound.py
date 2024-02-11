from abc import ABC, abstractmethod

from flo.universe import GameAtom
from flo.constants.settings import screen_height, screen_width


class CannotExitScreen(GameAtom, ABC):
    """Cannot leave the boundaries of the screen."""

    def bound(self) -> bool:
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top > screen_height - self.rect.height:
            self.rect.top = 0
        if self.rect.right < self.rect.width:
            self.rect.right = self.rect.width
        if self.rect.top < 0:
            self.rect.top = screen_height - self.rect.height
        return False


class CanExitScreen(GameAtom, ABC):
    """Can leave the boundaries of the screen."""

    def bound(self) -> bool:
        if (
            self.rect.right > screen_width
            or self.rect.top > screen_height - self.rect.height
            or self.rect.right < self.rect.width
            or self.rect.top < 0
        ):
            return True
        return False
