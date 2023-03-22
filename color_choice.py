import cv2
import math
h = 512
w = 640
img = cv2.imread("road_pic.jpg")
print(img.shape)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#print(f' H: {img_hsv[h, w, 1]} \t S: {img_hsv[h,w,2]} \t V: {img_hsv[h,w,3]} \n')
colorb = img_hsv[h,w,0]
colorg = img_hsv[h,w,1]
colorr = img_hsv[h,w,2]
print('blue:',  colorb,"green:",  colorg,"red:", colorr)
