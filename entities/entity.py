import pygame


class Entity:
    def __init__(self, health, size, x, y, display, walk_animation, entity_class):
        self.health = health
        self.size = size
        self.x = x
        self.y = y
        self.walk_animation = walk_animation
        self.display = display
        self.entity_class = entity_class
    def go_left(self, left = True):
        print(self.x)
        self.walk_animation.start_animation(3,self.display, left, x=self.x)
        self.x -= 4

    def go_right(self):
        self.walk_animation.start_animation(3,self.display, x=self.x)
        self.x += 4
