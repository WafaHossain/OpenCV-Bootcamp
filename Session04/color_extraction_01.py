### Color extraction Assignment

import cv2
import numpy as np

path = "Resources/lena.png"

def empty():
    pass

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBar", 84, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBar", 1, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 45, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBar", 105, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 37, 255, empty)
cv2.createTrackbar("Val Max", "TrackBar", 15, 255, empty)

while True:
    img = cv2.imread(path)
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBar")

    print(h_min, h_max, s_min, s_max, v_min, v_max)
    
    lower = np.array([105,45,45])  
    upper = np.array([255,255,255]) 
    mask = cv2.inRange(img_HSV, lower, upper)
    img_result = cv2.bitwise_and(img, img,mask= mask)


    cv2.imshow("Original", img)
    cv2.imshow("HSV img", img_HSV)
    cv2.imshow("mask img", mask)
    cv2.imshow("img_result", img_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break