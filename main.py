import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame=cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0,0,255],dtype=np.uint8)
    upper = np.array([0,0,255],dtype=np.uint8)

    mask = cv2.inRange(hsv,lower,upper)

    print(np.all(mask[mask == 255]))

    cv2.imshow('mask',mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

"""
if cv2.countNonZero(mask) > 29700:
        print("Motion")
    else:
        print("No Motion")
"""

