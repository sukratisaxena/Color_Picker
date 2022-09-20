import cv2
import numpy as np
def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.createTrackbar("Hue min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Sat min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Val max", "Trackbars", 255, 255, empty)

capture = cv2.VideoCapture(0)
capture.set(10, 150)
while True:
    isTrue, frame = capture.read()
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val max", "Trackbars")
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max, v_max])
    mask = cv2.inRange(frameHSV, lower,upper)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow("mask", res)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
