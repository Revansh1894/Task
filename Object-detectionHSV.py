import cv2 as cv
import numpy as np
import matplotlib as plt
def nothing(x):
    # print(x)
    x
cap=cv.VideoCapture(0)
cv.namedWindow('t')
cv.createTrackbar('lh','t',0,255,nothing)
cv.createTrackbar('ls','t',0,255,nothing)
cv.createTrackbar('lv','t',0,255,nothing)
cv.createTrackbar('uh','t',0,255,nothing)
cv.createTrackbar('us','t',0,255,nothing)
cv.createTrackbar('uv','t',0,255,nothing)

while(1):
    _,img=cap.read()
    #img=cv.imread(r'C:\Users\Hp\Desktop\Programming files\Computer Vision\OpenCV\data\HappyFish.jpg')
    lh=cv.getTrackbarPos('lh','t')
    ls=cv.getTrackbarPos('ls','t')
    lv=cv.getTrackbarPos('lv','t')
    uh=cv.getTrackbarPos('uh','t')
    us=cv.getTrackbarPos('us','t')
    uv=cv.getTrackbarPos('uv','t')
    img1=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    lb=np.array([lh,ls,lv])
    up=np.array([uh,us,uv])
    mask=cv.inRange(img1,lb,up)
    hsv=cv.bitwise_and(img,img,mask=mask)
    cv.imshow('img',hsv)
    cv.imshow('image',img1)
    cv.waitKey(1)
cap.release()
cv.destroyAllWindows()
