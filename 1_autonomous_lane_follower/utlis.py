""" Utils.py  
This module includes all extra functions used in LaneDetectionModule.py .
There are 8 functions in it.
"""


import cv2
import numpy as np


def thresholding(img):
    """Gives mask for specific color
    Chosen color is hardcoded.
    input: original RGB image
    output: scalar(single channel) mask, (1 for matched pixels, 0 for otherwise.)
    """
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([80, 0, 0])
    upperWhite = np.array([255, 160, 255])
    maskWhite = cv2.inRange(imgHsv, lowerWhite, upperWhite)
    return maskWhite


def warpImg(img, points, w, h, inv=False):
    """change to birds eye view
    input: img    = src
           points = the points which will be warped
           w      = final width
           h      = final height
    point is specified as first width then height, like (w,h)=(0,0)
    Order:top-left, top-right, bottom-left, bottom-right
    """
    pts1 = np.float32(points)       # src points
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])      # dst points
    if inv:
        matrix = cv2.getPerspectiveTransform(pts2, pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarp = cv2.warpPerspective(img, matrix, (w, h))
    return imgWarp


def nothing(a):
    """This null function is required for trackbar function"""
    pass


def initializeTrackbars(intialTracbarVals, wT=480, hT=240):
    """
    wT is width Target and hT is Height target
    Point is specified as first width then height, like (w,h)=(0,0)
    Order:top-left, top-right, bottom-left, bottom-right
    """
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0], wT // 2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2], wT // 2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT, nothing)


def valTrackbars(wT=480, hT=240):
    """
    point is specified as first width then height, like (w,h)=(0,0)
    Order:top-left, top-right, bottom-left, bottom-right
    """
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT - widthTop, heightTop),
                         (widthBottom, heightBottom), (wT - widthBottom, heightBottom)])
    return points


def drawPoints(img, points):
    """Used to draw four points to indicate Region of Interest"""
    for x in range(4):
        cv2.circle(img, (int(points[x][0]), int(points[x][1])), 15, (0, 0, 255), cv2.FILLED)
    return img


def getHistogram(img, minPer=0.1, display=False, region=1):
    if region == 1:
        histValues = np.sum(img, axis=0)
    else:
        histValues = np.sum(img[img.shape[0] // region:, :], axis=0)

    # print(histValues)
    maxValue = np.max(histValues)
    minValue = minPer * maxValue

    indexArray = np.where(histValues >= minValue)
    basePoint = int(np.average(indexArray))
    # print(basePoint)

    if display:
        imgHist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for x, intensity in enumerate(histValues):
            cv2.line(imgHist, (x, img.shape[0]), (x, img.shape[0] - intensity // 255 // region), (255, 0, 255), 1)
            cv2.circle(imgHist, (basePoint, img.shape[0]), 20, (0, 255, 255), cv2.FILLED)
        return basePoint, imgHist

    return basePoint


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver
