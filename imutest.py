
import time
import board
import adafruit_mpu6050

i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)

xarray = [];
yarray = [];
zarray = [];
xarray_a = [];
yarray_a =[];
zarray_a=[];
length = 10;

for i in range(length):
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print("Temperature: %.2f C" % mpu.temperature)
    print("")
    time.sleep(1)
    xarray.append(f'{mpu.gyro[0]:.2f}')
    yarray.append(f'{mpu.gyro[1]:.2f}')
    zarray.append(f'{mpu.gyro[2]:.2f}')
    xarray_a.append(f'{mpu.acceleration[0]:.2f}')
    yarray_a.append(f'{mpu.acceleration[1]:.2f}')
    zarray_a.append(f'{mpu.acceleration[2]:.2f}')

#datafile = open("imudata.txt", 'w')
#for i in range(length):
#    datafile.write(f'{xarray[i]} \t {yarray[i]} \t {zarray[i]} \t {xarray_a[i]} \t {yarray_a[i]} \t {zarray_a[i]} \n')
