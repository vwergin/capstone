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
        img2 = img[500:1024,0:1280]
#        hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask_img = cv2.inRange(img2, (40, 10, 10), (70, 255, 255))

        M = cv2.moments(mask_img)
        if M["m00"] ==0:
            M["m00"] = 1
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])

        sidewalk = cX
        rospy.loginfo(sidewalk)
        pub.publish(sidewalk)
        rate.sleep()

if __name__ == '__main__':
    try:
        cam_data()
    except rospy.ROSInterruptException:
        pass
