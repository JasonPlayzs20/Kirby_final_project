import pygame

from kirby_animation_state.idle import Idle
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


def get_image(sheet, frame, width, height, scale, colour):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width) + 4, 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)
    return image


# frame0 = get_image(sprite_sheet_image,0,31,31,3, BLACK)


run = True
frame = 0
# sprite_sheet = Animation.SpriteSheet(sprite_sheet_image)
idle = Idle()
walk = Walk()
while run:
    clock.tick(8)
    display.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    print("updated")
    walk.start_animation(3, display)
