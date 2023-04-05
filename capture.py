import time
from picamera import PiCamera
camera = PiCamera()
time.sleep(5)
camera.capture("wallpic4.jpg")
