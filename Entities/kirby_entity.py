import pygame
from Entities.entity import Entity
from kirby import Kirby
class Kirby_Entity(Entity):
    def __init__(self, health, size, x, y):
        super().__init__(health,size,x,y)

    def suck(self):
        pass
    def spit_out(self):
        pass
    def fly(self):
        pass
    def idle(self):
        pass
