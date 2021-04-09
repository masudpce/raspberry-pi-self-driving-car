"""
Motor pins are hardcoded in this module.
The car will take very small turn and correct direction. Then go forward.
Test to find out usable minimum values for speed and duration.
Usable function: 
    move()
    stopping()
"""

from gpiozero import Robot
import time

# ========== Minimum speed and duration values start
# todo: Need to find out by testing. Use minimum usable value
min_turn_speed = 0.4
turn_duration = 0.0

min_forward_speed = 0.5
forward_duration = 0.1
# ========== Minimum speed and duration values end

# ========== Motor pin definition
robot = Robot(left=(4, 14), right=(17, 18))


def move(curve):
    """
    Runs the motors to go forward or turn left/right 
    @ min speed and for min duration.
    Then stops the car.
    
    input: curve value
    output: prints direction of movement
    """
    if curve > 0.0:
        robot.right(min_turn_speed)
        print("           right\n")
        time.sleep(turn_duration)

    elif curve < 0.0:
        robot.left(min_turn_speed)
        time.sleep(turn_duration)
        print("left\n")

    elif curve == 0:
        robot.forward(min_forward_speed)
        print("          forward          \n")
        time.sleep(forward_duration)

    robot.stop()


def stopping():
    """stops the car"""
    robot.stop()
