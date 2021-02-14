"""test utlis"""

import cv2
import numpy as np

def thresholding(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l_white = np.array([80, 0, 0])
    u_white = np.array([255, 160, 255])
    mask = cv2.inRange(imgHSV, l_white, u_white)
    return mask
    
