#!/usr/bin/env python3
#ROS talking node
#   for camera/picture reading to publish a value

import rospy
from std_msgs.msg import String 
from std_msgs.msg import UInt8
from std_msgs.msg import Float32

#packages from script
#need to double check which ones are actually needed for camera
import cv2
import math
import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from picamera import PiCamera


def cam_data():
    camera = PiCamera()

    pub = rospy.Publisher('sidewalk', Float32, queue_size = 15)
    rospy.init_node('cam_data',anonymous=True)
    rate = rospy.Rate(4) #4 Hz (measurement 4 times a second)
    while not rospy.is_shutdown():
        #get the reading here
        camera.capture("firstroad1.jpg")
        img = cv2.imread("firstroad1.jpg")
        img2 = img[614:1024, 0:1280]
#        hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask_img = cv2.inRange(img2, (40, 10, 10), (80, 95, 95))

        row = 0
        for i in range(100, 410):
            white = 0
            for j in range(550, 750):
                if mask_img[i,j] == 255:
                    white = 1
            if white ==0:
                row = i
                break

        sidewalk = row
        rospy.loginfo(sidewalk)
        pub.publish(sidewalk)
        rate.sleep()

if __name__ == '__main__':
    try:
        cam_data()
    except rospy.ROSInterruptException:
        pass
