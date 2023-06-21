import turtle


class Sprite(turtle.Turtle):
    def __init__(self, shape='turtle',  color='black', location=0, height=10, width=10, x=0, y=0):
        # Sprite 기본 설정
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.right(location)
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.goto(x, y)

        self.height = height
        self.width = width
