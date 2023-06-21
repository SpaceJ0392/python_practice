import math
import random
from Sprite import Sprite


class Hurdle(Sprite):

    def __init__(self, dx=-0.2):
        super().__init__(shape='cacti.gif', y=-90)
        self.dx = dx
        self.dy = 0

    def is_aabb_collision(self, other):
        # 충돌 메서드
        x_collision = (math.fabs(self.xcor() - other.xcor()) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.ycor() - other.ycor()) * 2) < (self.height + other.height)
        return x_collision and y_collision

    # 허들 생성
    @staticmethod
    def make_hurdle(dx=-0.2):
        hurdle = []
        extra = 0

        num = random.randrange(1, 4)

        for _ in range(num):
            item = Hurdle(dx=dx)
            item.setx(random.randrange(300 + extra, 800 + extra))
            item.showturtle()
            hurdle.append(item)
            extra += 80

        return hurdle
