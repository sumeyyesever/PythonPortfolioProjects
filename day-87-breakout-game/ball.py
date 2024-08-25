from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -220)
        self.ball_xcor = -10
        self.ball_ycor = 10

    def move(self):
        x_cor = self.xcor() + self.ball_xcor
        y_cor = self.ycor() + self.ball_ycor
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.ball_xcor *= -1

    def bounce_x(self):
        self.ball_ycor *= -1

