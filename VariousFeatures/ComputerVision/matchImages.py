import cv2
import matplotlib.pyplot as plt
import numpy as np

#single image matching
imgsrc = cv2.imread('resource/chauchar.png')
imgcp = imgsrc.copy()

target = cv2.imread('resource/window.png')
targetcp = target.copy()

height, width, thick = target.shape

imgcp = cv2.Canny(imgcp, 100, 200)
target = cv2.Canny(target, 100, 200)

res = cv2.matchTemplate(imgcp, target, cv2.TM_CCOEFF)
# the third argument is started with TM_
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0]+ width, top_left[1] + height)

cv2.rectangle(imgsrc, top_left, bottom_right, (0, 0, 255), 2)

cv2.imshow('window', targetcp)
cv2.imshow('bf1', imgsrc)
cv2.waitKey(0)
cv2.destroyAllWindows()

#below are stuff of the multiply detecting
# the notice
background = np.zeros((200, 1100), np.uint8)
text = 'next contain is multiply detecting'
cv2.putText(background, text, (1, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('notice', background)
cv2.waitKey(0)
cv2.destroyWindow('notice')


#the matching of image
img_rgb = cv2.imread('resource/pokemon.jpg')
template = cv2.imread('resource/pokemontar.jpg',0)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('matching', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('res.png',img_rgb)