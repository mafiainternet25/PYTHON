import cv2
import numpy as np
img = cv2.imread('anh.jpg')
gauss = cv2.GaussianBlur(img, (5,5), 0)
xam = cv2.cvtColor(gauss, 6)
def update(x):
    nguongduoi = cv2.getTrackbarPos('Nguong duoi', 'Canny')
    nguongtren = nguongduoi * 2
    canny = cv2.Canny(xam, nguongduoi, nguongtren)
    cv2.imshow('Canny', canny)
cv2.namedWindow('Canny')
cv2.createTrackbar('Nguong duoi', 'Canny', 0, 255, update)
update(0)  
cv2.waitKey(0)



import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('anh.jpg')
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
xam = cv2.cvtColor(bilateral, cv2.COLOR_BGR2GRAY)
laplace = cv2.Laplacian(xam, 6)
laplace = np.uint8(np.absolute(laplace))
canny = cv2.Canny(xam, 100, 200)
plt.subplot(131); plt.imshow(cv2.cvtColor(bilateral, 4));
plt.subplot(132); plt.imshow(laplace, cmap='gray');                     
plt.subplot(133); plt.imshow(canny,   cmap='gray');                
plt.show()




import cv2
img = cv2.imread('anh.jpg')
xam = cv2.cvtColor(img, 6)
_, nguong = cv2.threshold(xam, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(nguong, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
cv2.imshow('Contour', img)
cv2.waitKey(0)