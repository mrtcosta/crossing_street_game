from turtle import Turtle



class Turtle_Game(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.fillcolor("black")
        self.setheading(90)
        self.goto(0, -280)

    def turtle_walk(self):
        new_y = self.ycor() + 15
        self.goto(0, new_y)


    def level_up(self):
        self.goto(0, -280)


