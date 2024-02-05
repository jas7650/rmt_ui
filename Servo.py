import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (servo)
GPIO.setup(18, GPIO.IN)  # Sets up pin 18 as an input (button)

duty_cycle = 0
firerate = 0
LOW_THRESHOLD_FIRERATE = 0
HIGH_THRESHOLD_FIRERATE = 9
p = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin (adjust frequency)
p.start(duty_cycle)               # Starts running PWM on the pin and sets it to 0

# Increase servo speed incrementaly based on button press
def increase_firerate():
    global firerate, duty_cycle
    if firerate < HIGH_THRESHOLD_FIRERATE:
        firerate += 1
        duty_cycle = (firerate/9)*85
        p.ChangeDutyCycle(duty_cycle)
        time.sleep(0.25)

# Decrease servo speed incrementaly based on button press
def decrease_firerate():
    global firerate, duty_cycle
    if firerate > LOW_THRESHOLD_FIRERATE:
        firerate -= 1
        duty_cycle = (firerate/9)*85
        p.ChangeDutyCycle(duty_cycle)
        time.sleep(0.25)

    #p.stop()               
    #GPIO.cleanup()         