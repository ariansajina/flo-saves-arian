from abc import ABC, abstractmethod

from flo.universe import GameAtom, Environment


class CanCollide(GameAtom, ABC):

    def collisions(self, environment: Environment) -> None:
        for game_atom in environment:
            if self.rect.colliderect(game_atom):
                self._collision_with_atom(game_atom)

    @abstractmethod
    def _collision_with_atom(self, game_atom: GameAtom):
        raise NotImplementedError()
