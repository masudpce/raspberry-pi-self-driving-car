from gpiozero import Robot, Motor
from time import sleep


robot = Robot (left=(4, 14), right=(17, 18))

try:
    while True:
        print("forward 2 sec")
        robot.forward()
        sleep(2)
        print("backward 2 sec")
        robot.backward()
        sleep(2)
except KeyboardInterrupt:
    robot.stop()
    print("\nRobot stopped")
