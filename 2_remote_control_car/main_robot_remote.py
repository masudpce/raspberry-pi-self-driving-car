import key_press_module as kp
from gpiozero import Robot

robot = Robot(left=(4,14), right=(17, 18))

kp.init()

def main():
    if kp.getKey('UP'):
        robot.forward(1)
    elif kp.getKey('DOWN'):
        robot.backward(1)
    elif kp.getKey('LEFT'):
        robot.left(0.5)
    elif kp.getKey('RIGHT'):
        robot.right(0.5)
    else:
        robot.stop()
        
if __name__ == '__main__':
    while True:
        main()
        