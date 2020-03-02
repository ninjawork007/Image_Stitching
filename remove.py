import os
import datetime
os.chdir("C:/Users/Soumya/Desktop/image-stitching-opencv/image-stitching-opencv/images/image")
d1=datetime.datetime.now().strftime("%Y_%m_%d")
for i in range(4):
    os.remove(str(d1)+str(i)+'.jpeg')
    os.remove(str(d1)+str(i)+'1.jpeg')
    
print("Files removed and Image stitched into video ! check the folder")
