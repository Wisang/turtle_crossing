from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.goto(random.randint(-480, 480), random.randint(-400, 480))
