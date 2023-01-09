from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=("Courier",80, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=("Courier", 80, "normal"))

    def count_score_l(self):
        self.clear()
        self.score_l += 1
        self.update_score()

    def count_score_r(self):
        self.clear()
        self.score_r += 1
        self.update_score()
