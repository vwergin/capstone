#!/usr/bin/env python
#ROS talking node
#   for camera/picture reading to publish a value

import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt8
from std_msgs.msg import Float32
import RPi.GPIO as GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)

#TRIG = 12
#ECHO = 11

#GPIO.setup(TRIG, GPIO.OUT)
#GPIO.output(TRIG, False)
#GPIO.setup(ECHO, GPIO.IN)

#packages from script
#need to double check which ones are actually needed for camera
#import cv2
#import math
import time
#from board import SCL, SDA
#import busio
#from adafruit_motor import servo
#from adafruit_pca9685 import PCA9685
#from picamera import PiCamera

time.sleep(.5)
time_start = time.time()

def cam_data():
#    camera = PiCamera()
#    camera.capture("firstroad1.jpg")
#    time.sleep(1)
    pub = rospy.Publisher('sidewalk', Float32, queue_size = 15)
    rospy.init_node('cam_data',anonymous=True)
    rate = rospy.Rate(4) #4 Hz (measurement 4 times a second)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    TRIG = 12
    ECHO = 11

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.output(TRIG, False)
    GPIO.setup(ECHO, GPIO.IN)


    while not rospy.is_shutdown():
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) ==0:
            start_time = time.time()
        while GPIO.input(ECHO) == 1:
            end_time = time.time()

        total_distance = ((end_time)- (start_time))*34000

        distance = total_distance/2
        sidewalk = distance
        rospy.loginfo(sidewalk)
        pub.publish(sidewalk)
        rate.sleep()

if __name__ == '__main__':
    try:
        cam_data()
    except rospy.ROSInterruptException:
        pass
