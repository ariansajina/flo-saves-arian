from abc import ABC

from pygame import Surface

from flo.universe import GameAtom


class GameObject(GameAtom, ABC):
    def __init__(self, image: Surface, x: int, y: int):
        super().__init__()
        self._image = image
        self._rect = image.get_rect()
        self._rect.x = x
        self._rect.y = y

    @property
    def rect(self):
        return self._rect

    @property
    def xy(self):
        return self.rect.x, self.rect.y

    @property
    def image(self) -> Surface:
        return self._image
