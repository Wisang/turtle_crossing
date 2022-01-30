from turtle import Turtle

FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.score = 1
        self.write(f"Level: {self.score}", font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

