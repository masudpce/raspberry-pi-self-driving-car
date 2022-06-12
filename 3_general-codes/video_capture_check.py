"""video_capture_check.py
This module is used to check if camera is working. 
Also it shows common useful functions when using opencv module. 
"""

import cv2

cap = cv2.VideoCapture(0)     # 0 = first camera device.

while True:
    ret, frame = cap.read()
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('black n white preview', gray)
    """
    cv2.imshow('original preview', frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):   # Pressing q will exit the program.
        break

cap.release()                 # gentle handling
cv2.destroyAllWindows()       # clean exit