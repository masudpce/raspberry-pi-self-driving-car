"""
Commented out three portions related to
movement for running in pc:
import, motor def, movement
"""
# from gpiozero import Robot
from LaneDetectionModule import getLaneCurve
import WebcamModule
import utlis
import cv2
 
##################################################
# my_car = Robot(left=(4,14), right=(17,18) )
##################################################


def main():
    img = WebcamModule.getImg()
    curveVal = getLaneCurve(img, 2)

    # sen = 1.3  # SENSITIVITY  # disabled for simplicity
    print("curve value = "+ str(curveVal))
    maxVal = 0.3  # MAX SPEED
    if curveVal > maxVal: curveVal = maxVal
    if curveVal < -maxVal: curveVal = -maxVal
    if curveVal > 0:      # Deadzone, if in this -0.08 to 0.05 then no turning
        # sen = 1.7
        if curveVal < 0.05: curveVal = 0
    else:
        if curveVal > -0.08: curveVal = 0
    """
    #============== Movement
    #motor.move(0.20,-curveVal*sen,0.05)
    if curveVal == 0 : 
        my_car.forward()
    elif curveVal > 0.0 :
        my_car.right(curveVal)
    elif curveVal < 0.0 :
        my_car.left(curveVal)
    """

 
if __name__ == '__main__':
    intialTrackBarVals = [102, 160, 20, 240]
    utlis.initializeTrackbars(intialTrackBarVals)
    while True:
        main()
        # To preview
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
