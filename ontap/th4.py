# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# anh = cv2.imread('data/quoc.jpg')
# xam = cv2.cvtColor(anh,6)                       
# loctv = cv2.medianBlur(xam,5)                       
# otsu,nhiphan = cv2.threshold(loctv,0,255,0+8)                       #**
# contours,_ = cv2.findContours(nhiphan,0,2)                          #**
# bansao = anh.copy()
# cv2.drawContours(bansao,contours,-1,(0,0,255),2)                    #**
# plt.subplot(121),plt.imshow(cv2.cvtColor(anh,4))      
# plt.subplot(122),plt.imshow(cv2.cvtColor(bansao,4))  
# plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt
anh = cv2.imread('data/quoc.jpg')
xam = cv2.cvtColor(anh,6)
loctv = cv2.medianBlur(xam,5)
otsu,nhiphan = cv2.threshold(loctv,1,255,0+8)
contours,_ = cv2.findContours(nhiphan,0,2)
anhbansao = anh.copy()
cv2.drawContours(anhbansao,contours,-1,(0,0,255),2)
plt.subplot(121),plt.imshow(cv2.cvtColor(anh,4))
plt.subplot(122),plt.imshow(cv2.cvtColor(anhbansao,4))
plt.show()
