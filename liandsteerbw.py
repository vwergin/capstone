

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
    print(data)
 #   time.sleep(1)
#    time.sleep(3)
    firstpoints =[data]
    for i in firstpoints:
        print(i)

        if ( data[i] and data[i + 180]) > 0.0:
            servo7.angle = 120
        else:
            serv07.angle = 95

#        if i > 795:
#            servo7.angle= 90

scan_data = [0]*360

try:
#    print(lidar.info)
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance
#        time.sleep(1)
        dataprocess(scan_data)
        print( "Hello Dumbass")

except KeyboardInterrupt:
    print('Stoping.')
lidar.stop()
lidar.disconnect()
