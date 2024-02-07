from .Mode import Mode


class Model(object):

    def __init__(self, speed_iterations, spin_iterations):
        self.speed = 0
        self.spin = 0
        self.mode = Mode.getValues()[0]
        self.modes = Mode.getValues()
        self.running = False
        self.speed_iterations = speed_iterations
        self.spin_iterations = spin_iterations


    def getMode(self):
        return Mode.getModeString(self.mode)
    

    def getSpin(self):
        return self.spin
    

    def getSpeed(self):
        return self.speed
    

    def getRunning(self):
        return self.running


    def increase_speed(self):
        if self.speed < self.speed_iterations:
            self.speed += 1


    def decrease_speed(self):
        if self.speed > 0:
            self.speed -= 1


    def increase_spin(self):
        if self.spin < self.spin_iterations:
            self.spin += 1


    def decrease_spin(self):
        if self.spin > 0:
            self.spin -= 1


    def increment_mode(self):
        if self.mode < len(self.modes)-1:
            self.mode += 1
    

    def decrement_mode(self):
        if self.mode > 0:
            self.mode -= 1


    def set_start(self):
        self.running = True


    def set_stop(self):
        self.running = False
