import pygame

class Collision:
    def __init__(self, gravity, level_map, kirby):
        self.gravity = gravity
        self.level_map = level_map
        self.kirby = kirby
        self.collision = False

    def detection(self, distance,back):
        gravity = True
        self.kirby.allow_right = True
        self.kirby.animation = True
        self.kirby.allow_left = True
        for y in range(len(self.level_map)):
            for x in range(len(self.level_map[y])):
                if self.level_map[y][x] == 1:
                    rect = pygame.Rect((x * 60) - distance, (y * 60)+15, 60, 60)
                    pygame.draw.rect(self.kirby.display, (255, 0, 0), rect, 1)
                    if self.kirby.rect.colliderect(rect):
                        # Determine collision sides
                        if self.kirby.rect.bottom > rect.top and self.kirby.rect.bottom<rect.bottom:
                            # print(self.kirby.rect.top, rect.top)
                            self.kirby.y -= self.kirby.rect.bottom - rect.top - 1
                            gravity = False

                        elif self.kirby.rect.top < rect.bottom and self.kirby.rect.bottom >rect.bottom:
                            print(self.kirby.rect.top - rect.bottom-1)
                            self.kirby.y += abs(self.kirby.rect.top - rect.bottom-1)




                    if self.kirby.side_rect.colliderect(rect):
                        if self.kirby.side_rect.right > rect.left and self.kirby.side_rect.right < rect.right:
                            print(self.kirby.side_rect.right, rect.left + 13)

                            self.kirby.animation = False
                            self.kirby.allow_right = False
                            print(self.kirby.side_rect.right - rect.left)

                        elif self.kirby.side_rect.left < rect.right and self.kirby.side_rect.right > rect.right:
                            # print(self.kirby.side_rect.right, rect.left + 13)
                            print("left")
                            self.kirby.animation = False
                            self.kirby.allow_left = False
                            # print(self.kirby.side_rect.right - rect.left)
        if gravity:
            if not self.kirby.flapping:
                self.kirby.y += 5

