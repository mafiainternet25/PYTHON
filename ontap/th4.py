import cv2
import matplotlib.pyplot as plt

anh = cv2.imread('data/quoc.jpg')
anhxam = cv2.cvtColor(anh,6)

loctv = cv2.medianBlur(anhxam,5)

otsu,nhiphan = cv2.threshold(loctv,1,255,0+8)

contours,_ = cv2.findContours(nhiphan,0,2)

cv2.drawContours(anh,contours,-1,(0,0,255),2)

plt.subplot(111),plt.imshow(cv2.cvtColor(anh,4))
plt.show()