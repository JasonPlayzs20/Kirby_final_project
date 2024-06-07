import pygame.display

from entities.kirby_entity import Kirby_Entity
from levels.level import Level
from entities.entity import Entity
from levels.level1 import Level1


class Background:
    def __init__(self, current_x, portview_x, display, kirby,size):
        self.current_x = current_x
        self.portview_x = portview_x
        self.display = display
        self.size = size
        self.kirby = kirby
        self.distance = 0

    def get_bg(self,number, chamber):
        classes = {1: Level1()}

        return getattr(classes.get(number, lambda x: None), 'get_level', lambda x: None)(chamber,self.size)


    def register_background(self):
        self.distance = self.kirby.get_distance()
        if self.kirby.get_distance() < 0:
            self.distance = 0
        self.display.blit(self.get_bg(1,1),(-self.distance,0))
        # self.display.blit(self.get_image(self.portview_image,500,500,self.portview_x,(0,0,0)))
        # pygame.display.update()
'''
The kirby

this class background (on edge)
if on edge just move
otherwise move background
'''
