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
import pygame
from adafruit_rplidar import RPLidar
#found_poles = 0

def lidar_data():
    PORT_NAME = '/dev/ttyUSB0'
    lidar = RPLidar(None, PORT_NAME)


    pub = rospy.Publisher('pole_detection', UInt8, queue_size = 15)
    rospy.init_node('lidar_data',anonymous=True)
    #rate = rospy.Rate(4) #4 Hz (measurement 4 times a second)

#    found_poles = 0

    while not rospy.is_shutdown():
        #get the reading here
        scan_data = [0]*360
        for  scan in lidar.iter_scans():
            for (_,angle,distance) in scan:
                scan_data[min([359, floor(angle)])] = distance

            #looking for the first time we get a reading in the range of the pole
            ref_point = scan_data[90]
            if 1200 < ref_point < 2200:
                pole =  1
            else:
                pole = 0
            #found_poles = found_poles + pole


            rospy.loginfo(pole)
            pub.publish(pole)
            #rate.sleep()
if __name__ == '__main__':
    try:
        lidar_data()
    except rospy.ROSInterruptException:
        pass


