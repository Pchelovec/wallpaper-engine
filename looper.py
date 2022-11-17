import ctypes
import os
import re
import time
import ctypes

SPI_SETDESKWALLPAPER = 20

data = 'C:\\data'
os.chdir(data)
images = os.listdir();

images.sort(key = lambda f:int(re.sub('\D', '', f)))

#ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C:\\data\\frame1.jpg" , 0)

for image in images:
    print(image)
    image_path = os.path.join("C:\\data",image)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
    time.sleep(1/24)


