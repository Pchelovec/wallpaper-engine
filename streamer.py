import cv2
import numpy as np
import os
from pathlib import *
import ctypes

SPI_SETDESKWALLPAPER = 20 

current_dir = Path.cwd()
home_dir = "C://data"
 
print(current_dir)
print(home_dir)

count = 0

print("Preparing file...")
cap = cv2.VideoCapture("dog.mp4")
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        cv2.imwrite(os.path.join(home_dir, "frame%d.jpg" % count), frame)
        count=count+1;
        print("current progress is %d", count)
        

    key = cv2.waitKey(1)
    if key == 27:
        break
        cap.release()
        cv2.destroyAllWindows()

        
print("File is ready for looping")
