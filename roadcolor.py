import cv2
import math
import numpy
blue = []
green = []
red = []
img = cv2.imread("road_pic.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
for i in range(400,620):
    for j in range(560, 740):
       # img = cv2.imread("road_pic.jpg")
        #print(img.shape)
      #  img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#print(f' H: {img_hsv[h, w, 1]} \t S: {img_hsv[h,w,2]} \t V: {img_hsv[h,w,3]} \n')
        colorb = img_hsv[i,j,0]
        blue.append(colorb)
        colorg = img_hsv[i,j,1]
        green.append(colorg)
        colorr = img_hsv[i,j,2]
        red.append(colorr)
#print('blue:',  colorb,"green:",  colorg,"red:", colorr)
print("blue:", numpy.mean(blue))
print("green:", numpy.mean(green))
print("red:", numpy.mean(red))
