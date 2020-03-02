import os
for i in range(2):
    os.remove("output{0}.png".format(i+1))
print("Files removed and Image stitched into video ! check the folder")
