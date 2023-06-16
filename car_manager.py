import random
import turtle
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "blue", "green", "purple", "pink"]

STARTING_MOVE_DISTANCE = 5
INCREMENT_MOVE_DISTANCE = 10
STARTING_COORDINATE_X = 270
FINISH_COORDINATE_X = -270


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle()
            turtle.colormode(255)
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREMENT_MOVE_DISTANCE

