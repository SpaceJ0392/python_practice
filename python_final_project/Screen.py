import turtle
from tkinter import PhotoImage

from Sprite import Sprite


class Screen:
    def __init__(self):
        self.window = turtle.Screen()  # Screen()이 싱글톤 객체이므로 그냥 생성함.

    def set_up(self, shapes, bgcolor='white', width=0, height=0, title='title'):
        '''
        : window 창을 관리 하기 위한 옵션 정리
        '''
        self.window.bgcolor(bgcolor)
        self.window.setup(width, height)
        self.window.title(title)
        self.window.tracer(0)

        # 이미지 추가
        shapes = shapes

        for shape in shapes:
            re_shape = PhotoImage(file=shape).subsample(3, 3)
            shape_name = shape[shape.find('/')+1:len(shape)]
            self.window.addshape(shape_name, turtle.Shape('image', re_shape))

        return self.window

    @staticmethod
    def set_screen():
        # 상단 UI
        bg_turtle = Sprite()
        bg_turtle.goto(0, 120)
        bg_turtle.write("Jump Game", False, "center", ('나눔바른펜', 25))

    @staticmethod
    def set_ending(time):
        bg_turtle = Sprite()
        bg_turtle.goto(0, 90)
        bg_turtle.write("Game over", False, "center", ('나눔바른펜', 15))
        bg_turtle.goto(0, 70)
        bg_turtle.write(f"게임 시간 : {time} 초", False, "center", ('나눔바른펜', 10))

        bg_turtle.goto(0, -50)
        bg_turtle.write(f"press the window if you close it", False, "center", ('나눔바른펜', 15))
