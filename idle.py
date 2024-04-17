from kirby import Kirby
import pygame

class Idle(Kirby):

    def __init__(self,running = False, frames= None,scale = None, total_frame = 16):
        self.sheet = "d4pnix0-4054eedb-e686-4e39-96c1-227b7c246bbf (2) - Copy.png"
        self.frames = frames
        self.width = 25
        self.height = 31
        self.scale = scale
        self.colour = (255,255,255)
        self.running = running
        self.total_frame = 16
        super().__init__(self.sheet, frames, self.width, self.height, scale, self.colour, running, total_frame)

    # def get_image(self, frame,scale):
    #     image = pygame.Surface((self.width,self.height), pygame.SRCALPHA).convert_alpha()
    #     image.blit(self.sheet,(0,0), ((frame*self.width),0, self.width, self.height))
    #     image = pygame.transform.scale(image, (self.width*scale, self.height*scale))
    #     image.set_colorkey(self.colour)
    #     return image
