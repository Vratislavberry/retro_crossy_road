from traffic_lane import Traffic_lane
import random

class Traffic_lanes:
    def __init__(self):
        self.lane_num = 3
        self.car_num = 2
        self.min_distance = 80
        self.max_distance = 400
        self.car_speed = 0.2
        self.traffic_lanes = []
        self.create_traffic()

    def create_traffic(self):
        y = -240
        self.traffic_lanes = []
        for _ in range(self.lane_num):
            self.traffic_lanes.append(Traffic_lane(self.car_num, self.min_distance, self.max_distance, self. car_speed, y))
            y += random.choice([40, 80])

    def start_traffic(self):
        for traffic_lane in self.traffic_lanes:
            traffic_lane.start_traffic()

    def is_crashed(self, player):
        for traffic_lane in self.traffic_lanes:
            if traffic_lane.is_crashed(player):
                return True
        return False


    def del_lanes(self):
        for traffic_lane in self.traffic_lanes:
            traffic_lane.del_cars()


    def new_level(self, level):
        level += 1
        if level % 10 == 0:
            self.lane_num += 1

        elif level % 5 == 0:
            self.min_distance -= 5
            self.max_distance -= 10
            self.car_num += 1

        else:
            self.car_speed += 0.05
        self.del_lanes()
        self.create_traffic()




