from kirby_animation_state.kirby_animation import Kirby
class Kirby_Flapping(Kirby):
    def __init__(self, frames = None, scale = None):
        super().__init__("kirby_animation_state/Kirby_Flapping.png", frames, 26, 29, scale, (255,255,255), False, 4, False)
