import time
from picamera import PiCamera
camera = PiCamera()
time.sleep(4)
camera.capture("wallpic2.jpg")
