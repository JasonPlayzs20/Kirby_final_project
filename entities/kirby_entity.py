import time

import pygame.display

from kirby_animation_state import walk
from entities.entity import Entity
from kirby_animation_state.kirby_flapping_animation import Kirby_Flapping
from kirby_animation_state.kirby_fly_idle import Kirby_Fly_Idle
from kirby_animation_state.kirby_jump import Jump

from kirby_animation_state.walk import Walk
from kirby_animation_state.idle_animation import Idle
from kirby_animation_state.sucked_walk import Sucked_Walk
from kirby_animation_state.suck_to_fly import Suck_To_Fly


class Kirby_Entity(Entity):
    def __init__(self, health, size, x, y, display):
        self.sucked = False
        self.flying = False
        self.flapping = False
        self.level = 1
        self.page = 1
        self.level = 1
        self.rect = pygame.Rect(x+5,y,66,66)
        self.chamber = 1
        super().__init__(health, size, x, y, display,self.level,self.chamber, Walk(), Jump(), self)

    sucked_walk = Sucked_Walk()
    idlee = Idle()
    suck_fly_class = Suck_To_Fly()
    suck_idle_fly_class = Kirby_Fly_Idle()
    flapping_class = Kirby_Flapping()

    def idle(self, scale=3):
        global idlee
        self.idlee.set_left(self.left)
        self.idlee.start_animation(scale, self.display, self.x, self.y + 7)

    def sucked_walk_left(self, scale=3, walk_speed=11):
        self.sucked_walk.set_left(True)
        self.left = True
        self.sucked_walk.start_animation(scale=scale, display=self.display, x=self.x, y=self.y - 18)
        self.globalx -= walk_speed

    def sucked_walk_right(self, scale=3, walk_speed=11):
        global sucked_walk
        self.sucked_walk.set_left(False)
        self.left = False
        self.sucked_walk.start_animation(scale=scale, display=self.display, x=self.x, y=self.y - 15)
        self.globalx += walk_speed

    def suck(self):
        # play suck animaion at kirby
        # move kirby back
        pass

    def spit_out(self):
        pass

    def suck_fly(self):
        if self.flying == True: return
        self.flying = False
        self.animation = False
        self.suck_fly_class.set_left(self.left)
        self.suck_fly_class.start_animation(scale=self.size, display=self.display, x=self.x-4, y=self.y - 18)
        if self.suck_fly_class.frames == 3:
            self.flying = True

    def fly_idle(self):
        self.flying = True
        self.flapping = False
        self.animation = False
        self.suck_idle_fly_class.set_left(self.left)
        self.suck_idle_fly_class.start_animation(scale=self.size, display=self.display, x=self.x-4, y=self.y - 18)
    def fly_up(self):
        self.flapping = True
        self.flying = True
        self.animation = False
        self.flapping_class.set_left(self.left)
        self.flapping_class.start_animation(scale=self.size, display=self.display, x=self.x+4, y=self.y-18)
        self.y -= 10

    def jump(self, height):
        self.jumping = True
        self.animation = False
        if self.jumping == True:
            self.clock.tick(25)
            self.jump_animation.set_left(self.left)
            if self.jump_c >= -10:
                neg = 1
                image = self.get_image(0, self.size, width=24, height=21, sheet="kirby_animation_state/kirby_jump.png")

                if self.jump_c < 0:
                    neg = -1
                    self.jump_animation.start_animation(3, self.display, x=self.x, y=self.y)
                else:
                    self.display.blit(image, (self.x, self.y))
                self.y -= (self.jump_c ** 2) / height * neg
                self.jump_c -= 2
                pygame.display.update()

            else:
                image = self.get_image(9, self.size, width=24, height=21, sheet="kirby_animation_state/kirby_jump.png")
                self.display.blit(image, (self.x, self.y))
                pygame.display.update()
                time.sleep(0.2)
                self.jump_c = 10
                self.jumping = False
                self.animation = True
            # self.display.fill((50, 70, 50))

    def keys_update(self):
        active = False
        self.rect = pygame.Rect(self.x+6, self.y, 66, 66)
        pygame.draw.rect(self.display, (0, 255, 0), self.rect,2)
        self.flapping = False
        keys = pygame.key.get_pressed()
        # jumping
        if not self.jumping:
            self.animation = True
        if self.jumping:
            self.jump(2)
            active = True
            self.animation = False
        elif keys[pygame.K_LALT]:
            if not self.jumping:
                self.jump(2)
                active = True
            else:
                self.animation = False
        # start flying
        if keys[pygame.K_UP]:
            active = True
            if not self.flying:
                self.suck_fly()
            else:
                self.fly_up()
        # left
        if keys[pygame.K_LEFT]:
            if self.flying:
                if not self.flapping:
                    self.fly_idle()
                    self.go_left(False)
                else:
                    self.go_left(False)
            else:
                self.go_left(self.animation)
            active = True
        # right
        elif keys[pygame.K_RIGHT]:
            if self.flying:
                if not self.flapping:
                    self.fly_idle()
                    self.go_right(False)
                else:
                    self.go_right(False)
            else:
                self.go_right(self.animation)
            active = True
        # idles
        if active is not True:
            if not self.flying:
                self.idle()
            else:
                self.fly_idle()
                # self.y += 3
