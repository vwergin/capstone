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
servo7.angle = 93.5

def Motor_Speed(pca, percent, channel = channel_motor):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)
first = 1
def tracking():
    global first
    camera.capture("first_road" + str(first) + ".jpg")
    img = cv2.imread("first_road" + str(first) + ".jpg")
    print(img.shape)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(hsv_img.shape)
    hsv_img2 = hsv_img[500:1000, 600:650]
#    print(hsv_img2.shape)
    mask_img = cv2.inRange(hsv_img2, (2, 10, 10), (25, 255, 255))
    mask_blur = cv2.blur(mask_img, (5,5))
    th, thresh = cv2.threshold(mask_blur, 200, 255, cv2.THRESH_BINARY)

    bottom = img.shape[0]
    middle= int(img.shape[1]/2)

    M = cv2.moments(mask_img)
    if M["m00"] == 0:
        print("no center detected")
        M["m00"] = 1
    cX = int(M["m10"]/M["m00"])
    cY = int(M["m01"]/M["m00"])

    for i in range(690, 720):
        for j in range(600, 650):
            print(i, hsv_img[i, j, 0], hsv_img[i,j,1], hsv_img[i,j,2])
# do 1024 - 665 = 360
# middle is 609
# good distance is 665
# this for loop is for one horizontal line
# this is vertical line
    if cX == 0:
        dist = 870
        print("sure")
    else:
        dist = 1024-cY
    print("dist", dist)
# middle is 83 ish, if index is less than 80, too close, turn right, 
# if greater than 80, too far, turn left
    if first == 1 or first ==2:
       servo7.angle = 93.5
    else:
        if dist < 860:
            print("too close")
#93
            servo7.angle = 87
            time.sleep(.25)
            servo7.angle = 93.5
        elif dist > 880:
            print("too far")
            servo7.angle = 100
            time.sleep(.25)
            servo7.angle = 93.5
        else:
            print("just right")
            servo7.angle = 93.5
    first = first + 1
#    print(first)
#    monarch_filtered = cv2.circle(hsv_img2, (cX, cY),5,(0,0,255), 2)
#    cv2.imwrite('grass_filtered13.png', monarch_filtered)
    print("middle", cX, cY)

#Motor_Speed(pca, .16, channel_motor)
#time.sleep(.1)
#tracking()
for i in range(3):
#    first = time.time()
#    Motor_Speed(pca, .15, channel_motor)
    tracking()
#    time.sleep(2)
#    last = time.time()
#    Motor_Speed(pca, .1525, channel_motor)
#    print("time:", last-first)
#    time.sleep(.1)

#Motor_Speed(pca, .15, channel_motor)

