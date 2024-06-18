import pygame


class Collision:
    def __init__(self, gravity, level_map, kirby):
        self.gravity = gravity
        self.level_map = level_map
        self.kirby = kirby
        self.collision = False
        self.disable =  False

    def jump_collide(self, distance):
        gravity = True
        collided_rects = []

        for y in range(len(self.level_map)):
            for x in range(len(self.level_map[y])):
                if self.level_map[y][x] == 1:
                    rect = pygame.Rect((x * 60) - distance, (y * 60) + 15, 60, 60)
                    # pygame.draw.rect(self.kirby.display, (255, 0, 0), rect, 1)
                    if self.kirby.jump_rect.colliderect(rect):
                        collided_rects.append(rect)
                        print("collider")

        if collided_rects:
            # Find the highest ground rectangle (i.e., the one with the smallest top value)
            highest_rect = min(collided_rects, key=lambda r: r.top)
            if self.kirby.jump_rect.bottom > highest_rect.top - 10:
                self.disable = True
                print("*" * 85)
                print(self.kirby.rect.bottom, "bottom + displacement")
                print(highest_rect.top)
                gravity = False
                self.kirby.jump_rect = pygame.Rect(self.kirby.x + 20, self.kirby.y, 35, 60)
                # Adjust Kirby's y position based on the highest ground rectangle
                self.kirby.y = highest_rect.top - self.kirby.rect.height
                print(highest_rect,self.kirby.rect.height)
                self.kirby.jump_c = 12
                print('jasobin')
                self.kirby.jumping = False

        if gravity:
            # Apply gravity effect if no collision with ground
            self.kirby.y += self.gravity

    def detection(self, distance, back):
        gravity = True
        print(self.kirby.y)
        print()
        if not self.kirby.jumping:
            self.disable = False
        self.kirby.allow_right = True
        self.kirby.animation = True
        self.kirby.allow_left = True
        for y in range(len(self.level_map)):
            for x in range(len(self.level_map[y])):
                if self.level_map[y][x] == 1:
                    rect = pygame.Rect((x * 60) - distance, (y * 60) + 15, 60, 60)
                    pygame.draw.rect(self.kirby.display, (255, 0, 0), rect, 1)
                    if self.kirby.rect.colliderect(rect):
                        # Determine collision sides
                        if self.kirby.rect.bottom > rect.top and self.kirby.rect.bottom < rect.bottom and not self.disable:
                            # print("Normal collision")

                            self.kirby.y -= self.kirby.rect.bottom - rect.top - 1
                            gravity = False

                        elif self.kirby.rect.top < rect.bottom and self.kirby.rect.bottom > rect.bottom:
                            # print(self.kirby.rect.top - rect.bottom-1)
                            self.kirby.y += abs(self.kirby.rect.top - rect.bottom - 1)

                    if self.kirby.side_rect.colliderect(rect):
                        if self.kirby.side_rect.right > rect.left and self.kirby.side_rect.right < rect.right:
                            # print(self.kirby.side_rect.right, rect.left + 13)

                            self.kirby.animation = False
                            self.kirby.allow_right = False
                            # print(self.kirby.side_rect.right - rect.left)

                        elif self.kirby.side_rect.left < rect.right and self.kirby.side_rect.right > rect.right:
                            # print(self.kirby.side_rect.right, rect.left + 13)
                            # print("left")
                            self.kirby.animation = False
                            self.kirby.allow_left = False
                            # print(self.kirby.side_rect.right - rect.left)
        if gravity:
            if not self.kirby.flapping:
                self.kirby.y += 5
