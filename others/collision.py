class Collision:
    def __init__(self, gravity,y):
        self.gravity = gravity
        self.y = y

    def start_gravity(self):
        self.y += self.gravity

    def collision(self,object):


    