from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self, direction=0, speed=0.01):
        super().__init__()
        self.shape("square")
        r, g, b = (random.randint(0, 255) for _ in range(3))
        self.color(r, g, b)
        self.setheading(direction)
        self.penup()
        self.shapesize(stretch_len=2)
        self.speed = speed

    def move(self):
        self.forward(self.speed)
