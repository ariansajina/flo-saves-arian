from flo.base import GameObject


class TrivialGameObject(GameObject):
    def update(self, environment: list[GameObject]):
        return


class Scenery(TrivialGameObject):
    pass


class ObstacleToStandOn(TrivialGameObject):
    pass


class Obstacle(TrivialGameObject):
    pass


class ObstacleRight(TrivialGameObject):
    pass
