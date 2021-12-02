import cv2 as cv
import numpy as np
import matplotlib as plt
def nothing(x):
    x
img=np.zeros((512,512,3),np.uint8)
cv.namedWindow('image')
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)

while(1):
    b=cv.getTrackbarPos('B','image')
    g=cv.getTrackbarPos('G','image')
    r=cv.getTrackbarPos('R','image')
    img[:]=[b,g,r]
    text='color : '+(str(b)+','+str(g)+','+str(r))
    font=cv.FONT_HERSHEY_PLAIN
    cv.putText(img,text,(50,50),font,2,(255-r,255-b,255-g),2)
    cv.imshow('image',img)
    cv.waitKey(1)
cv.destroyAllWindows()
