import math
import time

import pygame


class Entity:
    clock = pygame.time.Clock()

    def __init__(self, health, size, x, y, display, walk_animation, jump_animation, entity_class):
        self.health = health
        self.size = size
        self.x = x
        self.y = y
        self.walk_animation = walk_animation
        self.jump_animation = jump_animation
        self.display = display
        self.entity_class = entity_class
        self.down = False
        self.jump_c = 10
        self.left = False
        self.jumping = False
        self.animation = True
        self.gravity = 8
    def go_left(self, animation=True):
        self.left = True
        self.walk_animation.set_left(True)
        if self.animation:
            self.walk_animation.start_animation(3, self.display, x=self.x, y=self.y)
        self.x -= 11
        pygame.display.update()

    def go_right(self, animation=True):
        self.left = False
        self.walk_animation.set_left(False)
        if self.animation:
            self.walk_animation.start_animation(3, self.display, x=self.x, y=self.y)
        self.x += 11
        pygame.display.update()


    def get_image(self, frame, scale, width, height, sheet):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(pygame.image.load(sheet).convert_alpha(), (0, 0),
                   ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        if self.left == True:
            image = pygame.transform.flip(image, True, False)
        image.set_colorkey((255, 255, 255))
        return image
