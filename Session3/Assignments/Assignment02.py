# Shape and text
import cv2
import numpy as np 

img = np.zeros((720, 1440, 3), np.uint8)
img[:] = 80,100,255 #BGR 0,0,0

## Making a Triangle
cv2.ellipse(img,(700,300),(150,300),100,200,180,(255,0,215),-1)

# Making a triangle part2
pts = [(50, 50), (300, 190), (400, 10)]
cv2.polylines(img, np.array([pts]), True, (246,205,55), 5)

## Making an ellipse
cv2.ellipse(img,(500,400),(150,300),0,0,360,(1,255,100),-1)


### Enter Texts 
cv2.putText(img, 'I love OpenCV', (250,100), cv2.FONT_HERSHEY_COMPLEX, 2, (128,0,128), 1)



cv2.imshow('Image', img)
cv2.waitKey(0)