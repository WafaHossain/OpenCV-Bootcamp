### Resizing image
import cv2
# img = cv2.imread('Resources/lena.png')
# print(img.shape)
# resized_img = cv2.resize (img, (300, 300))
# print(resized_img.shape)
# cv2.imshow('output', img)
# cv2.imshow('Resized output', resized_img)
# cv2.waitKey(0)

### Cropping image
img = cv2.imread('Resources/lena.png')
crop_img = img[0:200, 0:100]
cv2.imshow('output', img)
cv2.imshow('Crop_ooutput', crop_img)
cv2.waitKey(0)