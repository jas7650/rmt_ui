import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program


class ServoMotor(object):
    def __init__(self, period_us, left_time_us, right_time_us, sleep_time):
        period_us = period_us   # 5000 us
        period = period_us * pow(10, -6)
        frequency_mhz = 1/period
        self.drop_duty = round(left_time_us/period_us * 100, 2)
        self.get_duty = round(right_time_us/period_us * 100, 2)
        IO.setwarnings(False)
        IO.setmode (IO.BCM)
        IO.setup(12,IO.OUT)
        self.p = IO.PWM(12,frequency_mhz)
        self.p.start(0)
        self.sleep_time


    def drop_ball(self):
        print("Dropping Ball")
        self.p.ChangeDutyCycle(self.drop_duty)
        time.sleep(self.sleep_time)


    def get_ball(self):
        print("Getting Next Ball")
        self.p.ChangeDutyCycle(self.get_duty)
        time.sleep(self.sleep_time)
