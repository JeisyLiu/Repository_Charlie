import cv2
import numpy as np
from matplotlib import pyplot as plt

blackboard = np.zeros((512, 512, 3), np.uint8)

#draw line
cv2.line(blackboard, (0, 0), (511, 511), (255, 0, 0), 3)
cv2.imshow('line', blackboard)
cv2.waitKey(0)
cv2.destroyWindow('line')
blackboard = np.zeros((512, 512, 3), np.uint8)

#draw rectangle
cv2.rectangle(blackboard, (128, 128), (384, 284), (0, 255, 0), 2)
cv2.imshow('rectangle', blackboard)
cv2.waitKey(0)
cv2.destroyAllWindows()
blackboard = np.zeros((512, 512, 3), np.uint8)

#draw circle
cv2.circle(blackboard, (256, 255), 42, (0, 0, 255), 4)
cv2.imshow('circle', blackboard)
cv2.waitKey(0)
cv2.destroyAllWindows()
blackboard = np.zeros((512, 512, 3), np.uint8)

#draw ellipse
cv2.ellipse(blackboard, (256, 256), (100, 50), 0, 0, 255, (0, 255, 255), 5)
cv2.imshow('ellipse', blackboard)
cv2.waitKey(0)
cv2.destroyAllWindows()
blackboard = np.zeros((512, 512, 3), np.uint8)

#draw polygon
pts = np.array([[10,50],[20,30],[270,120],[150,110]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(blackboard, [pts], True, (255, 0, 255), 1)
cv2.imshow('polygon', blackboard)
cv2.waitKey(0)
cv2.destroyAllWindows()
blackboard = np.zeros((512, 512, 3), np.uint8)

#draw text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blackboard,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('text', blackboard)
cv2.waitKey(0)
cv2.destroyAllWindows()