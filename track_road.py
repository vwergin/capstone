import cv2
import math
import time
from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

#steering
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100
channel_num = 14
servo7 = servo.Servo(pca.channels[channel_num])

img = cv2.imread("testing1.jpg")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask_img = cv2.inRange(hsv_img, (90, 10, 10), (120, 255, 255))

bottom = img.shape[0]
middle= int(img.shape[1]/2)

M = cv2.moments(mask_img)
cX = int(M["m10"]/M["m00"])
cY = int(M["m01"]/M["m00"])

monarch_filtered = cv2.circle(img, (cX, cY),5,(0,0,255), 2)
print(hsv_img[cX,cY])
print(img[cX, cY])

angle = math.atan((cX-middle)/(cY-bottom))
print(angle)
degrees = angle*180/3.14259
print(degrees)

constant = 2
test = True
while test:
    servo7.angle = 90 + degrees*constant
    time.sleep(1)
    servo7.angle = 90
    test = False 

#cv2.imwrite('monarch_filtered.jpg', monarch_filtered)
