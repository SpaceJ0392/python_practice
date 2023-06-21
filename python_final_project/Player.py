from Sprite import Sprite


class Player(Sprite):
    def __init__(self):
        super().__init__(shape='dino_1.gif')
        self.goto(-250, -85)
        self.showturtle()
        self.dy = 0

    def jump(self):
        self.dy = 1
