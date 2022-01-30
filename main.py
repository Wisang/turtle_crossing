import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=1000)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

game_is_on = True
sleep_time = 0.1

screen.listen()

screen.onkey(player.move, "u")
screen.onkeypress(player.move, "u")

cars = car_manager.get_cars()

game_is_on = True

while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    car_manager.play()

    if player.crossed_finish_line():
        player.go_home()
        player.speed_up()
        scoreboard.score_up()

    for car in cars:
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
