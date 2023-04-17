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
steer_ref = 92
servo7.angle = steer_ref

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

found_pole = 0
ref_row = 1
def callback(data):
    global found_pole
    global ref_row
    global pca
    global channel_motor
    global first_time
    rospy.loginfo(data.data)
    pole = data.data
#    servo7.angle = steer_ref
#   adding time delay in order to get lidar to agree again
    if pole == 1 and found_pole == 1 and time.time() > first_time:
        print("stopping")
        pca.channels[channel_motor].duty_cycle = math.floor(.15*65535)
    elif pole == 1 and found_pole == 0:
        first_time = time.time() + 3
        print("turning")
        servo7.angle = 110
        time.sleep(1.97)
        servo7.angle = steer_ref
#        time.sleep(2)
        found_pole = 1

def motor():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('motor', anonymous=True)

    rospy.Subscriber("pole_detection", UInt8, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    motor()
