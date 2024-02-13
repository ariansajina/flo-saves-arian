from abc import ABC, abstractmethod

from flo.base import GameObject


class CanCollide(GameObject, ABC):

    def __init__(self, image: str, x: int, y: int):
        super().__init__(image, x, y)
        self._is_on_ground = True
        self.y_velocity = 0

    def collisions(self, environment: list[GameObject]) -> None:
        for obj in environment:
            if self.rect.colliderect(obj.rect):
                self._collision_with_object(obj)

    @abstractmethod
    def _collision_with_object(self, obj: GameObject):
        raise NotImplementedError()
