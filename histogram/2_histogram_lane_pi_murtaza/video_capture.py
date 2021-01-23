import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('my_hunki_punky_bnW', gray)
    """

    cv2.imshow('my_color_cam', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):   # Pressing q will exit the program.
        break

cap.release()
cv2.destroyAllWindows()