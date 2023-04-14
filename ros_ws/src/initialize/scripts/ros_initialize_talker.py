#!/usr/bin/env python

import rospy
from std_msgs.msg import String 
from std_msgs.msg import UInt8
from std_msgs.msg import Float32

import cv2
import math
import time
from board import SCL, SDA
import busio
import os
from math import cos, sin, pi, floor
from picamera import PiCamera


def initialize_start():
    #camera = PiCamera()

    pub = rospy.Publisher('ready_motor', UInt8, queue_size = 15)
    rospy.init_node('initialize_start',anonymous=True)
    rate = rospy.Rate(4) #4 Hz (measurement 4 times a second)
    ready = 0

    while not rospy.is_shutdown():
        #take a couple photos here and then send the signal that they have been taken
        ready = 1
        rospy.loginfo(ready)
        pub.publish(ready)
        rate.sleep()

if __name__ == '__main__':
    try:
        initialize_start()
    except rospy.ROSInterruptException:
        pass
