import time
from picamera import PiCamera
camera = PiCamera()
time.sleep(3)
camera.capture("testing6.jpg")
