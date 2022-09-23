### Warp Document Assignment 
import cv2
import numpy as np

width , height = 645, 792

img = cv2.imread('Resources/docs.jpg')
pts1 = np.float32(([720,25],[1110,19],[746,560],[1222,546]))
pts2 = np.float32(([0,0], [width, 0], [0,height], [width, height]))
metrix = cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(img, metrix, (width, height))

cv2.imshow('Document', img)
cv2.imshow('Documents_warp', img_out)

cv2.waitKey(0)