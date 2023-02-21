import lgpio as IO
import time
import sys
import argparse
import busio
import smbus
from time import sleep
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import math

#IO.setwarnings(False)
IO.exceptions = False
#IO.setmode(IO.BCM)
h = IO.gpiochip_open(0)


GPIO_num = 16
#IO.setup(GPIO_num,IO.IN,IO.PUD_UP)


while True:
    curr_pin_val = IO.gpio_read(h, GPIO_num)
    print(curr_pin_val)
