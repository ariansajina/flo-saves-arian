from abc import ABC, abstractmethod
from typing import Optional, Self, Collection, TypeAlias

import pygame
from pygame import Rect


class GameAtom(ABC):
    def __init__(self):
        self.y_velocity: int = 0
        self._perished: bool = False

    @property
    def is_perished(self) -> bool:
        return self._perished

    def perish(self):
        self._perished = True

    @abstractmethod
    def tick(self, environment: Collection[Self]) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def rect(self) -> Rect:
        raise NotImplementedError()


Environment: TypeAlias = list[GameAtom]


class Universe:
    def __init__(self, atoms: Optional[list[GameAtom]] = None):
        self._atoms = atoms if atoms is not None else []

    @property
    def atoms(self) -> list[GameAtom]:
        return self._atoms

    def snapshot(self) -> set[GameAtom]:
        return set(self.atoms)

    def add(self, atom: GameAtom) -> None:
        self.atoms.append(atom)

    def remove(self, atom: GameAtom) -> None:
        self.atoms.remove(atom)

    def tick(self) -> None:
        snapshot = self.snapshot()
        perished_atoms = []
        for atom in snapshot:
            other_atoms = snapshot.difference([atom] + perished_atoms)
            atom.tick(other_atoms)
            if atom.is_perished:
                perished_atoms.append(atom)
                self.remove(atom)
