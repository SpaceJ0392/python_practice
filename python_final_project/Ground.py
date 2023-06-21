from Sprite import Sprite


class Ground(Sprite):
    def __init__(self):
        super().__init__(shape='ground.gif')

    def set_ground(self, x, y=-100):
        # 플레이어가 위치할 배경
        self.goto(x, y)
        self.stamp()

        # self.goto(800, -100)
        # self.stamp()

        return self
