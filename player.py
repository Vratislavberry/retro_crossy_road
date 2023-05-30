from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def reset_position(self):
        self.sety(-280)

    def do_a_step(self):
        self.forward(40)

    def is_winner(self):
        return self.ycor() >= 160