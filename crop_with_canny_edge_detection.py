# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:25:29 2023

@author: MerveOZKAN
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import os


def read_all_images(source_path):

    for img in glob.glob(source_path+"/*.jpg"):
        cv_img = cv2.imread(img)
        filepath= glob.glob(source_path+"/*.jpg")
    
    return filepath
    
def change_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img





def canny_edge_detection(path,cropped_file_name):     
     filename = path.split("\\")[1].split('.')[0]
     img = cv2.imread(path)
     img_brightness=change_brightness(img,70)  
     #parlaklığı artırmak köşedeki görünmemesi gereken edge'leri yok etmekte başarılı olmaktadır
     median_blur=cv2.medianBlur(img_brightness, 13)  #küçük ağaç parçacıklarını yok etmekte işe yarıyor
     edges = cv2.Canny(median_blur, 20, 185)


     ## find the non-zero min-max coords of canny
     pts = np.argwhere(edges>0)
     y1,x1 = pts.min(axis=0)
     y2,x2 = pts.max(axis=0)

     ## crop the region
     cropped = img[y1:y2, x1:x2]
     
     if not os.path.exists(cropped_file_name):
         os.makedirs(cropped_file_name)
         print("The new directory is created!")
     else:
         print("The directory already have.")
         
     cv2.imwrite(cropped_file_name+"\\"+filename+"_cropped.JPG", cropped)
     print(filename+"_cropped.JPG saved")
     
     



source_path='C:/Users/MerveOZKAN/Desktop/lamella_opencv_project/mese_mantar'
cropped_file_name = 'C:/Users/MerveOZKAN/Desktop/lamella_opencv_project/mese_mantar_cropped_canny'
filepaths = read_all_images(source_path)
print(str(len(filepaths)) +"  images will be cropped !")

for path in filepaths:
    canny_edge_detection(path,cropped_file_name)










