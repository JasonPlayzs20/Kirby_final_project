import pygame


class Collision:
    def __init__(self, gravity, level_map, kirby):
        self.gravity = gravity
        self.level_map = level_map
        self.kirby = kirby
        self.collision = False

    def detection(self, distance):
        gravity = True
        for y in range(len(self.level_map)):
            for x in range(len(self.level_map[y])):
                if self.level_map[y][x] == 1:
                    rect = pygame.Rect((x * 60) - distance, (y * 60), 60, 60)
                    pygame.draw.rect(self.kirby.display, (255, 0, 0), rect, 1)

                    if self.kirby.rect.colliderect(rect):
                        # Calculate overlap distances
                        overlap_left = self.kirby.rect.right - rect.left
                        overlap_right = rect.right - self.kirby.rect.left
                        overlap_top = self.kirby.rect.bottom - rect.top
                        overlap_bottom = rect.bottom - self.kirby.rect.top

                        # Determine the smallest overlap
                        min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                        if min_overlap == overlap_left:
                            print("Collision on the Left side")
                        elif min_overlap == overlap_right:
                            print("Collision on the Right side")
                        elif min_overlap == overlap_top:
                            print("Collision on the Top side")
                            gravity = False
                        elif min_overlap == overlap_bottom:
                            print("Collision on the Bottom side")
                            gravity = False

        if gravity:
            self.kirby.y += 5
