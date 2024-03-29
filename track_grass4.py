import cv2
import math
import time
from board import SCL, SDA
import busio
import os
from math import cos, sin, pi, floor
import pygame
from adafruit_rplidar import RPLidar
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from picamera import PiCamera
camera = PiCamera()
from threading import Thread

#motor
channel_motor = 15

#lidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME)

#steering
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100
channel_num = 14
servo7 = servo.Servo(pca.channels[channel_num])
steer_ref = 92
servo7.angle = steer_ref

system1 = True
def Motor_Speed(pca, percent, channel = channel_motor):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)

should_track = True
first = 1
ref = 0
def tracking():
    while should_track:
        global first
        global ref
        camera.capture("first_road1.jpg")
        img = cv2.imread("first_road1.jpg")
#        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#        hsv_img2 = hsv_img[614:1024, 0:1280] # crop bottom with grass
        print(img.shape)
        img2 = img[614:1024, 0:1280]
        mask_img = cv2.inRange(img2, (40, 10, 10), (80, 95, 95))
#    mask_blur = cv2.blur(mask_img, (5,5))
#    th, thresh = cv2.threshold(mask_blur, 200, 255, cv2.THRESH_BINARY)

    # find center
#        M = cv2.moments(mask_img)
#        if M["m00"] == 0:
#            print("no center detected")
#            M["m00"] = 1
#        cX = int(M["m10"]/M["m00"])
#        cY = int(M["m01"]/M["m00"])

        row = 0
        for i in range(50, 410):
            white = 0
            for j in range(550, 750):
                if mask_img[i,j] == 255:
                    white = 1
            if white ==0:
                row = i
                break
        print("row", row)
        dist = 1024 - row
        print("dist", dist)

    # steering based on ref distance
        if first == 1:
            servo7.angle = steer_ref
        else:
            if dist < 830:
                print("too close")
                servo7.angle = 86
                time.sleep(.25)
                servo7.angle = steer_ref
            elif dist > 850:
                print("too far")
                servo7.angle = 98
                time.sleep(.25)
                servo7.angle = steer_ref
            else:
                print("just right")
                servo7.angle = steer_ref
        first = first + 1
#    monarch_filtered = cv2.circle(hsv_img2, (cX, cY),5,(0,0,255), 2)
#    cv2.imwrite('grass_filtered13.png', monarch_filtered)

found_pole = 0
def dataprocess(data):
    print("hello")
    global found_pole
    global should_track
    ref_point = data[90]
    if 2000 < ref_point < 2500:
        print("ref point", ref_point)
        should_track = False
        servo7.angle = 120 # change values of angle and sleep time
        time.sleep(1.1)
        servo7.angle = steer_ref
        should_track = True
        time.sleep(1)
        found_pole = 1

def dataprocess2(data):
    global found_pole
    ref_point = data[90]
    if 300 < ref_point < 500:
        Motor_Speed(pca, .15, channel_motor)
    found_pole = 2


def datascan():
    scan_data = [0]*360
    global found_pole
    try:
        for scan in lidar.iter_scans():
            for (_,angle,distance) in scan:
                scan_data[min([359, floor(angle)])] = distance
#            if found_pole > 0:
#                dataprocess2(scan_data)
#            else:
#                dataprocess(scan_data)
    except KeyboardInterrupt:
         print("stopping")
    lidar.stop()
    lidar.disconnect()

def stop():
#    global system1
    x = input("hit enter when to stop")
    if x =="":
        Motor_Speed(pca, .15, channel_motor)
        system1 = False
        print("this should stop")

while system1:
#    if found_pole <2:
#    Thread(target = tracking).start()
    Thread(target = datascan).start()
#    Thread(target = stop).start()
#    else:
#        Motor_Speed(pca, .15, channel_motor)
#        break
print("all done")




#Motor_Speed(pca, .16, channel_motor)
#tracking()
#for i in range(3):
#    first_time = time.time()
#    tracking()
#    time.sleep(.25)
#    last_time = time.time()
#    print("time:", last_time-first_time)

#Motor_Speed(pca, .15, channel_motor)

