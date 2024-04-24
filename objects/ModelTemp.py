import numpy as np
import time

CUT_SERVE = 0
REVERSE_CUT_SERVE = 1
JAM_SERVE = 2
MAX_SPEED = 800
MIN_SPEED = 0

class ModelTemp(object):

    def __init__(self, speed_iterations, spin_iterations):
        self.speed = 0
        self.desired_speed = 0
        self.top_speeds = [(int)(value) for value in np.arange(MIN_SPEED, MAX_SPEED, (MAX_SPEED-MIN_SPEED)/(speed_iterations-1))]
        self.top_speeds.append(800)
        self.bottom_speeds = [(int)(value/2) for value in np.arange(MIN_SPEED, MAX_SPEED/2, (MAX_SPEED/2-MIN_SPEED)/(speed_iterations-1))]
        self.bottom_speeds.append(400)
        self.spins = [(int)(value) for value in np.arange(MIN_SPEED, MAX_SPEED, (MAX_SPEED-MIN_SPEED)/(spin_iterations-1))]
        self.spins.append(800)
        self.spin = 0
        self.desired_spin = 0
        self.mode = CUT_SERVE
        self.modes = [CUT_SERVE, REVERSE_CUT_SERVE, JAM_SERVE]
        self.running = False
        self.speed_iterations = speed_iterations
        self.spin_iterations = spin_iterations
        self.update_text_array()


    def update_text_array(self):
        self.text = []
        labels = ["Mode", "Speed", "Spin", "Status"]
        self.text.append(labels)
        values = [self.getMode(), self.getSpeed(), self.getSpin(), self.getRunning()]
        self.text.append(values)
        up_values = ["Next Mode", "Increase Speed", "Increase Spin", "Start"]
        self.text.append(up_values)
        down_values = ["Previous Mode", "Decrease Speed", "Decrease Spin", "Stop"]
        self.text.append(down_values)


    def getText(self, row, col):
        return f"{self.text[row][col]}"


    def getMode(self):
        if self.mode == CUT_SERVE:
            return "Cut Serve"
        elif self.mode == REVERSE_CUT_SERVE:
            return "Reverse Cut Serve"
        else:
            return "Jam Serve"


    def getSpin(self):
        return self.desired_spin


    def getSpeed(self):
        return self.desired_speed


    def getRunning(self):
        if self.running:
            return "Running"
        else:
            return "Stopped"


    def increase_speed(self):
        if self.desired_speed < self.speed_iterations-1:
            self.desired_speed += 1
        if self.running:
            self.speed = self.desired_speed
        self.update_text_array()


    def decrease_speed(self):
        if self.desired_speed > 0:
            self.desired_speed -= 1
        if self.running:
            self.speed = self.desired_speed
        self.update_text_array()


    def increase_spin(self):
        if self.desired_spin < self.spin_iterations-1:
            self.desired_spin += 1
        if self.running:
            self.spin = self.desired_spin
        self.update_text_array()


    def decrease_spin(self):
        if self.desired_spin > 0:
            self.desired_spin -= 1
        if self.running:
            self.spin = self.desired_spin
        self.update_text_array()


    def increment_mode(self):
        if self.mode < len(self.modes)-1:
            self.mode += 1
        self.update_text_array()
    

    def decrement_mode(self):
        if self.mode > 0:
            self.mode -= 1
        self.update_text_array()


    def print_status(self):
        print("Spin Motor Status")
        self.spin_motor_controller.print_status()
        print("Speed Motor Status")
        self.speed_motor_controller.print_status()


    def set_start(self):
        self.running = True
        while self.speed < self.desired_speed:
            print(f"Speed: {self.speed}, Desired: {self.desired_speed}")
            self.speed += 1
            self.update_text_array()
        while self.spin < self.desired_spin:
            print(f"Spin: {self.spin}, Desired: {self.desired_spin}")
            self.spin += 1
            self.update_text_array()
        self.update_text_array()


    def set_stop(self):
        while self.speed > 0:
            self.speed -= 1
            self.update_text_array()
        while self.spin > 0:
            self.spin -= 1
            self.update_text_array()
        self.running = False
        self.update_text_array()
