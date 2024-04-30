from Animation import SpriteSheet
from kirby_animation_state.kirby_animation import Kirby

class Suck_To_Fly(Kirby):
    def __init__(self, frames=0, scale=None, left=False):
        super().__init__("kirby_animation_state/kirby_sucking_to_fly.png", frames, 24, 24, scale, (255, 255, 255), False, 5, left)
