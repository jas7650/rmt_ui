import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program

# Period -> 0.00333333333 seconds -> 3330 microseconds

# Pulses range from 500-2500 us
# 1500 us is centered
# 1000-2000 us is counterclockwise
FREQUENCY = 400
PERIOD = 1/FREQUENCY
print(PERIOD)
MAX_LEFT = 500/PERIOD
MAX_RIGHT = 2500


IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(12,IO.OUT)
p = IO.PWM(12,300)
p.start(0)
while 1:
    p.ChangeDutyCycle(MAX_LEFT)
    time.sleep(10)
    p.ChangeDutyCycle(MAX_RIGHT)
    time.sleep(10)