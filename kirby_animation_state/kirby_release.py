import pygame
from kirby_animation_state.kirby_animation import Kirby


class Kirby_Release(Kirby):
    def __init__(self, frames=1, scale=None, left = False):
        super().__init__("kirby_animation_state/Kirby_unsuck.png", frames, 23, 24, scale, (255, 255, 255), False, 10, left)
