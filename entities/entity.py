import math

import pygame


class Entity:
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
    def go_left(self, left = True):
        print(self.x)
        self.walk_animation.start_animation(3,self.display, left, x=self.x, y = self.y)
        self.x -= 4

    def go_right(self):
        self.walk_animation.start_animation(3,self.display, x=self.x, y = self.y)
        self.x += 11
    def get_image(self, frame, scale, left, width, height, sheet):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(pygame.image.load(sheet).convert_alpha(), (0, 0),
                   ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        if left == True:
            image = pygame.transform.flip(image,True,False)
        image.set_colorkey((255,255,255))
        return image
    def jump(self, height):
        print("hi")
        if self.jump_c >= -10:
            neg = 1
            image = self.get_image(0, 3, left=False, width=24, height=21, sheet="kirby_animation_state/kirby_jump.png")


            if self.jump_c < 0:
                neg = -1
                self.jump_animation.start_animation(3, self.display, x=self.x, y=self.y)
            else:
                self.display.blit(image, (self.x, self.y))
            self.y -=(self.jump_c**2)/height*neg
            self.jump_c-=1
            pygame.display.update()

        else:
            self.jump_c = 10














        # global tempy
        # # self.y = math.floor(self.y)
        # print(str(self.down) + " self.down")
        # # if self.y == self.tempy-height and self.down == False: #+1
        # #     #start down
        # #     self.down = True
        # # elif self.y >= self.tempy:
        # #     #stop down
        # #     self.down = False
        #
        #
        # if self.y >= self.tempy and self.down == True:
        #     self.down = False
        # elif self.y == self.tempy-height and self.down == False:
        #     self.down = True
        #
        #     # print("setted")
        # if self.y >= self.tempy - height and self.down == False:
        #     image = self.get_image(0, 3, left=False, width=24, height=21, sheet="kirby_animation_state/kirby_jump.png")
        #     self.display.blit(image, (self.x, self.y))
        #     pygame.display.update()
        #     # print("go up?")
        #     print(self.y,"self.y")
        #     if self.y < self.tempy - height + 20:
        #         distance_to_target = abs((self.tempy - height) - self.y)
        #         self.y -= round(abs((distance_to_target+5)/4))
        #     else:
        #         self.y -= 10
        # else:
        #     self.jump_animation.start_animation(3, self.display, x=self.x, y=self.y)
        #     # print("go down?")
        #     print(self.y,"self.y")
        #     self.y += 31

