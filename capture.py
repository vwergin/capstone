import time
import cv2
import math
from picamera import PiCamera
camera = PiCamera()
#time.sleep(3)
#camera.capture("look_at_pic.jpg")
#time.sleep(2)
#camera.resolution = (640, 540)
#camera.capture("outsidep6.jpg")
img = cv2.imread("look_at_pic2.jpg")
#print(img.shape)
img2 = img[math.floor(.01*img.shape[0]):img.shape[0],0:img.shape[1]]
print(img2.shape)
img3 = img[math.floor(.7*img.shape[0]):img.shape[0],0:img.shape[1]] 
mask_img = cv2.inRange(img3, (45, 30, 5), (85, 255, 255))
#cv2.imwrite('grassfill.png', mask_img)
#M = cv2.moments(mask_img)
#cX = int(M["m10"]/M["m00"])
#cY = int(M["m01"]/M["m00"])
#middleimg = cv2.circle(mask_img, (cX, cY), 5, (0,0,255), 2)
#print(cX, cY)
cv2.imshow("og", mask_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

#cv2.imwrite("maskedtest1.jpg")

