import cv2
import time
from picamera import PiCamera
camera = PiCamera()

def camerawarm():
    camera.capture("firstroad4.jpg")
#    img = cv2.imread("firstroad4.jpg")
#    time.sleep(1)
    print("yes")
#    cv2.imshow("original", img)
#    cv2.waitKey(1000)
#    cv2.destroyAllWindows()
def track():
#    time.sleep(1)
    camera.capture("firstroad4.jpg")
    img = cv2.imread("firstroad4.jpg")

#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(img.shape)
    img2 = img[614:1024, 0:1280]
#print(img2.shape)
    mask = cv2.inRange(img, (40,10,10), (80,95,95))
    row = 0
    for i in range(100,410):
        white = 0
        for j in range(550, 750):
#        print(mask[i,j])
            if mask[i,j] == 255:
                white = 1
        if white == 0:
            row = i
            break
    print("row",row)
    cv2.imshow('original', img)
    cv2.waitKey(1000)
#time.sleep(10)
    cv2.destroyAllWindows()
#track()
camerawarm()
print("hello")
for i in range(5):
    track()
