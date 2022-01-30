import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

game_is_on = True
sleep_time = 0.1

while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    player.move()
    car_manager.play()
    if player.crossed_finish_line():
        player.go_home()
        player.speed_up()

screen.exitonclick()
