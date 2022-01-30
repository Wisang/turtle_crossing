from turtle import Turtle
import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 20


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []

        for i in range(NUMBER_OF_CARS):
            self.cars.append(Car())

    def play(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(MOVE_INCREMENT)
            if car.xcor() < -280:
                car.goto(480, random.randint(-480, 480))

    def get_cars(self):
        return self.cars
