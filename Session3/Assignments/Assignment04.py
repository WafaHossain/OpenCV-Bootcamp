## Joinining Image

import cv2
import numpy as np

img_lambo = cv2.imread("Resources/lambo.png")
img_robot = cv2.imread("Resources/robot.png")

resized_lambo = cv2.resize (img_lambo, (300, 300))
resized_robot = cv2.resize (img_robot, (300, 300))

img_hor_alt = np.hstack((resized_lambo, resized_robot))
img_var_alt = np.vstack((resized_lambo, resized_robot))

img_hor_lambo = np.hstack((img_lambo, img_lambo))
img_ver_lambo = np.vstack((img_lambo, img_lambo))

img_hor_robot = np.hstack((img_robot, img_robot))
img_ver_robot = np.vstack((img_robot, img_robot))

cv2.imshow("Horizontal Alt", img_hor_alt)
cv2.imshow("Vertical Alt", img_var_alt)

cv2.imshow("Horizontal Lambo", img_hor_lambo)
cv2.imshow("Vertical Lambo", img_ver_lambo)

cv2.imshow("Horizontal Robot", img_hor_robot)
cv2.imshow("Vertical Robot", img_ver_robot)

cv2.waitKey(0)