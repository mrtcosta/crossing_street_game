from turtle import Turtle
import random
cores = ["blue", "red", "green", "yellow", "orange"]


class Cars():

    def __init__(self):
        self.little_cars = []


    def create_cars(self):
        r = random.randint(1, 6)
        if r == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(cores))
            new_car.goto(420, random.randint(-250, 250))
            self.little_cars.append(new_car)


    def move_cars(self):
        for car in self.little_cars:
            car.setheading(180)
            car.forward(5)

