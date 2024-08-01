from turtle import Turtle


class LivesBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.live = 4

    def create_board(self):
        self.goto(-350, 200)
        self.write(f"{self.live}/4", align="center", font=("Courier", 25, "normal"))

    def update_live_count(self):
        self.clear()
        self.live -= 1
