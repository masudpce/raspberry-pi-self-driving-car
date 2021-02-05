
from gpiozero import Robot
from LaneDetectionModule import getLaneCurve
import WebcamModule
 
##################################################
my_car = Robot(left=(4,14), right=(17,18) )
##################################################
 
def main():
 
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img,1)
    maxVAl= 0.3 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl

    #sen = 1.3  # SENSITIVITY
    #print(curveVal)
    if curveVal>0:      # Deadzone, if in this -0.08 to 0.05 then no turning
        #sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    
    #============== Movement
    #motor.move(0.20,-curveVal*sen,0.05)
    if curveVal == 0 : 
        my_car.forward()
    elif curveVal > 0.0 :
        my_car.right(curveVal)
    elif curveVal < 0.0 :
        my_car.left(curveVal)
    
    #cv2.waitKey(1)   # Necessary if we want to preview
     
 
if __name__ == '__main__':
    while True:
        main()
