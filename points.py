import cv2 as cv
import numpy as np
import matplotlib as plt

img1 = np.zeros((1000, 1500, 3), np.uint8)


def s(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONUP:
        text = str(x)+','+str(y)
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img1, text, (x, y), font, 2, (0, 255, 0), 2)
        cv.circle(img1, (x, y), 3, (255, 255, 0), 2, -1)
        point.append((x, y))
        if len(point) >= 2:
            cv.line(img1, point[-1], point[-2], (0, 255, 255), 2)
        cv.imshow('image', img1)


point = []
cv.imshow('image', img1)
cv.setMouseCallback('image', s)
cv.waitKey(0)
