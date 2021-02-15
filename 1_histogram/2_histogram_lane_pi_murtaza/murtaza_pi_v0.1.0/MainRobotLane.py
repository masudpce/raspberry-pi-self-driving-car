""" This file contains gpiozero and movement codes
which is related to Pi.
So can be run in Pi. But can not be run in windows.

Use different maxVal(aka max speed) for battery(0.7) and adapter(1) 

"""
# ========== Imports Start
import cv2

from LaneDetectionModule import getLaneCurve
import WebcamModule
import utlis

import gpiozero_robot

# ========== Imports End
 

# ========== Main Function Start
def main():
    img = WebcamModule.getImg()
    curveVal = getLaneCurve(img, 0)

    # sen = 1.3  # SENSITIVITY  # disabled for simplicity
    
    # lithium battery can deliver high current, so use value lower than 1,
    # adapter delivers very low current(180mA), so use 1(full available speed)
    maxVal = 0.7  # MAX SPEED
    if curveVal > maxVal:
        curveVal = maxVal
    if curveVal < -maxVal:
        curveVal = -maxVal
    print("curve value = " + str(curveVal))
    if curveVal > 0:      # Deadzone, if in this -0.08 to 0.05 then no turning
        # sen = 1.7
        if curveVal < 0.05:
            curveVal = 0
    else:
        if curveVal > -0.08:
            curveVal = 0

    gpiozero_robot.move(curveVal)

# ========== Main Function End


# ========== If this module is run
if __name__ == '__main__':
    intialTrackBarVals = [102, 160, 20, 240]
    utlis.initializeTrackbars(intialTrackBarVals)
    while True:
        main()
        """ 
        To preview, waitKey is necessary.
        bitwise AND will be evaluated first.
        ord() returns unicode number for character.
        """
        if cv2.waitKey(1) & 0xff == ord('q'):
            gpiozero_robot.stopping()
            cv2.destroyAllWindows()
            break
