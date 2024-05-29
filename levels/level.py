import pygame


class Level:
    def __init__(self, image, total_sections, *level_data):
        self.image = image
        self.total_selections = total_sections
        self.level_data = level_data #different scetions cords/others

    def get_background(self,section):
        if section > self.total_selections: return False
        section -= 1
        image = pygame.Surface((self.level_data[section], 500),pygame.SRCALPHA).convert_alpha()
        image.blit(pygame.image.load(self.image).convert_alpha(),(0,0),(self.level_data[section],0,self.level_data[section],500))
        image.set_colorkey((255,255,255))
        return image

