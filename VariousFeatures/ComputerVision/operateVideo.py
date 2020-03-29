import cv2
import numpy as np 
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('resource/niko.avi')
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('resource/output.avi', fourcc, 20.0, (854,  480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # operate every frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame = cv2.flip(frame, 0)
    # write the flipped frame
    out.write(frame)
    cv2.imshow('clipped', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()