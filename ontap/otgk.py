# ==================== PHẦN 1 ====================
import cv2
import numpy as np
import matplotlib.pyplot as plt
img     = cv2.imread('onhieuoi.jpg')
img_xam = cv2.imread('onhieuoi.jpg', 0)
print('Kích thước :', img.shape)
print('Tổng pixel :', img.size)
print('Pixel[50,50]:', img[50, 50])
crop = img[100:300, 100:400]
cv2.imwrite('ket_qua.jpg', img_xam)




# ==================== PHẦN 2 ====================
import cv2
img = cv2.imread('onhieuoi.jpg')
sang_hon = cv2.convertScaleAbs(img, alpha=1.5, beta=50)
am_ban   = 255 - img
h, w     = img.shape[:2]
center   = (w//2, h//2)
matranxoay   = cv2.getRotationMatrix2D(center, 45, 1)
xoay     = cv2.warpAffine(img, matranxoay, (w, h))






# ==================== PHẦN 3 ====================
import cv2
img     = cv2.imread('onhieuoi.jpg')
img_xam = cv2.cvtColor(img, 6)
gauss  = cv2.GaussianBlur(img_xam, (5, 5), 0)
sobelx = cv2.Sobel(gauss, 6, 1, 0)
sobely = cv2.Sobel(gauss, 6, 0, 1)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
sobel  = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
laplace = cv2.convertScaleAbs(cv2.Laplacian(gauss, 6))
canny   = cv2.Canny(gauss, 50, 150)







# ==================== CÂU 4 ====================
import cv2
import numpy as np
img     = cv2.imread('onhieuoi.jpg')
img_xam = cv2.cvtColor(img, 6)
nguong, otsu = cv2.threshold(img_xam, 0, 255, 0 + 8)
adaptive = cv2.adaptiveThreshold(img_xam, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
contours, _ = cv2.findContours(otsu, 0, 2)
ban_sao = img.copy()
cv2.drawContours(ban_sao, contours, -1, (0, 0, 255), 2)    # do
for i, c in enumerate(contours):
    print(f'Contour {i}: dien tich = {cv2.contourArea(c):.1f}')
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(ban_sao, (x, y), (x+w, y+h), (0, 255, 0), 2)  # xanh la
cv2.imshow('Contour', ban_sao)
cv2.waitKey(0)