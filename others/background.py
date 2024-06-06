import pygame.display

from levels.level import Level
from levels.level1 import Level1


class Background:
    def __init__(self, background_image, current_x, portview_image, portview_x, display):
        self.background_image = background_image
        self.current_x = current_x
        self.portview_image = portview_image
        self.portview_x = portview_x
        self.display = display
    def run_function_based_on_input(number):
        class_map = {1: Level1}
        (class_map.get(number, type("DefaultFunction", (object,),
                                    {"get_background": lambda self: print("No function for this number")}))()).get_background(1)

    # Example usage
    input_number = int(input("Enter a number: "))
    run_function_based_on_input(input_number)
    def get_image(self, image, display_x, display_y, frame, color_key):
        whiteboard = pygame.Surface((display_x,display_y),pygame.SRCALPHA).convert_alpha()
        whiteboard.blit(pygame.image.load(image).convert_alpha(),(0,0), (frame+display_x,0,display_x,display_y))
        whiteboard.set_colorkey(color_key)

    def register_background(self):
        self.display.blit(self.get_image(self.background_image,500,500,self.current_x,(0,0,0)))
        self.display.blit(self.get_image(self.portview_image,500,500,self.portview_x,(0,0,0)))
        pygame.display.update()
'''
The kirby

this class background (on edge)
if on edge just move
otherwise move background
'''