from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(300 - STARTING_MOVE_DISTANCE, 0)

    def play(self):
        self.setheading(180)
        self.forward(MOVE_INCREMENT)
