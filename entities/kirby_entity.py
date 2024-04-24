from kirby_animation_state import walk
from entities.entity import Entity

from kirby_animation_state.walk import Walk
from kirby_animation_state.idle_animation import Idle
from kirby_animation_state.sucked_walk import Sucked_Walk

class Kirby_Entity(Entity):
    def __init__(self, health, size, x, y, display):
        self.health = health
        self.size = size
        self.x = x
        self.y = y
        self.display = display
        super().__init__(health, size, x, y, display, Walk(), self)

    sucked_walk = Sucked_Walk()

    def idle(self):
        print("no")
        idlee = Idle()

        idlee.start_animation(scale=3,display = self.display,x=self.x)

    def sucked_walk_left(self):

        self.sucked_walk.start_animation(scale=3, display=self.display, x = self.x, left= True)
        self.x -= 8
    def sucked_walk_right(self):
        global sucked_walk
        self.sucked_walk.start_animation(scale=3, display=self.display, x=self.x, left=False)
        self.x += 8
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
