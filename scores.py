from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.clear()
        self.penup()
        self.color("black")
        self.goto(-300, 250)
        self.write(f"Level: {self.level}", False, "left", font=("Courier", 25, "normal"))

    def level_up(self):

        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "left", font=("Courier", 25, "normal"))

    def game_over(self):
        self.goto(0, 0)
        with open("highscore.txt") as h:
            self.hs = int(h.read())
            if self.level > self.hs:
                self.hs = self.level
        with open("highscore.txt", "w") as h:
            h.write(str(self.hs))

        self.write(f"        GAME OVER\nYour score:{self.level} Highscore:{self.hs}", False, "center", font=("Courier", 30, "bold"))
