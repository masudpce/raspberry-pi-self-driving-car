"""test main"""

import cv2
import utlis

def getLaneCurve(img):
    imgThres = utlis.thresholding(img)
    
    cv2.imshow('Thres', imgThres)
    return None
"""test main"""    
cap = cv2.VideoCapture('vid1.mp4')
while True:
    success, img = cap.read()
    img = cv2.resize(img, (480, 240))
    getLaneCurve(img)
    
    cv2.imshow('vid', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
