import time
import cv2
from picamera import PiCamera
camera = PiCamera()
#time.sleep(3)
camera.capture("outsidep5.jpg")
#time.sleep(2)
camera.resolution = (640, 540)
camera.capture("outsidep6.jpg")
img = cv2.imread("outsidepic3.jpg")
#print(img.shape)
img2 = img[400:1024,0:1280] 
mask_img = cv2.inRange(img2, (40, 10, 10), (70, 255,255))
#cv2.imwrite('grassfill.png', mask_img)
M = cv2.moments(mask_img)
cX = int(M["m10"]/M["m00"])
cY = int(M["m01"]/M["m00"])
middleimg = cv2.circle(mask_img, (cX, cY), 5, (0,0,255), 2)
print(cX, cY)
#cv2.imshow("og", middleimg)
#cv2.waitKey(5000)
#cv2.destroyAllWindows()
