import time
import cv2
from picamera import PiCamera
camera = PiCamera()
#time.sleep(3)
#camera.capture("outsidepi3.jpg")
#time.sleep(2)
#camera.capture("pictest.jpg")
img = cv2.imread("xxpic3.jpg")
print(img.shape)
#print(img.shape)
img2 = img[600:1080,0:1980]
mask_img = cv2.inRange(img2, (10, 10, 10), (60, 255,255))
#cv2.imwrite('grassfill.png', mask_img)
#M = cv2.moments(mask_img)
#cX = int(M["m10"]/M["m00"])
#cY = int(M["m01"]/M["m00"])
#middleimg = cv2.circle(mask_img, (cX, cY), 5, (0,0,255), 2)
#print(cX, cY)
cv2.imshow("og", mask_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
