from kirby_animation_state.kirby_animation import Kirby
import pygame


class Idle(Kirby):

    def __init__(self, frames=None, scale=None):
        super().__init__("kirby_animation_state/kirby_walk.png", frames, 24, 21, scale, (255, 255, 255), False, 16, left=False)
    # def get_image(self, frame,scale):
    #     image = pygame.Surface((self.width,self.height), pygame.SRCALPHA).convert_alpha()
    #     image.blit(self.sheet,(0,0), ((frame*self.width),0, self.width, self.height))
    #     image = pygame.transform.scale(image, (self.width*scale, self.height*scale))
    #     image.set_colorkey(self.colour)
    #     return image
