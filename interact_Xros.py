
import math
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import time

import board
import adafruit_mpu6050

from adafruit_motor import servo

import RPi.GPIO as IO
import sys
import argparse
import smbus
from time import sleep
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


### SETUP

## setup for motor
#channel number for motor
channel_num_motor = 15

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 100

## setup for imu
i2c_2 = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c_2)

## setup for steering
channel_num_servo = 14
servo7 = servo.Servo(pca.channels[channel_num_servo])

##setup for encoder
IO.setwarnings(False)
IO.setmode(IO.BCM)
GPIO_num_encoder = 16
IO.setup(GPIO_num_encoder,IO.IN,IO.PUD_UP)



### SEPARATE ELEMENTS

##motor
#   takes in a % (should stay between .15-.18)
def Motor_Speed(pca, percent, channel = channel_num_motor):
    print("motor speed (input):", percent) #might need to fix this
    pca.channels[channel].duty_cycle = math.floor(percent*65535)


## make sure servo is in straight position to begin (need to check this value)
servo_angle = 115
servo7.angle = servo_angle

## initialize all vectors to hold data
gyro_x = []
gyro_y = []
gyro_z = []
acc_x = []
acc_y = []
acc_z = []
servo = []
motor_input = []
encoder_speed = []
encoder_counts = []
times = []

## begin running motor
# start with low motor speed
current_motor_speed = 0.15
time.sleep(1)

start_time = time.time()
times.append(start_time)
cur_time = start_time


test = True
test_encoder = True
time_int = 3 #seconds (how often we take a data point)

while test:
    Motor_Speed(pca, current_motor_speed, channel_num_motor)
    time.sleep(time_int) #wait before checking current_motor_speed to change
    #check speed using encoder function
    #taking last three seconds of data from encoder (find rps)
    speed = observed_speed(encoder_counts[number_encoder-300:number_encoder], time_int)
    print(speed)

    #log all of the values
    times.append(cur_time)
    encoder_speed.append(speed)
    motor_input.append(current_motor_speed)
    servo.append(servo_angle)
    gyro_x.append(f'{mpu.gyro[0]:.2f}')
    gyro_y.append(f'{mpu.gyro[1]:.2f}')
    gyro_z.append(f'{mpu.gyro[2]:.2f}')
    acc_x.append(f'{mpu.acceleration[0]:.2f}')
    acc_y.append(f'{mpu.acceleration[1]:.2f}')
    acc_z.append(f'{mpu.acceleration[2]:.2f}')
    cur_time = time.time()
    #based on the speed, change the current_motor_speed variable
    ## WRITE HERE (call function?)

while test_encoder:
    curr_pin_val = IO.input(GPIO_num_encoder)
    encoder_counts.append(curr_pin_val)
    time.sleep(.01)
    number_encoder = number_encoder+1





## servo steering
# To get the full range of the servo you will likely need to adjust the min_pulse and max_pulse to
# match the stall points of the servo.
# The pulse range is 750 - 2250 by default. This range typically gives 135 degrees of
# range, but the default is to use 180 degrees. You can specify the expected range if you wish:
# for i in range(89,140):
#     servo7.angle = i
#     time.sleep(0.03)
#     print(i)

## encoder
# test_encoder = True
# while test_encoder:
#     curr_pin_val = IO.input(GPIO_num_encoder)
#     print(curr_pin_val)


# ## write to a file
# datafile = open("imudata.txt", 'w')
# for i in range(length):
#     datafile.write(f'{xarray[i]} \t {yarray[i]} \t {zarray[i]} \t {xarray_a[i]} \t {yarray_a[i]} \t {zarray_a[i]} \n')




## PLAN 

# set motor to initial speed (low)
# start collecting encoder data
# calculate actual speed from encoder readings
# set up a signifier to stop increasing motor and change steering once car reaches certain encoder reading
# loop through to increase motor speed every time

# keep track of data (motor input & encoder reading)




# later
# signify start of turn by lidar
    # turn off steering from camera
    # reduce speed of car
    # use accelerometer values to make a turn
        #begin incrementing steering direction
        #signify when turn has almost completed
        #increment steering back to straight
    # turn camera steering back on



#input for the function should be the last certain value of readings 
def observed_speed(vector_encoder_vals, calc_time):
    maxsize = len(vector_encoder_vals)
    #create new vectors to hold data 
    changes = [0]*maxsize
    vals = [0]*maxsize

    #loop through all values in 0/1 vector to find number changes (use last 3 sec?)
    i = 0 
    for dat in vector_encoder_vals:
        #values = dat.split()
        vals[i] = float(dat)
    if (i==0):
        changes[i] =0
    else:
        changes[i] = vals[i] - vals[i-1]
        i = i +1

    #find the total number of changes
    ticks = np.sum(changes)
    speed = ticks/calc_time #rps
    return speed
    




#calculate the average rpm for the wheel for a given dataset
#def find_rpm(dataset):
   #find the transitions of the disk
   #transitions =
   #total_time =  
   #find average rpm
   #cycles_per_sec = transitions/4/total_time
   #rpm = cycles_per_sec*60
   

   #return rpm
