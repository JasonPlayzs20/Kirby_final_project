from kirby_animation_state import walk
from entities.entity import Entity

from kirby_animation_state.walk import Walk
from kirby_animation_state.idle_animation import Idle

class Kirby_Entity(Entity):
    def __init__(self, health, size, x, y, display):
        self.health = health
        self.size = size
        self.x = x
        self.y = y
        self.display = display
        super().__init__(health, size, x, y, display, Walk(), self)

    def idle(self):
        print("no")
        idlee = Idle()

        idlee.start_animation(scale=3,display = self.display,x=self.x)
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
