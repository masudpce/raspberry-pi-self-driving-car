""" This file contains gpiozero and movement codes
which is related to Pi.
So can be run in Pi. But can not be run in windows."""

from gpiozero import Robot
from LaneDetectionModule import getLaneCurve
import WebcamModule
import utlis
import cv2
 
##################################################
my_car = Robot(left=(4,14), right=(17,18) )
##################################################


def main():
    img = WebcamModule.getImg()
    curveVal = getLaneCurve(img, 2)

    # sen = 1.3  # SENSITIVITY  # disabled for simplicity
    maxVAl = 1.0  # MAX SPEED
    if curveVal > maxVAl: curveVal = maxVAl
    if curveVal < -maxVAl: curveVal = -maxVAl
    print("curve value = "+ str(curveVal))
    if curveVal > 0:      # Deadzone, if in this -0.08 to 0.05 then no turning
        # sen = 1.7
        if curveVal < 0.05: curveVal = 0
    else:
        if curveVal > -0.08: curveVal = 0

    #============== Movement
    #motor.move(0.20,-curveVal*sen,0.05)
    if curveVal == 0 : 
        my_car.forward()
    elif curveVal > 0.0 :
        my_car.right(curveVal)
    elif curveVal < 0.0 :
        my_car.left(curveVal)


 
if __name__ == '__main__':
    intialTrackBarVals = [102, 160, 20, 240]
    utlis.initializeTrackbars(intialTrackBarVals)
    while True:
        main()
        # To preview
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
