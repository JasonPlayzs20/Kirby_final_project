from kirby_animation_state.kirby_animation import Kirby
class Kirby_Fly_Idle(Kirby):
    def __init__(self, frames = None, scale = None):
        super().__init__("kirby_animation_state/Kirby_Fly_Idle.png", frames, 32, 27, scale, (255,255,255), False, 3, False)
