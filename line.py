from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(-300, 250)
        self.pendown()
        self.forward(600)
        self.hideturtle()