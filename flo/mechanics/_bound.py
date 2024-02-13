from abc import ABC, abstractmethod

from flo.base import GameObject
from flo.constants.settings import screen_height, screen_width


class Bound(GameObject, ABC):
    @abstractmethod
    def bound(self) -> None:
        raise NotImplementedError()


class CannotExitScreen(Bound, ABC):
    """Cannot leave the boundaries of the screen."""

    def bound(self) -> None:
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top > screen_height - self.rect.height:
            self.rect.top = 0
        if self.rect.right < self.rect.width:
            self.rect.right = self.rect.width
        if self.rect.top < 0:
            self.rect.top = screen_height - self.rect.height


class CanExitScreen(Bound, ABC):
    """Can leave the boundaries of the screen."""

    def bound(self) -> None:
        if (
            self.rect.right > screen_width
            or self.rect.top > screen_height - self.rect.height
            or self.rect.right < self.rect.width
            or self.rect.top < 0
        ):
            self.kill()
