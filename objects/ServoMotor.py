# import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program
import multiprocessing


class ServoMotor(object):
    def __init__(self, period_us, min_duty_us, max_duty_us, shot_frequency):
        self.run = False
        period_us = 5000   # 5000 us
        period = period_us * pow(10, -6)
        frequency_mhz = 1/period
        self.min_duty = round(min_duty_us/period_us * 100, 2)
        self.max_duty = round(max_duty_us/period_us * 100, 2)
        # IO.setwarnings(False)
        # IO.setmode (IO.BCM)
        # IO.setup(12,IO.OUT)
        # self.p = IO.PWM(12,frequency_mhz)
        # self.p.start(0)
        self.shot_frequency = shot_frequency
        self.queue = multiprocessing.Queue()


    def start_feeder(self):
        print("Starting")
        self.run = True
        self.process = multiprocessing.Process(target=self.iterate_locations, args=(self.queue,))
        self.process.start()


    def stop_feeder(self):
        print("Stopping")
        self.run = False
        self.queue.put(False)
        if self.process != None:
            self.process.terminate()


    def iterate_locations(self, queue):
        value = True
        while value:
            print("At max")
            self.drop_ball()
            print("At min")
            self.load_ball()
            time.sleep(self.shot_frequency/2)
            print("Checking queue")
            if not queue.empty():
                print("Queue not empty")
                if queue.get() == False:
                    value = False


    def drop_ball(self):
        # self.p.ChangeDutyCycle(self.min_duty)
        time.sleep(self.shot_frequency/2)


    def load_ball(self):
        # self.p.ChangeDutyCycle(self.max_duty)
        time.sleep(self.shot_frequency/2)
