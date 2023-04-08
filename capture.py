import time
from picamera import PiCamera
camera = PiCamera()
time.sleep(3)
camera.capture("outsidepic2.jpg")
