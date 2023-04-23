import math
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import time
from adafruit_motor import servo
channel_servo = 14

#channel number of the pwm board (should be channel 15 if using pi hat)
channel_num = 15

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100

servo7 = servo.Servo(pca.channels[channel_servo])
servo7.angle = 92

def Motor_Speed(pca, percent, channel = channel_num):
    print(percent)
    pca.channels[channel].duty_cycle = math.floor(percent*65535)



Motor_Speed(pca, .158, channel_num)
time.sleep(3)
Motor_Speed(pca, .15, channel_num)
