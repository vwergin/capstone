import time
import cv2
from picamera import PiCamera
camera = PiCamera()
time.sleep(3)
camera.capture("outsidepic2.jpg")
time.sleep(2)
camera.capture("pictest7.jpg")
img = cv2.imread("pictest7.jpg")
mask_img = cv2.inRange(img, (40, 10, 10), (80, 95,95))
cv2.imwrite('grassfill.png', mask_img)
