from turtle import Screen
from turtle_dona import Turtle_Game
from cars import Cars
from scores import Scoreboard
import time



# SCREEN
screen = Screen()
screen.bgcolor("white")
screen.setup(height=600, width=800)
screen.tracer(0)



score = Scoreboard()
donatello = Turtle_Game()
cars = Cars()


# KEYS
screen.listen()
screen.onkeypress(fun=donatello.turtle_walk, key="Up")


# GAME
is_on = True

time_delay = 0.1

while is_on:
    time.sleep(time_delay)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    for car in cars.little_cars:
        if car.distance(donatello) < 20:
            score.game_over()
            is_on = False


    if donatello.ycor() > 280:
        donatello.level_up()
        time_delay *= 0.5
        score.level_up()


screen.exitonclick()