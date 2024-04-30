from Animation import SpriteSheet


class Kirby(SpriteSheet):
    def __init__(self, image: object, frames: object, width: object, height: object, scale: object, colour: object, running: object, total_frame: object, left: object) -> object:
        super().__init__(image, frames, width, height, scale, colour, running, total_frame,left)

    # def get_image(self, frame,scale):
    #     image = pygame.Surface((self.width,self.height), pygame.SRCALPHA).convert_alpha()
    #     image.blit(self.sheet,(0,0), ((frame*self.width),0, self.width, self.height))
    #     image = pygame.transform.scale(image, (self.width*scale, self.height*scale))
    #     image.set_colorkey(self.colour)
    #     return image
