import cv2
import numpy as np

kernel = np.ones((10, 10), np.uint8)

cap = cv2.VideoCapture(0)

while(True):

    gray = cv2.medianBlur(cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY),5)
    frameResized = cv2.resize(gray, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)

    retval, threshold = cv2.threshold(frameResized,254,255,cv2.THRESH_BINARY)

    #erosion = cv2.erode(threshold, kernel, iterations=100)

    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
    dilation = cv2.dilate(opening, kernel, iterations=100)


    circleDetect = cv2.HoughCircles(dilation,
                                    cv2.HOUGH_GRADIENT,
                                    0.5,20,
                                    param1=50,
                                    param2=30,
                                    minRadius=0,
                                    maxRadius=0)

    if circleDetect != None:
        print("Circle There !")

    cv2.imshow('video',threshold)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


