#ROS talking node
#   for camera/picture reading to publish a value

import rospy
from std_msgs.msg import String 
from std_msgs.msg import UInt8

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


def acc_data():

#need to go through and define all values here 

    pub = rospy.Publisher('acc', Uint8, queue_size = 15)
    rospy.init_node('cam_data',anonymous=True)
    rate = rospy.rate(4) #4 Hz (measurement 4 times a second)
    while not rospy.is_shutdown():
        #get the reading here
        camera.capture("test_image.jpg")
        img = cv2.imread("test_image.jpg")
        hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask_img = cv2.inRange(hsv_img, (20, 10, 10), (40, 255, 255))

        bottom = img.shape
        bottom = img.shape[0]
        middle= int(img.shape[1]/2)

        M = cv2.moments(mask_img)
        if M["m00"] == 0:
            M["m00"] = 1
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])

        angle = math.atan((cX-middle)/(cY-bottom))
        #    print("Angle:", angle)
        degrees = angle*180/3.141592
        #    print("Degrees:", degrees)

        sidewalk = degrees
        rospy.loginfo(sidewalk)
        pub.publish(sidewalk)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        cam_data()
    except rospy.ROSInterruptException:
        pass