import time

import pygame.display

from kirby_animation_state import walk
from entities.entity import Entity
from kirby_animation_state.kirby_jump import Jump

from kirby_animation_state.walk import Walk
from kirby_animation_state.idle_animation import Idle
from kirby_animation_state.sucked_walk import Sucked_Walk
from kirby_animation_state.suck_to_fly import Suck_To_Fly

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
    suck_fly_class = Suck_To_Fly()
    def idle(self, scale = 3):
        global idlee
        self.idlee.set_left(self.left)
        self.idlee.start_animation(scale,self.display,self.x,self.y+7)
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
    def suck_fly(self):
        self.suck_fly_class.set_left(self.left)
        self.suck_fly_class.start_animation(scale=3,display=self.display,x=self.x,y = self.y-8)

    def fly(self):
        pass
    def jump(self, height):
        self.jumping = True
        if self.jumping == True:
            self.clock.tick(25)
            self.jump_animation.set_left(self.left)
            if self.jump_c >= -10:
                neg = 1
                image = self.get_image(0, 3, width=24, height=21, sheet="kirby_animation_state/kirby_jump.png")


                if self.jump_c < 0:
                    neg = -1
                    self.jump_animation.start_animation(3, self.display, x=self.x, y=self.y)
                else:
                    self.display.blit(image, (self.x, self.y))
                self.y -=(self.jump_c**2)/height*neg
                self.jump_c-=2
                pygame.display.update()

            else:
                image = self.get_image(9, 3, width=24, height=21, sheet="kirby_animation_state/kirby_jump.png")
                self.display.blit(image,(self.x,self.y))
                pygame.display.update()
                time.sleep(0.2)
                self.jump_c = 10
                self.jumping = False
            self.display.fill((50, 70, 50))

