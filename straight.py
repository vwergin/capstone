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
servo7.angle = 91
def Motor_Speed(pca, percent, channel = channel_num):
    print(percent)
    pca.channels[channel].duty_cycle = math.floor(percent*65535)

#Motor_StartUp(pca)

#print('')
#print('Changing Speeds:')
test = True
while test:
    print("input a value of .15-.18")
    x = float(input())
    Motor_Speed(pca, x, channel_num)
    time.sleep(.5)
    Motor_Speed(pca, .15, channel_num)
#time.sleep(2)
#Motor_Speed(pca, .16, channel_num)
#pca.channels[11].duty_cycle = math.floor(.17*65535)
#time.sleep(2)
#pca.channels[11].duty_cycle = math.floor(.15*65535)
#Motor_Speed(pca, .15, channel_num)
