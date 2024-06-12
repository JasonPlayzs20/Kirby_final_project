import sys
import time

import pygame

from entities.kirby_entity import Kirby_Entity
from kirby_animation_state.idle_animation import Idle
from kirby_animation_state.walk import Walk
from levels.level1 import Level1
from others.background import Background

pygame.init()

screen_h = 1080
screen_w = 700
display = pygame.display.set_mode((screen_h, screen_w))
pygame.display.set_caption("why is kirby")
clock = pygame.time.Clock()

BG = (50, 70, 50)
BLACK = (255, 255, 255)
animation = True
run = True
frame = 0

kirby = Kirby_Entity(20, 3, 0, 484, display)  # SCALE NOT WORK
background = Background(0,0,display,kirby,5.2)
tick = 0
# kirby.distance = 9000
Level1()
box_size = 60
while run:
    clock.tick(60)
    display.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit(69)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the top-left corner of the box
    print((background.background_distance+mouse_x)//box_size)
    # grid_x = ((-background.background_distance+mouse_x)//box_size)*box_size
    grid_x = ((-background.background_distance+mouse_x)//box_size)*box_size+(background.background_distance+mouse_x)

    grid_y = (mouse_y // box_size) * box_size

    # Draw the box

    background.register_background()
    kirby.keys_update()
    pygame.draw.rect(display, (255,0,0), (grid_x, grid_y, 12*5, 12*5),1)
    pygame.display.update()


