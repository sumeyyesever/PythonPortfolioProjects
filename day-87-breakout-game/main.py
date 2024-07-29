import random
from turtle import Screen
from paddle import Paddle
from brick import Brick

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=500)
screen.title("Breakout")
screen.tracer(0)
paddle = Paddle()
bricks_array = []


stretch_l_array = [2, 3, 4]
for i in range(3):
    y_cor = 120 - 25*i
    x_cor = -400
    while x_cor <= 400:
        random_stretch = random.choice(stretch_l_array)
        x_cor = x_cor + random_stretch * 10
        brick = Brick(x_cor, y_cor, random_stretch)
        x_cor = x_cor + random_stretch * 10 + 5
        bricks_array.append(brick)


screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
