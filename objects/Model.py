import numpy as np
import time
from .MotorController import MotorController

CUT_SERVE = 0
REVERSE_CUT_SERVE = 1
JAM_SERVE = 2
MAX_SPEED = 800
MIN_SPEED = 0

class Model(object):

    def __init__(self, speed_iterations, spin_iterations):
        self.speed = 0
        self.current_speed = 0
        self.top_speeds = [(int)(value) for value in np.arange(MIN_SPEED, MAX_SPEED, (MAX_SPEED-MIN_SPEED)/(speed_iterations-1))]
        self.top_speeds.append(800)
        self.bottom_speeds = [(int)(value/2) for value in np.arange(MIN_SPEED, MAX_SPEED/2, (MAX_SPEED/2-MIN_SPEED)/(speed_iterations-1))]
        self.bottom_speeds.append(400)
        self.spins = [(int)(value) for value in np.arange(MIN_SPEED, MAX_SPEED, (MAX_SPEED-MIN_SPEED)/(spin_iterations-1))]
        self.spins.append(800)
        self.spin = 0
        self.current_spin = 0
        self.mode = CUT_SERVE
        self.modes = [CUT_SERVE, REVERSE_CUT_SERVE, JAM_SERVE]
        self.running = False
        self.speed_iterations = speed_iterations
        self.spin_iterations = spin_iterations
        self.spin_motor_controller = MotorController(16)
        self.speed_motor_controller = MotorController(17)
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
        return self.spin


    def getSpeed(self):
        return self.speed


    def getSpinMotor(self):
        if self.mode == CUT_SERVE:
            return self.spins[self.spin]
        elif self.mode == REVERSE_CUT_SERVE:
            return self.spins[self.spin] * -1
        else:
            return 0

    def getSpeedMotorTop(self):
        return self.top_speeds[self.speed]


    def getSpeedMotorBottom(self):
        return self.bottom_speeds[self.speed]


    def getRunning(self):
        if self.running:
            return "Running"
        else:
            return "Stopped"


    def increase_speed(self):
        if self.speed < self.speed_iterations-1:
            self.speed += 1
        self.update_text_array()
        if self.running:
            self.speed_motor_controller.setSpeed(1, -1*self.getSpeedMotorTop())
            self.speed_motor_controller.setSpeed(2, self.getSpeedMotorBottom())



    def decrease_speed(self):
        if self.speed > 0:
            self.speed -= 1
        self.update_text_array()
        if self.running:
            self.speed_motor_controller.setSpeed(1, -1*self.getSpeedMotorTop())
            self.speed_motor_controller.setSpeed(2, self.getSpeedMotorBottom())


    def increase_spin(self):
        if self.spin < self.spin_iterations-1:
            self.spin += 1
        self.update_text_array()
        if self.running:
            self.spin_motor_controller.setSpeed(1, self.getSpinMotor())
            self.spin_motor_controller.setSpeed(2, self.getSpinMotor())


    def decrease_spin(self):
        if self.spin > 0:
            self.spin -= 1
        self.update_text_array()
        if self.running:
            self.spin_motor_controller.setSpeed(1, self.getSpinMotor())
            self.spin_motor_controller.setSpeed(2, self.getSpinMotor())


    def increment_mode(self):
        previous_mode = self.mode
        if self.mode < len(self.modes)-1:
            self.mode += 1
        self.update_text_array()
        if self.running and previous_mode != self.mode:
            self.spin_motor_controller.setSpeed(1, 0)
            self.spin_motor_controller.setSpeed(2, 0)
            time.sleep(1)
            self.spin_motor_controller.setSpeed(1, self.getSpinMotor())
            self.spin_motor_controller.setSpeed(2, self.getSpinMotor())

    

    def decrement_mode(self):
        previous_mode = self.mode
        if self.mode > 0:
            self.mode -= 1
        self.update_text_array()
        if self.running and previous_mode != self.mode:
            self.spin_motor_controller.setSpeed(1, 0)
            self.spin_motor_controller.setSpeed(2, 0)
            time.sleep(1)
            self.spin_motor_controller.setSpeed(1, self.getSpinMotor())
            self.spin_motor_controller.setSpeed(2, self.getSpinMotor())


    def print_status(self):
        print("Spin Motor Status")
        self.spin_motor_controller.print_status()
        print("Speed Motor Status")
        self.speed_motor_controller.print_status()


    def set_start(self):
        self.running = True
        self.update_text_array()
        self.spin_motor_controller.setSpeed(1, self.getSpinMotor())
        self.spin_motor_controller.setSpeed(2, self.getSpinMotor())
        self.speed_motor_controller.setSpeed(1, -1*self.getSpeedMotorTop())
        self.speed_motor_controller.setSpeed(2, self.getSpeedMotorBottom())



    def set_stop(self):
        self.running = False
        self.update_text_array()
        self.spin_motor_controller.setSpeed(1, self.getSpinMotor())
        self.spin_motor_controller.setSpeed(2, self.getSpinMotor())
        self.speed_motor_controller.setSpeed(1, -1*self.getSpeedMotorTop())
        self.speed_motor_controller.setSpeed(2, self.getSpeedMotorBottom())

