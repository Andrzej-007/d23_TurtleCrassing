from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.create_cars()


    def create_cars(self):

        new_car = Turtle(shape='square')
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(280, random.randint(-250, 250))
        self.all_cars.append(new_car)



