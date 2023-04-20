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

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
check=0
first = 1
ref_row = 1
def callback(data):
    global first
    global ref_row
    global check
    global checkpole
    if check==1 and checkpole ==0:
        rospy.loginfo(data.data)
        row = data.data
        i2c = busio.I2C(SCL, SDA)
        pca = PCA9685(i2c)
        pca.frequency = 100
        channel_num = 14
        servo7 = servo.Servo(pca.channels[channel_num])
        steer_ref = 94
        servo7.angle = steer_ref

#        if row < row + 100 or row > row - 100:
#            servo7.angle = steer_ref
#        else:
        if 700 < row<750:
            print("too close")
            servo7.angle = steer_ref -6
            time.sleep(.5)
            servo7.angle = steer_ref
        elif 500<row < 550:
            print("too far")
            servo7.angle = steer_ref + 6
            time.sleep(.5)
            servo7.angle = steer_ref
        else:
            print("just right")
            servo7.angle = steer_ref
        first = first + 1

def check_start(data):
    global check
    check = data.data

def check_pole(data):
    global checkpole
    checkpole = data.data

def steering():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('steering', anonymous=True)

    rospy.Subscriber("sidewalk", Float32, callback)
    rospy.Subscriber("ready_motor", UInt8, check_start)
    rospy.Subscriber("pole_detection", UInt8, check_pole)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    steering()
