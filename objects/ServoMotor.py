import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program
import multiprocessing


class ServoMotor(object):
    def __init__(self, period_us, min_duty_us, max_duty_us, shot_frequency):
        period_us = 5000   # 5000 us
        period = period_us * pow(10, -6)
        frequency_mhz = 1/period
        self.min_duty = round(min_duty_us/period_us * 100, 2)
        self.max_duty = round(max_duty_us/period_us * 100, 2)
        IO.setwarnings(False)
        IO.setmode (IO.BCM)
        IO.setup(12,IO.OUT)
        self.p = IO.PWM(12,frequency_mhz)
        self.p.start(0)
        self.shot_frequency = shot_frequency


    def start_feeder(self):
        self.process = multiprocessing.Process(target=self.iterate_locations)
        self.process.start()


    def stop_feeder(self):
        if self.process:
            self.process.terminate()


    def iterate_locations(self):
        while 1:
            self.drop_ball()
            print("At max")
            self.load_ball()
            print("At min")
            time.sleep(self.shot_frequency/2)


    def drop_ball(self):
        self.p.ChangeDutyCycle(self.min_duty)
        time.sleep(self.shot_frequency/2)


    def load_ball(self):
        self.p.ChangeDutyCycle(self.max_duty)
        time.sleep(self.shot_frequency/2)
