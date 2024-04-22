import pygame
from kirby_animation_state.kirby_animation import Kirby


class Walk(Kirby):
    def __init__(self, frames=None, scale=None, left = False):
        super().__init__("kirby_animation_state/kirby_walk.png", frames, 24, 21, scale, (255, 255, 255), False, 11, left)
