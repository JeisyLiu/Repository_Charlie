import cv2

facedata = cv2.CascadeClassifier('haar/face.xml')
trsrc = cv2.imread('../../resource/me.jpg', cv2.IMREAD_COLOR)

gray = cv2.cvtColor(trsrc, cv2.COLOR_BGR2GRAY)
faces = facedata.detectMultiScale(gray, 1.1, 2)
l, t, w, h = faces[0]
cv2.rectangle(trsrc, (l, t), (l + w, t + h), (0, 0, 255), thickness= 5)

cv2.imshow("tor", trsrc)

cv2.waitKey(0)
cv2.destroyAllWindows()

