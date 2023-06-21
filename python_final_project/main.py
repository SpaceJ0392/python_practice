import time
import turtle

from Ground import Ground
from Hurdle import Hurdle
from Player import Player
from Screen import Screen

window = Screen()
window = window.set_up(['cacti.gif', 'dino_1.gif', 'ground.gif'], width=600, height=400, title='python_final')

# 배경 초기화
Screen.set_screen()

# 바닥 초기화
ground = Ground()
ground.set_ground(0)
ground_speed = -0.13

# 플레이어 생성
player = Player()
gravity = -0.0034

# 허들 생성
hurdle = Hurdle.make_hurdle()
speed = -0.2

# 키보드 입력
window.listen()
window.onkeypress(lambda: player.jump(), 'space')

# 타이머 (종료 시간 측정)
begin = time.time()
temp = begin

# 끝을 알림
end_flag = False
while not end_flag:
    # 타이머 기능
    end = time.time()

    # 허들 없으면 추가 생성
    if len(hurdle) == 0:
        hurdle = Hurdle.make_hurdle(dx=speed)

    for item in hurdle:
        # 허들 이동 & 바닥 이동
        item.setx(item.xcor() + item.dx)
        ground.clear()
        ground.set_ground(ground.xcor() + ground_speed)  # 초기에 허들과의 속도 차로 인해 임의로 설정

        # 허들이 공간을 넘어가면 삭제
        if item.xcor() < -350:
            hurdle.remove(item)
            item.clear()

        # 바닥이 없어지기 전에 새로운 바닥 생성
        if ground.xcor() < -100:
            ground.clear()
            ground.set_ground(100 + speed)

        # 허들과 충돌시 게임 종료
        if item.is_aabb_collision(player):
            end_flag = True
            temp = round(end - begin, 1)

            Screen.set_ending(temp)

    # 사긴이 5초이상 경과 하면 허들 속도 증가 (단, 최대 속도는 -0.5)
    if end - temp > 5 and speed > -0.5:
        speed -= 0.05
        temp = end

    # 플레이어 점프시 중력에 따른 상하 이동
    player.dy += gravity
    player.sety(player.ycor() + player.dy)

    if player.ycor() <= -90:
        player.dy = 0
        player.sety(-90)

    window.update()

turtle.exitonclick()  # 게임 종료 후 창 유지 및 화면 클릭시 화면 닫기
