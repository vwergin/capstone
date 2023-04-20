import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

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
    time.sleep(.5)
    read()

GPIO.cleanup()

