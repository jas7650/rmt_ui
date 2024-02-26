import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program

# Period -> 0.00333333333 seconds -> 3330 microseconds

# Pulses range from 500-2500 us
# 1500 us is centered
# 1000-2000 us is counterclockwise
PERIOD_US = 5000   # 5000 us
PERIOD = PERIOD_US * pow(10, -6)
print(f"Period: {PERIOD_US} us")
FREQUENCY_MHZ = 1/PERIOD
FREQUENCY = 1/PERIOD_US
print(f"Frequency: {FREQUENCY_MHZ} Mhz, {FREQUENCY} Hz")
MIN_DUTY = round(500/PERIOD_US * 100, 2)
MAX_DUTY = round(2500/PERIOD_US * 100, 2)
MIN_PULSE_TIME = round((PERIOD_US*MIN_DUTY)/100, 2)
MAX_PULSE_TIME = round((PERIOD_US*MAX_DUTY)/100, 2)
print(f"Min Duty Cycle: {MIN_DUTY}%, Min Pulse Time: {MIN_PULSE_TIME} us")
print(f"Max Duty Cycle: {MAX_DUTY}%, Max Pulse Time: {MAX_PULSE_TIME}us")



IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(12,IO.OUT)
p = IO.PWM(12,FREQUENCY_MHZ)
p.start(0)
while 1:
    p.ChangeDutyCycle(MAX_DUTY)
    time.sleep(10)
    p.ChangeDutyCycle(MIN_DUTY)
    time.sleep(10)