import numpy as np


class SpeedMotor(object):
    def __init__(self, id, min_speed, max_speed, iterations):
        self.id = id
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.speeds = np.arange(min_speed, max_speed, (max_speed-min_speed)/iterations)
        print(self.speeds)
