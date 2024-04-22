from kirby_animation_state.Animation import SpriteSheet


class Kirby(SpriteSheet):
    def __init__(self, image, frames, width, height, scale, colour, running, total_frame, left):
        super().__init__(image, frames, width, height, scale, colour, running, total_frame,left)

    # def get_image(self, frame,scale):
    #     image = pygame.Surface((self.width,self.height), pygame.SRCALPHA).convert_alpha()
    #     image.blit(self.sheet,(0,0), ((frame*self.width),0, self.width, self.height))
    #     image = pygame.transform.scale(image, (self.width*scale, self.height*scale))
    #     image.set_colorkey(self.colour)
    #     return image
