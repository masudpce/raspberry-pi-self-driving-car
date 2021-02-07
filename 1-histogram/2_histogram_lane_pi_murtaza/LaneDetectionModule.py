import cv2
import numpy as np
import utlis

curveList = []
avgVal = 10


def getLaneCurve(img, display=2):
    """ 
    display options:
        0: Nothing will be displayed in the window
        1: Show only resulted image (marked by detected lane)
        2: Shows full pipeline with six frames stacked from different phases
    Total 5 steps
    """
    imgCopy = img.copy()
    imgResult = img.copy()

    # ============ STEP 1
    """ Produce mask; min and max hsv value range is hardcoded in utlis module."""
    imgThres = utlis.thresholding(img)

    # ============ STEP 2
    """Region of interest will be warped and resized
     to the size of original image"""
    hT, wT, c = img.shape     # the order is Height, width and channel/depth
    points = utlis.valTrackbars()      # trackbar initialized with values in main function

    # order of W and H can be arbitrary but must be consistent across all functions
    # wT is width Target and hT is height Target
    imgWarp = utlis.warpImg(imgThres, points, wT, hT) 
    imgWarpPoints = utlis.drawPoints(imgCopy, points)

    # ============ STEP 3
    middlePoint, imgHist = utlis.getHistogram(imgWarp, display=True, minPer=0.5, region=4)
    curveAveragePoint, imgHist = utlis.getHistogram(imgWarp, display=True, minPer=0.9)
    curveRaw = curveAveragePoint - middlePoint

    # ============ STEP 4
    curveList.append(curveRaw)
    if len(curveList) > avgVal:
        curveList.pop(0)
    curve = int(sum(curveList) / len(curveList))

    # ============ STEP 5
    if display == 0:
        # Do nothing
        pass
    else:
        # if display = 0, then display related nothing will execute 
        # in any other case, it will execute

        # Inverse warped image to get original unwarped portion
        imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT, inv=True)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)   # convert to 3 channel to match in stacking
        imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
        midY = 450
        cv2.putText(imgResult, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
        cv2.line(imgResult, (wT // 2, midY), (wT // 2 + (curve * 3), midY), (255, 0, 255), 5)
        cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY - 25), (wT // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
        for x in range(-30, 30):
            w = wT // 20
            cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),
                     (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
        # fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        # cv2.putText(imgResult, 'FPS ' + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230, 50, 50), 3);
        if display == 1:
            cv2.imshow('Result', imgResult)
        elif display == 2:
            imgStacked = utlis.stackImages(0.7, ([img, imgWarpPoints, imgWarp],
                                                 [imgHist, imgLaneColor, imgResult]))
            cv2.imshow('ImageStack', imgStacked)

    # ========= NORMALIZATION
    curve = curve / 100
    if curve > 1:
        curve = 1
    if curve < -1:
        curve = -1

    return curve


if __name__ == '__main__':
    # cap = cv2.VideoCapture('vid1.mp4')
    cap = cv2.VideoCapture(0)   # use camera
    intialTrackBarVals = [102, 160, 20, 240]
    utlis.initializeTrackbars(intialTrackBarVals)

    frameCounter = 0
    while True:
        # continuous loop
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0

        success, img = cap.read()
        img = cv2.resize(img, (480, 240))
        curve = getLaneCurve(img, display=2)
        print("curve = " + str(curve))
        # cv2.imshow('Vid',img)
        # cv2.waitKey(1)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
