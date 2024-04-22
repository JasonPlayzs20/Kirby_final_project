import pygame


class Entity:
    def __init__(self, health, size, x, y, display, walk_animation):
        self.health = health
        self.size = size
        self.x = x
        self.y = y
        self.walk_animation = walk_animation
        self.display = display
    def go_left(self, left = True):
        self.walk_animation.start_animation(3,self.display, left)
        pass

    def go_right(self):
        pass
