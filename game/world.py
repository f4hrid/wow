from game.config import GRAVITY
from game.player import Player


class World:
    """ Creación del pseudo mundo. """

    def __init__(self):
        """ Constructor: """

        self.floor = 555
        self.gravity = GRAVITY
        self.mass = 3

        self.player: Player = Player()


    def update(self):
        """ Actualizar los objetos del mundo. """

        self.player.update()

        self.__apply_gravity(self.player)
        self.__ground_level(self.player)


    def draw(self):
        """ Componentes para dibujar el mundo. """
        return None


    def __ground_level(self, obj: Player):
        """ Fija el nivel del suelo para todos los objetos del mundo. """

        # mientras no este en el aire
        if obj.position.bottom < self.floor:
            return
        # establece la altura del mundo
        obj.position.bottom = self.floor
        # reestablece la velocidad delta del objeto
        obj.dy = 0
        # verifica si el objeto tiene el estado de
        if hasattr(obj, 'is_grounded'):
            # sale si ya estaba en el suelo
            if obj.is_grounded:
                return
            obj.is_grounded = True


    def __apply_gravity(self, obj: Player):
        """ Fijar la gravedad del mundo. """

        # aumenta la velocidad delta y, en proporcion a la fuerza de gravedad
        obj.dy += self._gravitation()


    def _gravitation(self):
        """ Calcula la gravitación del mundo. """

        pull = 0
        # aumenta la fuerza de gravedad
        pull += self.gravity
        # limita la fuerza de gravedad
        pull = min(pull, self.gravity)
        return pull