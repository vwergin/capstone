import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100
channel_num = 14
servo7 = servo.Servo(pca.channels[channel_num])
steer_ref = 91
servo7.angle = steer_ref

TRIG = 12
ECHO = 11

print("setting up")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, False)
GPIO.setup(ECHO, GPIO.IN)

print("sleeping")
time.sleep(.5)
time_start = time.time()

def read():
    print("reading")
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) ==0:
        start_time = time.time()
    while GPIO.input(ECHO) ==1:
        end_time = time.time()

    total_distance =( (end_time)-(start_time)) *34300
    time_taken = end_time-time_start

    print(f'Distance Away: {total_distance/2 :.2f} cm')
    return total_distance/2, time_taken


while True:
    time.sleep(.25)
    read()

GPIO.cleanup()

