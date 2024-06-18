import pygame

from kirby_animation_state.idle_animation import Idle
from levels.level1 import Level1


class Entity:
    clock = pygame.time.Clock()

    def __init__(self, health, size, x, y, display, level, chamber, flying, walk_animation, jump_animation,
                 entity_class):
        self.flying = False
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
        self.global_x = 0
        self.level = level
        self.chamber = chamber
        self.allow_right = True
        self.allow_left = True

    def get_level_endline(self, level, chamber):
        classes = {1: Level1()}
        level_list = getattr(classes.get(level, lambda x: None), 'get_levels', lambda x: None)
        level_last = level_list()[chamber]
        endline = level_last * 5.2 - 700
        return endline

    def get_global_x(self):
        return self.global_x

    idlee = Idle()

    def idle(self, scale=3):
        global idlee
        self.idlee.set_left(self.left)
        self.idlee.start_animation(scale, self.display, self.x, self.y + 7)

    def go_left(self, animation=True):
        self.left = True
        self.walk_animation.set_left(True)
        if not self.allow_left:
            self.animation = False
            if not self.flying:
                self.idle()
            return
        if self.animation:
            self.walk_animation.start_animation(3, self.display, x=self.x, y=self.y)

        if self.global_x < 500:
            self.x -= 11
        if self.get_global_x() > self.get_level_endline(self.level, self.chamber):
            self.x -= 11
        self.global_x -= 11
        pygame.display.update()

    def go_right(self, animation=True):
        self.left = False
        self.walk_animation.set_left(False)

        if not self.allow_right:
            self.animation = False
            if not self.flying:
                self.idle()
            return

        if self.animation:
            self.walk_animation.start_animation(3, self.display, x=self.x, y=self.y)

        if self.global_x < 500:
            self.x += 11
        if self.get_global_x() > self.get_level_endline(self.level, self.chamber):
            self.x += 11
        self.global_x += 11
        # print(self.distance)

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
