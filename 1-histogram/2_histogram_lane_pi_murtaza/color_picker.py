import cv2
import numpy as np

"""
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
"""


def empty():
    """ Null function for trackbar"""
    pass


# Initialize trackbar
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
# trackbar inputs:
# trackbar name, window name, initial value, max value, any null function
cv2.createTrackbar("HUE Min", "HSV", 40, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 160, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 30, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

cap = cv2.VideoCapture('vid1.mp4')
frameCounter = 0

while True:
    frameCounter += 1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0

    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    print(h_min)

    # ========== create mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # any hsv range chosen, gives white for selection and black for exclusion.
    mask = cv2.inRange(imgHsv, lower, upper)  # output is scalar

    # bitwise_and requires 2 src. As our mask is scalar,
    # it does not match with array src, so input as option.
    result = cv2.bitwise_and(img, img, mask=mask)  # outputs with original color

    match_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)   # convert into 3 channels, same as original

    """ If only stack original and result, both are fully visible.
     If 3 is stacked then, last one is cropped from right side.
     All source must have same number of channels"""
    # hStack = np.hstack([img, match_mask, result])
    hStack = np.hstack([img, result])

    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
