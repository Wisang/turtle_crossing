import time
from distutils.command.install import key
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

screen.listen()

screen.onkey(player.move, "u")

while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    car_manager.play()

    if player.crossed_finish_line():
        player.go_home()
        player.speed_up()
        scoreboard.score_up()

screen.exitonclick()
