import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
cap=cv.VideoCapture(0)
ret,f1=cap.read()
ret,f2=cap.read()
while cap.isOpened():
    diff=cv.absdiff(f1,f2)
    gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),0)
    _,thresh=cv.threshold(blur,120,255,cv.THRESH_BINARY)
    contours,_=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(f1,contours,-1,(0,255,0),2)
    for contour in contours:
        (x,y,w,h)=cv.boundingRect(contour)
        if cv.contourArea(contour)>0:
            continue
        cv.putText(f1,'Motion detected',(30,50),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv.imshow('frame',f1)
    f1=f2
    ret,f2=cap.read()
    if cv.waitKey(1) & 0xFF==27:
        break
cv.destroyAllWindows()
