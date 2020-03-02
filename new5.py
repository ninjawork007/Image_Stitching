import cv2
import datetime
import os
d1=datetime.datetime.now().strftime("%Y_%m_%d")
path = "C:/Users/Soumya/Desktop/image-stitching-opencv/image-stitching-opencv/images/image"
camera = cv2.VideoCapture(0)
#camera = cv2.VideoCapture(0)
#camera = cv2.VideoCapture(0)
#camera = cv2.VideoCapture(0)
cam=cv2.VideoCapture(1)
#cam=cv2.VideoCapture(1)
#cam=cv2.VideoCapture(1)
#cam=cv2.VideoCapture(1)

for i in range(4):
    return_value, image = camera.read()
    return_valu, imag = cam.read()
    im1=cv2.resize(image,(500,500))
    im2=cv2.resize(imag,(500,500))
    cv2.imwrite(os.path.join(path,str(d1)+str(i)+'.jpeg'), im1)
    cv2.imwrite(os.path.join(path,str(d1)+str(i)+'1.jpeg'), im2)
del(camera)
