from turtle import Turtle

FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-480, 470)
        self.score = 1
        self.write(f"Level: {self.score}", font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("game_over", font=FONT)


