import cv2
import numpy as np
from matplotlib import pyplot as plt

colorspacelist = [i for i in dir(cv2) if i.startswith('COLOR_')]
print (colorspacelist)

imgsrc = cv2.imread('resource/pitrain3.png', cv2.IMREAD_UNCHANGED)
grayimg = cv2.cvtColor(imgsrc, cv2.COLOR_BGR2GRAY)
cv2.imshow('unchanged', imgsrc)
cv2.waitKey(0)
cv2.imshow('gray', grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows()