# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:22:16 2023

@author: MerveOZKAN
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt


global mask

def nothing(x):
    pass


def hsv_value(img,hsv):
    
    cv2.namedWindow("window")
    cv2.resizeWindow("window", 800,500)
    
    cv2.createTrackbar("Hue min","window",0,179,nothing)
    cv2.createTrackbar("Hue max", "window",179,179,nothing)
    
    cv2.createTrackbar("Saturation min", "window", 0,255,nothing)
    cv2.createTrackbar("Saturation max", "window", 255,255,nothing)
    
    cv2.createTrackbar("Value min", "window", 0,255,nothing)
    cv2.createTrackbar("Value max", "window", 255,255,nothing)
    
    
    
    while(1):
        

         H_min = cv2.getTrackbarPos("Hue min","window")  
         H_max = cv2.getTrackbarPos("Hue max","window") 
         S_min = cv2.getTrackbarPos("Saturation min","window")
         S_max = cv2.getTrackbarPos("Saturation max","window")
         V_min = cv2.getTrackbarPos("Value min","window")
         V_max = cv2.getTrackbarPos("Value max","window")
         print("lower:",H_min,S_min,V_min)
         print("upper:",H_max,S_max,V_max)
         lower = np.array([H_min,S_min,V_min])
         upper = np.array([H_max,S_max,V_max])
         
         mask = cv2.inRange(hsv, lower, upper)
         
         cv2.imshow("window",img)
         cv2.imshow("hsv",mask)
         
         
         if cv2.waitKey(5) == ord("q"):
             break
    
    cv2.destroyAllWindows()
    
    return lower,  upper



img= cv2.imread("C:/Users/MerveOZKAN/Desktop/lamella_opencv_project/oak_fungal_cropped_canny/mese_mantar_0032_cropped.JPG")
hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower, upper =hsv_value(img,hsv)
print("lower :"+str(lower))
print("upper :"+str(upper))






