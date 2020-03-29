import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

#####################-------------GEOMETRIC TRANSFORMATIONS IN MATRIX LEVEL-----------------#####################

imgsrc = cv2.imread('resource/bflog.png')
height, width, thickness = imgsrc.shape


# resize/scale the image

alpha = cv2.resize(imgsrc, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('alpha', alpha)
cv2.waitKey(0)

apples = cv2.resize(imgsrc, (width*2, height*2), interpolation=cv2.INTER_CUBIC)
cv2.imshow('apples', apples)
cv2.waitKey(0)
cv2.destroyAllWindows()


# translate the image

bravo = np.float32([[1, 0, 20], [0, 1, 100]]) # this is a multiplied matrix
res = cv2.warpAffine(imgsrc, bravo, (width *2, height *2))
cv2.imshow('bravo', res)
cv2.waitKey(0)
cv2.destroyAllWindows()


#rotate the image

#charlie = cv2.getRotationMatrix2D(((width-1)/2.0, (height)/2.0), 90, 1) # set the center of the rotated image
charlie = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
res = cv2.warpAffine(imgsrc, charlie, (height* 2, width* 2))
cv2.imshow('charlie', res)
cv2.waitKey(0)
cv2.destroyAllWindows()


# affine transformation

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

delta = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(imgsrc,delta,(width, height))
plt.subplot(121),plt.imshow(imgsrc),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()


# Perspective transformation

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

echo = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(imgsrc,echo,(300,300))
plt.subplot(121),plt.imshow(imgsrc),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
