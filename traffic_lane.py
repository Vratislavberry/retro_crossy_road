from turtle import Turtle
from car import Car
import random


class Traffic_lane:
    def __init__(self, car_num, min_distance, max_distance, car_speed, y):
        self.car_num = car_num
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.car_speed = car_speed
        self.direction = random.choice([0, 180])
        self.set_lane(y)
    def set_lane(self, y):
        self.cars = [Car(direction=self.direction, speed=self.car_speed) for _ in range(self.car_num)]
        x = -320
        for car in self.cars:
            car.sety(y)
            x += random.randint(self.min_distance, self.max_distance)
            car.setx(x)

    def del_cars(self):
        for car in self.cars:
            car.reset()
            car.hideturtle()

    def start_traffic(self):
        for car in self.cars:
            car.move()
            if car.xcor() > 320:
                car.setx(-320)

            elif car.xcor() < -320:
                car.setx(320)

    def is_crashed(self, player):
        for car in self.cars:
            if car.distance(player) < 25:
                return True
        return False

