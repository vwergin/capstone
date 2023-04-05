import time
from picamera import PiCamera
camera = PiCamera()
time.sleep(6)
camera.capture("wallpic5.jpg")
