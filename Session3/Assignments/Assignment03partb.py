### Face Detection

import cv2
import numpy as np

haarcascade = "Resources/haarcascade_frontalface_default.xml"

cap = cv2.imread('Resources/lena.png')

            
img = cap

facecascade = cv2.CascadeClassifier(haarcascade)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = facecascade.detectMultiScale(img_gray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img ,(x,y), (x+w,y+h), (246,255,215), 2)
    cv2.imshow("face",img)

cv2.waitKey(0)


