import numpy as np
from .MotorController import MotorController

CUT_SERVE = 0
REVERSE_CUT_SERVE = 1
JAM_SERVE = 2
MAX_SPEED = 800
MIN_SPEED = 0

class Model(object):

    def __init__(self, speed_iterations, spin_iterations):
        self.speed = 0
        self.speeds = [(int)(value) for value in np.arange(MIN_SPEED, MAX_SPEED, (MAX_SPEED-MIN_SPEED)/(speed_iterations-1))]
        self.speeds.append(800)
        self.spins = [(int)(value) for value in np.arange(MIN_SPEED, MAX_SPEED, (MAX_SPEED-MIN_SPEED)/(spin_iterations-1))]
        self.spins.append(800)
        self.spin = 0
        self.mode = CUT_SERVE
        self.modes = [CUT_SERVE, REVERSE_CUT_SERVE, JAM_SERVE]
        self.running = False
        self.speed_iterations = speed_iterations
        self.spin_iterations = spin_iterations
        self.spin_motor_controller = MotorController(16)
        self.speed_motor_controller = MotorController(17)


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
        print(f"Index: {self.spin}")
        print(f"Spins: {self.spins}")
        return self.spins[self.spin]


    def getSpeedMotor(self):
        print(f"Index: {self.spin}")
        print(f"Speeds: {self.spins}")
        return self.speeds[self.speed]


    def getRunning(self):
        if self.running:
            return "Running"
        else:
            return "Stopped"


    def increase_speed(self):
        if self.speed < self.speed_iterations-1:
            self.speed += 1
            self.speed_motor_controller.setSpeed(1, self.getSpeedMotor())
            self.speed_motor_controller.setSpeed(2, self.getSpeedMotor())


    def decrease_speed(self):
        if self.speed > 0:
            self.speed -= 1
            self.speed_motor_controller.setSpeed(1, self.getSpeedMotor())
            self.speed_motor_controller.setSpeed(2, self.getSpeedMotor())


    def increase_spin(self):
        if self.spin < self.spin_iterations-1:
            self.spin += 1
            self.spin_motor_controller.setSpeed(1, self.getSpinMotor())
            self.spin_motor_controller.setSpeed(2, self.getSpinMotor())


    def decrease_spin(self):
        if self.spin > 0:
            self.spin -= 1
            self.spin_motor_controller.setSpeed(1, self.getSpinMotor())
            self.spin_motor_controller.setSpeed(2, self.getSpinMotor())


    def increment_mode(self):
        if self.mode < len(self.modes)-1:
            self.mode += 1
    

    def decrement_mode(self):
        if self.mode > 0:
            self.mode -= 1


    def set_start(self):
        self.running = True
        self.spin_motor_controller.setSpeed(1, self.getSpinMotor())
        self.spin_motor_controller.setSpeed(2, self.getSpinMotor())
        self.speed_motor_controller.setSpeed(1, self.getSpeedMotor())
        self.speed_motor_controller.setSpeed(2, self.getSpeedMotor())


    def set_stop(self):
        self.running = False
        self.spin_motor_controller.setSpeed(1, 0)
        self.spin_motor_controller.setSpeed(2, 0)
        self.speed_motor_controller.setSpeed(1, 0)
        self.speed_motor_controller.setSpeed(2, 0)
