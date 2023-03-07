import math
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import time

#channel number of the pwm board (should be channel 15 if using pi hat)
channel_num = 15


i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100


#def Motor_StartUp(pca):
#    print('Starting Motor Start Up Sequence')
#    pca.channels[channel_num].duty_cycle = math.floor(.15*65535)
#    time.sleep(2)
#    pca.channels[channel_num].duty_cycle = math.floor(.2*65535)
#    time.sleep(1)
#    pca.channels[channel_num].duty_cycle = math.floor(.15*65535)
#    time.sleep(1)
#    pca.channels[channel_num].duty_cycle = math.floor(.1*65535)
#    time.sleep(1)
#    pca.channels[channel_num].duty_cycle = math.floor(.15*65535)
#    time.sleep(1)
#    print('Start Up Complete')

def Motor_Speed(pca, percent, channel = channel_num):
    print("motor speed is .156")
    pca.channels[channel].duty_cycle = math.floor(percent*65535)

#Motor_StartUp(pca)

#print('')
#print('Changing Speeds:')
#test = True
#while test:
#    Motor_Speed(pca, .1, channel_num)
#time.sleep(2)
Motor_Speed(pca, .17, channel_num)
time.sleep(3)
#pca.channels[11].duty_cycle = math.floor(.17*65535)
Motor_Speed(pca, .16, channel_num)
time.sleep(3)
#pca.channels[11].duty_cycle = math.floor(.15*65535)
Motor_Speed(pca, .15, channel_num)
time.sleep(3)
