#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt8
from std_msgs.msg import Float32

#need to check these
import cv2
import math
import time
from board import SCL, SDA
import busio
import os
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

channel_motor = 15
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100
channel_num = 14
servo7 = servo.Servo(pca.channels[channel_num])
steer_ref = 93
servo7.angle = steer_ref

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

found_pole = 0
ref_row = 1
count = 0
def callback1(data):
    global channel_motor
    global pca
    global count
    rospy.loginfo(data.data)
    ready = data.data
    if ready > 0 and count ==0:
        print("start going")
        pca.channels[channel_motor].duty_cycle = math.floor(.158*65535)
        count = count + 1
    x = input("type enter to stop motor ")
    if x == "":
        pca.channels[channel_motor].duty_cycle = math.floor(.15*65535)

def start():
    rospy.init_node('start', anonymous = True)
    rospy.Subscriber("ready_motor", UInt8, callback1)
    rospy.spin()
if __name__ == '__main__':
    start()
