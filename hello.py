import os
for i in range(5):
    os.system("python new5.py")
    os.system("python image_stitching_simple.py --images images/image --output output{0}.png".format(i+1))
    os.system("python remove.py")
    os.chdir("C:/Users/Soumya/Desktop/image-stitching-opencv/image-stitching-opencv")
os.system("python im2v.py")
os.system("python remove2.py")
os.system("python video_object_detection.py")
