from levels.level import Level


class Level1(Level):
    def __init__(self):
        # x = 13
        map =[[],
              [],
              [],
              [],
              [],
              [],
              [],
              [],
              [],
              [],
              [],
              []
              ]
        super().__init__("levels/Kirby_level_1.png", 3, 0,953, 10000,2673*5.2)
