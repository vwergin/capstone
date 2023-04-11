import time
import math

from board import SCL, SDA
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

channel_motor = 15

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100
channel_num = 14

servo7 = servo.Servo(pca.channels[channel_num])

#set the initial angle of the tires
servo7.angle = 93.5


def Motor_Speed(pca, percent, channel = channel_motor):
    pca.channels[channel].duty_cycle = math.floor(percent*65535)

def turn():
    #use keyboard input as trigger for turn to start
    servo7.angle = 120

def straight():
    #use keyboard input as trigger for back to straight
    servo7.angle = 93.5


Motor_Speed(pca, .165, channel_motor)
x = input("hit enter when ready to turn") 
if x == "":
    turn()
    start_time = time.time()

#section for testing the timing
#y = input("hit enter when ready to go straight") 
#if y=="":
 #   straight()
 #   end_time = time.time()
#print(end_time-start_time)
#time.sleep(1)

#section for hard coded time
time_turn = 0.820
time.sleep(time_turn)
straight()
time.sleep(1)


Motor_Speed(pca, .15, channel_motor)


