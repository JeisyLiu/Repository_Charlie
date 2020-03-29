import cv2
import numpy as np
from matplotlib import pyplot as plt

imgsrc = cv2.imread('resource/pitrain3.png')
graysrc = cv2.cvtColor(imgsrc, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(imgsrc,100,200)
threshs = cv2.adaptiveThreshold(graysrc, 255, 1, 1, 11, 2)

plt.subplot(121),plt.imshow(imgsrc,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

cv2.imshow('edge image', edges)
cv2.waitKey(0)
cv2.imshow('thresh image', threshs)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.show()