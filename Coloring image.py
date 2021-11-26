import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img1=cv.imread(r"C:\Users\Hp\Desktop\Programming files\Computer Vision\OpenCV\data\lena.jpg") 
plt.title("Original Image")
plt.imshow(img1)
img2=np.zeros_like(img1)
img2[:,:,1]=img1[:,:,1]
plt.imshow(img2)
#cv.imwrite(0)
plt.show()
