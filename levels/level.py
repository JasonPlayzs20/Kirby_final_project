import pygame


class Level:
    def __init__(self, image, total_sections, map,*level_data):
        self.image = image
        self.total_selections = total_sections
        self.level_data = level_data #different scetions cords/others
        self.map = map

    def get_level(self, chamber,size=5.2):
        if chamber > self.total_selections:
            return None  # Return None instead of False
        # section -= 1
        # print(self.level_data[section])
        image = pygame.Surface((self.level_data[chamber], 500), pygame.SRCALPHA).convert_alpha()
        image.blit(pygame.image.load(self.image).convert_alpha(), (-10, 0), (0, 0, self.level_data[chamber]*5.2, 500))
        # image.blit(pygame.image.load(self.image).convert_alpha(), (0, 0), (1500, 0, 10000, 500))

        image = pygame.transform.scale(image, (self.level_data[chamber]*size, 500*size))
        image.set_colorkey((255, 255, 255))
        return image

    def get_levels(self):
        return self.level_data


