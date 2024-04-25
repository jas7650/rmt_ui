import multiprocessing.queues
import time                            #calling time to provide delays in program
import multiprocessing


class ServoMotorTemp(object):
    def __init__(self, period_us):
        period_us = period_us   # 5000 us
        period = period_us * pow(10, -6)
        frequency_mhz = 1/period
        frequency = 1/period_us
        self.min_duty = round(920/period_us * 100, 2)
        self.max_duty = round(1900/period_us * 100, 2)
        MIN_PULSE_TIME = round((period_us*self.min_duty)/100, 2)
        MAX_PULSE_TIME = round((period_us*self.max_duty)/100, 2)
        print(f"Min Duty Cycle: {self.min_duty}%, Min Pulse Time: {MIN_PULSE_TIME} us")
        print(f"Max Duty Cycle: {self.max_duty}%, Max Pulse Time: {MAX_PULSE_TIME} us")
        self.queue = multiprocessing.Queue()
        p = multiprocessing.Process(target=self.iterate_spots, args=(self.queue, ), daemon=True)
        p.start()


    def set_start(self):
        self.queue.put("start")


    def set_stop(self):
        self.queue.put("stop")


    def iterate_spots(self, queue):
        running = False
        while True:
            if not queue.empty():
                if queue.get() == "start":
                    running = True
                elif queue.get() == "stop":
                    running = False
            if running == True:
                print(f"At max: {time.time()}")
                time.sleep(5)
                print(f"At min: {time.time()}")
                time.sleep(5)



# p = IO.PWM(12,frequency_mhz)
# p.start(0)
# while 1:
#     p.ChangeDutyCycle(MAX_DUTY)
#     time.sleep(10)
#     p.ChangeDutyCycle(MIN_DUTY)
#     time.sleep(10)
