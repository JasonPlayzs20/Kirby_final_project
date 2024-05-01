import pygame
from kirby_animation_state.kirby_animation import Kirby


class Sucked_Walk(Kirby):
    def __init__(self, frames=None, scale=None, left=False):
        super().__init__("kirby_animation_state/kirby_sucked_walk.png", frames, 33, 28, scale, (255, 255, 255), False,
                         14, left)
