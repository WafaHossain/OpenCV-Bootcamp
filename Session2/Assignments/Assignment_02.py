import cv2

cap = cv2.VideoCapture('Resources/elon.mp4')
while True:
    success, img = cap.read()
    crop_img = img[0:300, 0:300]
    cv2.imshow('Cropped_Output', crop_img)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break