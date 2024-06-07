import sys
import time

import pygame

from entities.kirby_entity import Kirby_Entity
from kirby_animation_state.idle_animation import Idle
from kirby_animation_state.walk import Walk
from others.background import Background

pygame.init()

screen_h = 1080
screen_w = 700
display = pygame.display.set_mode((screen_h, screen_w))
pygame.display.set_caption("why is kirby")
clock = pygame.time.Clock()

BG = (50, 70, 50)
BLACK = (255, 255, 255)
sprite_sheet_image = pygame.image.load("d4pnix0-4054eedb-e686-4e39-96c1-227b7c246bbf (2) - Copy.png").convert_alpha()
animation = True
run = True
frame = 0

kirby = Kirby_Entity(20, 3, 0, 484, display)  # SCALE NOT WORK
background = Background(0,0,display,kirby,5.2)
tick = 0
while run:
    clock.tick(11)
    display.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit(69)
    background.register_background()
    kirby.keys_update()

