import sys
import time

import pygame

from entities.kirby_entity import Kirby_Entity
from kirby_animation_state.idle_animation import Idle
from kirby_animation_state.walk import Walk

pygame.init()

screen_h = 500
screen_w = 500
display = pygame.display.set_mode((screen_h, screen_w))
pygame.display.set_caption("Max is gay")
clock = pygame.time.Clock()

BG = (50, 70, 50)
BLACK = (255, 255, 255)
sprite_sheet_image = pygame.image.load("d4pnix0-4054eedb-e686-4e39-96c1-227b7c246bbf (2) - Copy.png").convert_alpha()

run = True
frame = 0
# sprite_sheet = Animation.SpriteSheet(sprite_sheet_image)
# idle = Idle()
walk = Walk()
kirby = Kirby_Entity(20, 7, 0, 200, display) #SCALE NOT WORK
tick = 0
while run:
    clock.tick(11)
    display.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit(69)
    print("max is gay")
    print(tick)
    if tick < 21:
        kirby.jump(2)
        print(kirby.jumping)
        if kirby.jumping == True:
            print("yesed")
            kirby.go_right(animation=False)


    if tick > 21:
        kirby.sucked_walk_left()
        print(kirby.left)
    if tick > 40:
        tick = 0
        if kirby.jumping == False:
            kirby.jump(2)
            continue

    tick +=1

    # kirby.idle()
