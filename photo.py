
from smb.SMBConnection import SMBConnection

import cv2
import numpy as np
from matplotlib import pyplot as plt
import urllib
import os
d1=datetime.datetime.now().strftime("%Y_%m_%d")
path = "smb://192.168.0.104/image on 192.168.0.104"
camera = cv2.VideoCapture(0)
userID = 'kc'
password = 'Research@11'
client_machine_name = 'kc'

server_name = 'sambaserver'
server_ip = '192.168.0.104'

domain_name = 'workgroup'

conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True,
                     is_direct_tcp=True)

conn.connect(server_ip, 445)

shares = conn.listShares()



#(cv2.imwrite("/run/user/1000/gvfs/smb-share:server=192.168.0.104,share=sambashare/myimg.jpg",img)
for i in range(4):
    return_value, image = camera.read()
    
    cv2.imwrite("/run/user/1000/gvfs/smb-share:server=192.168.0.104,share=sambashare",str(d1)+str(i)+'.jpeg',image)
    
del(camera)


camera.release()
conn.close()
