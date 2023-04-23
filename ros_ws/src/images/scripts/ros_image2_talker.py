#!/usr/bin/env python
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
#    camera.resolution=(640,540)
#    camera.capture("firstroad1.jpg")
#    time.sleep(1)
    pub = rospy.Publisher('sidewalk', Float32, queue_size = 15)
    rospy.init_node('cam_data',anonymous=True)
    rate = rospy.Rate(4) #4 Hz (measurement 4 times a second)
    while not rospy.is_shutdown():
        #get the reading here
        camera.capture("firstroad2.jpg")
        img = cv2.imread("firstroad2.jpg")
#        img2 = img[500:1024, 0:1280]
        print(img.shape)

        img2 = img[math.floor(.7*img.shape[0]):img.shape[0],0:img.shape[1]]
#        hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask_img = cv2.inRange(img2, (50, 10, 10), (70, 255, 255))
 #       mask_img = cv2.inRange(img2, (20, 10, 10), (70, 255, 255))

        row = 0
        for i in range(0, mask_img.shape[0]):
            whites = 0
            for j in range(1,mask_img.shape[1]): # range(400,800): #mask_img.shape[1]):
                if mask_img[i,j] == 255:
                    whites = whites + 1
            if whites < 150:
                row = i
                break
            print(whites,i)    

        sidewalk = row
        rospy.loginfo(sidewalk)
        pub.publish(sidewalk)
        rate.sleep()

if __name__ == '__main__':
    try:
        cam_data()
    except rospy.ROSInterruptException:
        pass
