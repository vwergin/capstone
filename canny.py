import cv2
import time

img = cv2.imread("first_road5.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(img.shape)
img2 = img[400:720, 0:1280]
mask = cv2.inRange(img2, (40,10,10), (80,100,100))
t_lower = 150
t_upper = 200
edge = cv2.Canny(mask, t_lower, t_upper, L2gradient = True)
#edge = cv2.Canny(img, t_lower, t_upper)
cv2.imshow('original', mask)
#cv2.imshow('edge', edge)
cv2.waitKey(5000)
#time.sleep(10)
cv2.destroyAllWindows()
