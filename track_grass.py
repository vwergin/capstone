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
servo7.angle = 94

def Motor_Speed(pca, percent, channel = channel_motor):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)
first = 1
def tracking():
    global first
    camera.capture("testing7.jpg")
    img = cv2.imread("testing7.jpg")
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_img = cv2.inRange(hsv_img, (50, 10, 10), (70, 255, 255))

    bottom = img.shape[0]
    middle= int(img.shape[1]/2)

    M = cv2.moments(mask_img)
    if M["m00"] == 0:
        M["m00"] = 1
    cX = int(M["m10"]/M["m00"])
    cY = int(M["m01"]/M["m00"])

# do 1024 - 665 = 360
# middle is 609
# good distance is 665
# this for loop is for one horizontal line
    counter = 0
    for i in range(600, 680):
#        counter = 0
#        for j in range(620, 660):
        if 50 <=  hsv_img[612,i, 0] <= 70:
            if 10 <= hsv_img[612, i, 1] <= 255:
                if 10 <= hsv_img[612, i, 2] <= 255:
                    counter = counter + 1
#    print("count", counter)

# this is vertical line
    vert = []
    counter2 = 0
    for i in range(610, 750):
        if 50 <= hsv_img[i, 620, 0] <= 70:
            if 10 <= hsv_img[i, 620, 1] <= 255:
                if 10 <= hsv_img[i, 620, 2] <= 255:
                    vert.append("1")
        else:
            vert.append("0")
    print(vert)
    vert.reverse()
    print("last index", vert.index("1"))
    digit = vert.index("1")

    dist = 1024-cY
    print("dist", dist)
# middle is 83 ish, if index is less than 80, too close, turn right, 
# if greater than 80, too far, turn left
    if first == 1:
        servo7.angle = 94
    else:
        if dist < 750:
            servo7.angle = 100
            time.sleep(.25)
            servo7.angle = 94
        elif dist > 800:
            servo7.angle = 92
            time.sleep(.25)
            servo7.angle = 94
        else:
            servo7.angle = 94
    first = first + 1
    print(first)
#    monarch_filtered = cv2.circle(img, (cX, cY),5,(0,0,255), 2)
#    cv2.imwrite('grass_filtered2.png', monarch_filtered)
    print("middle", cX, cY)

#Motor_Speed(pca, .16, channel_motor)
#time.sleep(.1)
#tracking()
for i in range(4):
#    first = time.time()
#    Motor_Speed(pca, .15, channel_motor)
    tracking()
    time.sleep(1)
#    last = time.time()
#    Motor_Speed(pca, .1525, channel_motor)
#    print("time:", last-first)
#    time.sleep(.1)

#Motor_Speed(pca, .15, channel_motor)
