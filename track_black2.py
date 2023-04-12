import cv2
import time
from picamera import PiCamera
camera = PiCamera()

camera.capture("first_road4.jpg")
img = cv2.imread("first_road4.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(img.shape)
img2 = img[400:720, 0:1280]
print(img2.shape)
mask = cv2.inRange(img2, (40,10,10), (80,95,95))
row = 0
for i in range(180,215):
    white = 0
    for j in range(550, 750):
#        print(mask[i,j])
        if mask[i,j] == 255:
            white = 1
    if white == 0:
        row = i
        break
print("row",row)
cv2.imshow('original', mask)
cv2.waitKey(5000)
#time.sleep(10)
cv2.destroyAllWindows()
