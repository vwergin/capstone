import cv2
import math
import time
from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

from picamera import PiCamera
camera = PiCamera()

#motor
channel_motor = 15

#steering
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100
channel_num = 14
servo7 = servo.Servo(pca.channels[channel_num])
servo7.angle = 90

def Motor_Speed(pca, percent, channel = channel_motor):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)

count = 1
def tracking():
    camera.capture("testing7.jpg")
    img = cv2.imread("testing7.jpg")
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_img = cv2.inRange(hsv_img, (90, 10, 10), (120, 255, 255))

    bottom = img.shape[0]
    middle= int(img.shape[1]/2)

    M = cv2.moments(mask_img)
    if M["m00"] == 0:
        M["m00"] = 1
    if count ==1:
        cX = 512
        cY = 640
    else:
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])

    monarch_filtered = cv2.circle(img, (cX, cY),5,(0,0,255), 2)
    angle = math.atan((cX-middle)/(cY-bottom))
#    print("Angle:", angle)
    degrees = angle*180/3.141592
#    print("Degrees:", degrees)
    count = count + 1
    constant = 1
    test = True
    while test:
        angle_desired = 90 + degrees*constant
        print("angle desired:", angle_desired)
        if angle_desired < 70:
            print("first")
            servo7.angle = 70
        elif angle_desired > 110:
            print("second")
            servo7.angle = 110
        else:
            print("third")
            servo7.angle = angle_desired
        time.sleep(1)
        servo7.angle = 90
        test = False
#cv2.imwrite('monarch_filtered1.jpg', monarch_filtered)
Motor_Speed(pca, .1525, channel_motor)
time.sleep(.1)
#Motor_Speed(pca, .15, channel_motor)

for i in range(3):
    first = time.time()
    Motor_Speed(pca, .15, channel_motor)
    tracking()
#    time.sleep(.25)
    last = time.time()
    Motor_Speed(pca, .1525, channel_motor)
    print("time:", last-first)
    time.sleep(.1)
Motor_Speed(pca, .15, channel_motor)
