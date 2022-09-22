  ###Reading an image

import cv2

# img = cv2.imread('Resources/lena.png')
# print(img.shape)
# cv2.imshow('Lena is here', img)
# cv2.waitKey(0)

  ###Reading videos
# cap = cv2.VideoCapture('Resources/elon.mp4')
# while True:
#     success, img = cap.read()
#     print(img.shape)
#     cv2.imshow('Output', img)

#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break

cap = cv2.VideoCapture(0)

cap.set(3, 640) #The number '3' to set width
cap.set(4, 480) #The number '3' to set height
while True:
    success, img = cap.read()
    # print(img.shape)
    cv2.imshow('Output', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
