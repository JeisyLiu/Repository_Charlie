import matplotlib.pyplot as plt 
import numpy as np
import cv2

imgsrc = cv2.imread('resource/geometric3D.png')
imgcp = imgsrc.copy()

# Harris corner detector

grayimg = cv2.cvtColor(imgsrc, cv2.COLOR_BGR2GRAY)
gray = np.float32(grayimg)

corners = cv2.cornerHarris(gray, 2, 3, 0.04)
destin = cv2.dilate(corners, None)

imgsrc[destin> 0.01*destin.max()] = [200, 126, 0]
cv2.imshow('corner', imgsrc)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Shi-Tomasi image corner detector

shicorners = cv2.goodFeaturesToTrack(grayimg, 25, 0.01, 10)
#shicorners = np.int0(shicorners)
for i in shicorners:
    x, y = i.ravel()
    cv2.circle(imgcp, (x, y), 3, (100, 200, 100),-1)

cv2.imshow('Shi-Tomasi', imgcp)
cv2.waitKey(0)
cv2.destroyAllWindows()