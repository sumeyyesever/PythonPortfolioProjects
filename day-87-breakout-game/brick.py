from turtle import Turtle
import random

BRICK_COLOR = ["skyblue", "hotpink", "darkgreen", "purple"]


class Brick(Turtle):
    def __init__(self, x_cor, y_cor, stretch_l):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=stretch_l)
        self.color(random.choice(BRICK_COLOR))
        self.penup()
        self.goto(x_cor, y_cor)
