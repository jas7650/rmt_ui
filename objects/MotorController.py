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
import motoron


MAX_ACCELERATION = 300
MAX_DECELERATION = 300


class MotorController(object):
    def __init__(self, address):
        self.address = address
        mc = motoron.MotoronI2C(address=address)
        # Reset the controller to its default settings, then disable CRC.  The bytes for
        # each of these commands are shown here in case you want to implement them on
        # your own without using the library.
        mc.reinitialize()
        mc.disable_crc()

        # Clear the reset flag, which is set after the controller reinitializes and
        # counts as an error.
        mc.clear_reset_flag()
        mc.clear_motor_fault_unconditional()

        # By default, the Motoron is configured to stop the motors if it does not get
        # a motor control command for 1500 ms.  You can uncomment a line below to
        # adjust this time or disable the timeout feature.
        # mc.set_command_timeout_milliseconds(1000)
        mc.disable_command_timeout()

        # Configure motor 1
        mc.set_max_acceleration(1, MAX_ACCELERATION)
        mc.set_max_deceleration(1, MAX_DECELERATION)
        mc.set_speed(1, 0)

        # Configure motor 2
        mc.set_max_acceleration(2, MAX_ACCELERATION)
        mc.set_max_deceleration(2, MAX_DECELERATION)
        mc.set_speed(2, 0)

        # Configure motor 3
        mc.set_max_acceleration(3, MAX_ACCELERATION)
        mc.set_max_deceleration(3, MAX_DECELERATION)
        mc.set_speed(3, 0)
        self.mc = mc


    def print_status(self):
        print(self.mc.get_status_flags())


    def setSpeed(self, motor_num, speed):
        print(f"Address: {self.address}, Motor: {motor_num}, Speed: {speed}")
        self.mc.set_speed(motor_num, speed)
        time.sleep(0.25)
