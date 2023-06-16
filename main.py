import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time


# TODO 1: Create a 600 x 600 screen, turn animation off, and update screen
screen = Screen()
# turns off animation
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

# this is required for listening to the user keyboard input
screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
car_manager = CarManager()
scoreboard = ScoreBoard()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # TODO 2: Generate cars along y axis and move from left to right
    car_manager.create_car()
    car_manager.move_cars()
    # TODO 3: Check if turtle collides with the car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        # TODO 4: Use move_increment to increase speed of cars
        car_manager.level_up()
        scoreboard.level_up()
    # TODO 5: Keep scoreboard for level

screen.exitonclick()

