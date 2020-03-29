import cv2
import numpy as np
from matplotlib import pyplot as plt

def donothing(x):
    pass

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('trackbar')

cv2.createTrackbar('R', 'trackbar', 0, 255, donothing)
cv2.createTrackbar('G', 'trackbar', 0, 255, donothing)
cv2.createTrackbar('B', 'trackbar', 0, 255, donothing)
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'trackbar', 0, 1, donothing)

while(1):
    cv2.imshow('trackbar', img)
    key = cv2.waitKey(1) & 0xFF
    if (key == 27):
        break
    
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')
    s = cv2.getTrackbarPos(switch, 'trackbar')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()