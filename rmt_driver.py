from objects.SpeedMotor import SpeedMotor

def main():
    speed_motors = []
    for i in range(4):
        speed_motors.append(SpeedMotor(i, 0, 10, 10))



if __name__ == "__main__":
    main()
