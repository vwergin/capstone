import time
import cv2
from picamera import PiCamera
camera = PiCamera()
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
channel_num = 15
channel_servo = 14
import math
import busio

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100

servo7 = servo.Servo(pca.channels[channel_servo])
servo7.angle = 92

def Motor_Speed(pca, percent,channel = channel_num):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)
Motor_Speed(pca, .16, channel_num)

time.sleep(1)

first = 0
def take():
    global first
#time.sleep(3)
    camera.capture("zpic" + str(first) + ".jpg")
    time.sleep(.5)
    print("taking photo")
    first = first + 1
#camera.capture("pictest.jpg")
#img = cv2.imread("outsidepic3.jpg")
#print(img.shape)
#img2 = img[400:1024,0:1280] 
#mask_img = cv2.inRange(img2, (40, 10, 10), (70, 255,255))
#cv2.imwrite('grassfill.png', mask_img)
#M = cv2.moments(mask_img)
#cX = int(M["m10"]/M["m00"])
#cY = int(M["m01"]/M["m00"])
#middleimg = cv2.circle(mask_img, (cX, cY), 5, (0,0,255), 2)
#print(cX, cY)
#cv2.imshow("og", middleimg)
#cv2.waitKey(5000)
#cv2.destroyAllWindows()


for i in range(5):
    take()

#pca.channels[channel_num].duty_cycle = math.floor(.15*65535)
Motor_Speed(pca, .15, channel_num)
