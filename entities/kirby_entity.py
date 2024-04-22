from kirby_animation_state import walk
from entities.entity import Entity

from kirby_animation_state.walk import Walk

class Kirby_Entity(Entity):
    def __init__(self, health, size, x, y, display):
        super().__init__(health, size, x, y, display, Walk())

    def suck(self):
        #play suck animaion at kirby
        #move kirby back
        pass

    def spit_out(self):
        pass

    def fly(self):
        pass

    def idle(self):
        pass
