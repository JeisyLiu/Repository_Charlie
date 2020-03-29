import cv2
import numpy as np
from matplotlib import pyplot as plt

# divide red green and blue

imgsrc = cv2.imread('resource/bflog.png')
imgsrc[:, :, (1, 2)] = 0
cv2.imshow('blue', imgsrc)
cv2.waitKey(0)

imgsrc = cv2.imread('resource/bflog.png')
imgsrc[:, :, (0, 2)] = 0
cv2.imshow('green', imgsrc)
cv2.waitKey(0)

imgsrc = cv2.imread('resource/bflog.png')
imgsrc[:, :, (0, 1)] = 0
cv2.imshow('green', imgsrc)
cv2.waitKey(0)

# image filtering in a range
imgsrc = cv2.imread('resource/bflog.png')
range_min = np.array([:, 55, 55])
range_max = np.array([:, 200, 200])
mask = cv2.inRange(imgsrc, range_min, range_max)
filteredimg = cv2.bitwise_and(imgsrc, range_min, range_max)
cv2.imshow('ranged color', filteredimg)
cv2.waitKey(0)

cv2.destroyAllWindows()