import sys
import pygame

from entities.kirby_entity import Kirby_Entity
from levels.level1 import Level1
from levels.background import Background

pygame.init()

screen_h = 1080
screen_w = 700
display = pygame.display.set_mode((screen_h, screen_w))
pygame.display.set_caption("why is kirby")
clock = pygame.time.Clock()

BG = (50, 70, 50)
box_color = (255, 0, 0)
run = True
kirby = Kirby_Entity(20, 3, 0, 484, display)  # SCALE NOT WORK
background = Background(0, 0, display, kirby, 5.2)
kirby.background = background
box_size = 60

level1 = Level1()

def save_level(map_data):
    with open("levels/level1.txt", "w") as file:
        for row in map_data:
            file.write(",".join(map(str, row)) + "\n")

while run:
    clock.tick(11)
    display.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit(69)
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_x, mouse_y = pygame.mouse.get_pos()
        #     grid_x = int((background.background_distance + mouse_x) // box_size)
        #     grid_y = int(mouse_y // box_size)
        #     if 0 <= grid_y < len(level1.map) and 0 <= grid_x < len(level1.map[grid_y]):
        #         level1.map[grid_y][grid_x] = 1
        #         save_level(level1.map)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.display.set_caption(f"{mouse_x},{mouse_y}")
    background_distance = background.background_distance
    grid_x = int((background_distance + mouse_x) // box_size * box_size - background_distance)
    grid_y = int(mouse_y // box_size * box_size)

    background.register_background()
    kirby.keys_update()
    background.start_collision()


    for y, row in enumerate(level1.map):
        for x, cell in enumerate(row):
            if cell == 1:
                draw_x = x * box_size - background_distance
                draw_y = y * box_size
                # pygame.draw.rect(display, box_color, (draw_x, draw_y, box_size, box_size), 1)

    pygame.draw.rect(display, box_color, (grid_x, grid_y, box_size, box_size), 1)
    pygame.display.update()
