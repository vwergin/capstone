

#import time
import os
from math import cos, sin, pi, floor
import pygame
from adafruit_rplidar import RPLidar
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import time

# setup servo
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100
channel_num = 14
servo7 = servo.Servo(pca.channels[channel_num])

# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME)


def dataprocess(data):
 #   time.sleep(1)
#    time.sleep(3)
#    firstpoints =[ data[355], data[356], data[357], data[358]]
#    for i in firstpoints:
#        print(i)
#        if i < 795:
#            servo7.angle = 60
#        if i > 795:
#            servo7.angle= 90
     newdata = []
#     for i in range(1,5):
#         print(i)
     j = 0
     for i in range(0,360):
         print(j, data[i])
         j = j + 1

scan_data = [0]*360

try:
#    print(lidar.info)
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance
#        time.sleep(1)
        dataprocess(scan_data)

except KeyboardInterrupt:
    print('Stoping.')
lidar.stop()
lidar.disconnect()
