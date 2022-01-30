from turtle import Turtle

STARTING_POSITION = (0, -460)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 480


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.move_step = MOVE_DISTANCE
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(self.move_step)

    def speed_up(self):
        self.move_step *= 1.2

    def crossed_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def go_home(self):
        self.goto(STARTING_POSITION)

