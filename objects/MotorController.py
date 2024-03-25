#!/usr/bin/env python3

# This example shows a simple way to control the Motoron Motor Controller.
#
# The motors will stop but automatically recover if:
# - Motor power (VIN) is interrupted
# - A temporary motor fault occurs
# - A command timeout occurs
#
# This program will terminate if it does not receive an acknowledgment bit from
# the Motoron for a byte it has written or if any other exception is thrown by
# the underlying Python I2C library.
#
# The motors will stop until you restart this program if the Motoron
# experiences a reset.
#
# If a latched motor fault occurs, the motors experiencing the fault will stop
# until you power cycle motor power (VIN) or cause the motors to coast.

import time
# import motoron


MAX_ACCELERATION = 100
MAX_DECELERATION = 100


class MotorController(object):
    def __init__(self, address):
        self.address = address
        # mc = motoron.MotoronI2C(address=address)

        # mc.reinitialize()
        # mc.disable_crc()

        # mc.clear_reset_flag()

        # mc.disable_command_timeout()

        # mc.set_max_acceleration(1, MAX_ACCELERATION)
        # mc.set_max_deceleration(1, MAX_DECELERATION)
        # mc.set_speed(1, 0)

        # mc.set_max_acceleration(2, MAX_ACCELERATION)
        # mc.set_max_deceleration(2, MAX_DECELERATION)
        # mc.set_speed(2, 0)

        # mc.set_max_acceleration(3, MAX_ACCELERATION)
        # mc.set_max_deceleration(3, MAX_DECELERATION)
        # mc.set_speed(3, 0)
        # self.mc = mc


    def setSpeed(self, motor_num, speed):
        # print(f"Address: {self.address}, Motor: {motor_num}, Speed: {speed}")
        # self.mc.set_speed(motor_num, speed)
        time.sleep(0.005)
