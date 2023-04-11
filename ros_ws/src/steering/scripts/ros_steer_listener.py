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


def callback(data):

    rospy.loginfo(data.data)

    i2c = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c)
    pca.frequency = 100
    channel_num = 14
    servo7 = servo.Servo(pca.channels[channel_num])
    servo7.angle = 94

    constant = 1
    test = True
    while test:
        angle_desired = 94 - data.data*constant
        print("angle desired:", angle_desired)
        if angle_desired < 84:
            print("first")
            servo7.angle = 84
        elif angle_desired > 104:
            print("second")
            servo7.angle = 104
        else:
            print("third")
            servo7.angle = angle_desired
        time.sleep(1)
        servo7.angle = 94
        test = False

    
def steering():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('steering', anonymous=True)

    rospy.Subscriber("sidewalk", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    steering()
