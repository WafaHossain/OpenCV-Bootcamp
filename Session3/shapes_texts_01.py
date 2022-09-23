# Shape and text
import cv2
import numpy as np 

img = np.zeros((720, 1440, 3), np.uint8)
print(img.shape)

img[:] = 80,100,255 #BGR 0,0,0

# Create a line
cv2.line(img, (0,0), (300,400), (0,255,0), 3)
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 3)

# Creating a rectangle
cv2.rectangle(img, (20,50), (400,150), (0,0,255), 3)
cv2.rectangle(img, (20,50), (400,150), (0,0,255), cv2.FILLED) #color filed rectangle

# making a Circle
cv2.circle(img, (200,200), 50, (128,0,128), 3)

### Enter Texts 
cv2.putText(img, 'OpenCV is boring', (250,100), cv2.FONT_HERSHEY_COMPLEX, 2, (128,0,128), 1)


cv2.imshow('Image', img)
cv2.waitKey(0)