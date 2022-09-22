import cv2

cap = cv2.VideoCapture('Resources/elon.mp4')
while True:
    success, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale_Output', img_gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break