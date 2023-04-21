import time
import cv2
from picamera import PiCamera
camera = PiCamera()
import math
from math import floor
from board import SCL, SDA
import busio
import os
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
channel_motor = 15

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100
channel_servo = 14
servo7 = servo.Servo(pca.channels[channel_servo])
steer_ref = 92
servo7.angle = steer_ref

#time.sleep(3)
camera.capture("outsidepi3.jpg")
time.sleep(2)

def Motor_Speed(pca, percent, channel = channel_motor):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)

#Motor_Speed(pca, .16, channel_motor)

ref = 160

for i in range(20):
#def track():
#    global ref
#    camera = PiCamera()
#    camera.capture("test2.jpg")
    camera.capture("zzpic2.jpg")
#    time.sleep(.1)
    img = cv2.imread("zzpic2.jpg")
    print(img.shape)
#print(img.shape)
    img2 = img[math.floor(.7*img.shape[0]):img.shape[0],0:img.shape[1]]
    print(img2.shape)
    mask_img = cv2.inRange(img2, (10, 10, 10), (60, 255,255))
#cv2.imwrite('grassfill.png', mask_img)
#M = cv2.moments(mask_img)
#cX = int(M["m10"]/M["m00"])
#cY = int(M["m01"]/M["m00"])
#middleimg = cv2.circle(mask_img, (cX, cY), 5, (0,0,255), 2)
#print(cX, cY)
    row = 0
    for i in range(0,mask_img.shape[0]):
        whites = 0
        for j in range(1, mask_img.shape[1]):
            if mask_img[i,j] == 255:
                whites = whites + 1
        if whites < 150:
           # print(whites)
            row = i
#            print("first row", row)
            break
#        print("whites", whites, i)
    print("row", row)
#    camera.close()
    if row < ref -10:
        print("too far")
        servo7.angle = steer_ref + 10
        time.sleep(.5)
        servo7.angle = steer_ref
    elif row > ref + 10:
        print("too close")
        servo7.angle = steer_ref - 10
        time.sleep(.5)
        servo7.angle = steer_ref
    else:
        print("just right")
        servo7.angle = steer_ref

#cv2.imshow("og", mask_img)
#cv2.waitKey(5000)
#cv2.destroyAllWindows()
#
#for i in range (100):
#3   track()

#Motor_Speed(pca, .15, channel_motor)
