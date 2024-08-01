import random
import time
from turtle import Screen
from paddle import Paddle
from brick import Brick
from ball import Ball
from livesboard import LivesBoard


screen = Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=500)
screen.tracer(0)

# create live count board
lives_board = LivesBoard()
lives_board.create_board()

# create the paddle and manage it's moving
paddle = Paddle()
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")


# create the bricks
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


# create the ball and start the game
ball = Ball()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # if ball collide the left or right walls
    if ball.xcor() <= -390 or ball.xcor() >= 390:
        ball.bounce_y()

    # if ball collide the upper wall
    if ball.ycor() >= 240:
        ball.bounce_x()

    # if ball collide with the paddle
    if ball.distance(paddle) < 120 and ball.ycor() <= -220:
        ball.bounce_x()

    # if ball collide lower wall without colliding the paddle
    if ball.ycor() <= -240:
        ball.hideturtle()
        ball = Ball()
        lives_board.update_live_count()
        lives_board.create_board()

        # if there is no life to play stop the game
        if lives_board.live == 0:
            game_is_on = False

        ball.move()

    # detecting of ball's collision with bricks
    for brick in bricks_array:
        if ball.distance(brick) < 37 and ball.ycor() >= 35:
            ball.bounce_x()
            brick.hideturtle()
            bricks_array.remove(brick)


screen.exitonclick()
