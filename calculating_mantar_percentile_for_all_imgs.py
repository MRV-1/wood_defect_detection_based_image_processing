# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:34:27 2023

@author: MerveOZKAN
"""

import numpy as np
import cv2
import glob 
import os
import matplotlib.pyplot as plt
import codecs
import io


global result; global img;global percentage;global filename;

def get_percentage(sum_color_pixel_count, sum_pixel_count):
    try:
        return ((100.0 * sum_color_pixel_count) / sum_pixel_count )
    except ZeroDivisionError:
        return float('inf')
    
    
def read_all_images(source_path):

    for img in glob.glob(source_path+"/*.jpg"):
        cv_img = cv2.imread(img)
        filepath= glob.glob(source_path+"/*.jpg")
    
    return filepath

def masked_imgs(path,masked_file_name):
     filename = path.split("\\")[1].split('.')[0]
     print("filename:",filename)
     img = cv2.imread(path)
     hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
     lower = np.array([23,70,170])
     upper = np.array([50,255,255])
     mask = cv2.inRange(hsv, lower, upper)
     result = cv2.bitwise_and(img,img, mask=mask)
     img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
     img_result=cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
     return result,img,filename
    
def prepercentage(result,img):
    rows,cols, number_of_channels= result.shape
    sum_pixel_count = rows * cols  
    sum_color_pixel_count = 0;i=0;j=0
 
    for i in range(rows):
       for j in range(cols):
           
           pixel_value_r = result[i,j,0]
           pixel_value_g = result[i,j,1]
           pixel_value_b = result[i,j,2]
           #print("pixel_value_r :",pixel_value_r,"pixel_value_g :",pixel_value_g,"pixel_value_b :",pixel_value_b)
           if (pixel_value_r != 0 or pixel_value_g != 0 or pixel_value_b != 0):
               #print("renkli pixel elde edildi")
               sum_color_pixel_count = sum_color_pixel_count + 1
            
    print("Renkli piksel sayısı :", sum_color_pixel_count)
    print("Toplam piksel sayısı :", sum_pixel_count)
    percentage = get_percentage(sum_color_pixel_count, sum_pixel_count)
    print("Proportion of fungal on the coverslip : %", percentage)    
    return percentage

def write_percantage_on_image(result,percentage):
   # Convert to PIL Image
   font                   = cv2.FONT_HERSHEY_SIMPLEX
   bottomLeftCornerOfText = (50,100)                   
   fontScale              = 3
   fontColor              = (255,0,0)
   thickness              = 5
   lineType               = 1

   cv2.putText(result, (f"%{percentage}"), 
   bottomLeftCornerOfText, 
   font, 
   fontScale,
   fontColor,
   thickness,
   lineType)
    
   return result
    
    
def masked_image_save(filename, percentage,masked_file_name,result,text_file_name):
    result = write_percantage_on_image(result, percentage)
    
    if not os.path.exists(masked_file_name):
        os.makedirs(masked_file_name)
        print("The new directory is created!")
    else:
        print("The directory already have.")
    cv2.imwrite(masked_file_name+"\\"+filename+"_masked.JPG", result)
    print(filename+"_masked.JPG saved")
    #save the fungal percentage ratios of all images in a text file
    save_all_percentile_information(filename, percentage,masked_file_name)
    
    

def save_all_percentile_information(filename, percentage,text_file_name):
    with open('C:/Users/MerveOZKAN/Desktop/lamella_opencv_project/oak_fungal_masked_percentile/readme.txt', 'a') as f:  
        #if it opens in "w" write mode it does not overwrite the file but takes the last appended one, "a" append mode allows printing all lines
        f.write('filename : ' + str(filename) + '.JPG --> mantar percentage : ' + str(percentage)+'\n' )
        f.close()
    
    
    
source_path='C:/Users/MerveOZKAN/Desktop/lamella_opencv_project/oak_fungal'
masked_file_name = 'C:/Users/MerveOZKAN/Desktop/lamella_opencv_project/oak_fungal_masked_percentile'
text_file_name = 'C:/Users/MerveOZKAN/Desktop/lamella_opencv_project/oak_fungal_masked_percentile/readme.txt'
filepaths = read_all_images(source_path)
print(str(len(filepaths)) +"  images will be calculate mantar percentile !")




for path in filepaths:
    result,img,filename = masked_imgs(path,masked_file_name)
    percentage=prepercentage(result,img)
    print("percentage:",percentage)
    print("-------------------------------------------------------------------")
    masked_image_save(filename, percentage,masked_file_name,result,text_file_name)
    





    
    
