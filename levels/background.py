import pygame.display

from entities.kirby_entity import Kirby_Entity
from levels.level import Level
from entities.entity import Entity
from levels.level1 import Level1
from others.collision import Collision


class Background:
    def __init__(self, current_x, portview_x, display, kirby,size):
        self.current_x = current_x
        self.portview_x = portview_x
        self.display = display
        self.size = size
        self.kirby = kirby
        self.background_distance = 0
        self.classes = {1: Level1()}
        self.level = self.kirby.level
        self.chamber = self.kirby.chamber
        self.collision = Collision(3,self.classes[self.kirby.level].map,kirby)


    def get_bg(self,level, chamber):

        return self.classes[level].get_level(chamber)

    def get_level_endline(self,level,chamber):
        level_last = self.classes[level].get_levels()[chamber]
        endline = level_last*5.2-700
        return endline
    def register_background(self):
        self.background_distance = self.kirby.get_global_x()-500
        if self.kirby.get_global_x() < 500:
            self.background_distance = 0
        if self.kirby.get_global_x() > self.get_level_endline(self.level,self.chamber):
            self.background_distance = self.get_level_endline(self.level,self.chamber)-500

        self.display.blit(self.get_bg(self.level,self.chamber),(-self.background_distance,0))

    def start_collision(self):
        self.collision.detection(self.background_distance,self)



        # self.display.blit(self.get_image(self.portview_image,500,500,self.portview_x,(0,0,0)))
        # pygame.display.update()
'''
The kirby

this class background (on edge)
if on edge just move
otherwise move background
'''
