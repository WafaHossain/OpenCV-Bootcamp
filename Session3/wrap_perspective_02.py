### Wrap Perspective 
import cv2
import numpy as np

width , height = 250, 350

img = cv2.imread('Resources/cards.jpg')
pts1 = np.float32(([752,118],[1128,265],[540,668],[871,830]))
pts2 = np.float32(([0,0], [width, 0], [0,height], [width, height]))
metrix = cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(img, metrix, (width, height))

cv2.imshow('Cards', img)
cv2.imshow('Cards_wrap', img_out)

cv2.waitKey(0)