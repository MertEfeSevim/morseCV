import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (cap.isOpened()):

    _,frame=cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    retval, threshold = cv2.threshold(blur,254,255,cv2.THRESH_BINARY)

    cv2.imshow('threshold',threshold)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()