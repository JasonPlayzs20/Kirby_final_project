import pygame
from kirby_animation_state.kirby_animation import Kirby


class Jump(Kirby):
    def __init__(self, frames=1, scale=None, left = False):
        super().__init__("kirby_animation_state/kirby_jump.png", frames, 24, 21, scale, (255, 255, 255), False, 10, left)
