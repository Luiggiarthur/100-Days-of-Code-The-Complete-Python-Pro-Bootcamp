from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-220, 260)
        self.ht()
        self.score = 0
        self.score_board()

    def score_board(self):
        self.clear()
        self.score += 1
        self.write(f"Level {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
