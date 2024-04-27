import pygame.display

from kirby_animation_state import walk
from entities.entity import Entity
from kirby_animation_state.kirby_jump import Jump

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
        self.sucked = False
        super().__init__(health, size, x, y, display, Walk(), Jump(), self)

    sucked_walk = Sucked_Walk()
    idlee = Idle()
    def idle(self):
        global idlee
        image = self.get_image(0, 3, width=24, height=21, sheet="kirby_animation_state/kirby_jump.png")
        self.display.blit(image, (self.x, self.y))
        pygame.display.update()
    def sucked_walk_left(self, scale = 3, walk_speed = 11):
        self.sucked_walk.set_left(True)
        self.left = True
        self.sucked_walk.start_animation(scale=scale, display=self.display, x = self.x, y = self.y-18)
        self.x -= walk_speed
    def sucked_walk_right(self, scale = 3, walk_speed = 11):
        global sucked_walk
        self.sucked_walk.set_left(False)
        self.left = False
        self.sucked_walk.start_animation(scale=scale, display=self.display, x=self.x, y = self.y-15)
        self.x += walk_speed
    def suck(self):
        #play suck animaion at kirby
        #move kirby back
        pass

    def spit_out(self):
        pass

    def fly(self):
        pass


