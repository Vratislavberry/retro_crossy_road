from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.setposition(-270, 250)
        self.write(f"level: {self.level} highscore: {self.get_highscore()}", font=("Courier", 25, "normal"))

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"level: {self.level} highscore: {self.get_highscore()}", font=("Courier", 25, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game Over", align="center" ,font=("Courier", 25, "normal"))

    def get_highscore(self):
        with open("highscore.txt") as file:
            highscore = int(file.read())
        return highscore

    def new_highscore(self):
        previous_highscore = int(self.get_highscore())
        return self.level > previous_highscore

    def update_highscore(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.level))
        self.print_highscore()

    def print_highscore(self):
        self.clear()
        self.write(f"New highscore: {self.get_highscore()}", font=("Courier", 25, "normal"))

