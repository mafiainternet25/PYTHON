# Câu 5(3 điểm): Viết chương trình thực hiện các yêu cầu sau.
# a. tạo ảnh âm bản từ ảnh gốc.
# b. xoay ảnh với góc xoay nhập vào từ bàn phím quanh tâm ảnh , scale = 1.
# c. biến đổi phối cảnh ảnh với bốn điểm nguồn nhập vào từ bàn phím.
# d. tách biên ảnh sobel cả hướng x và y.
# e. tìm contour từ ảnh tách biên , vẽ contour màu đỏ lên ảnh gốc.
# f. hiển thị ảnh gốc , âm bản , xoay , sobel , contour trên matplotlib.

import cv2
import numpy as np
import matplotlib.pyplot as plt
anh = cv2.imread('data/quoc.jpg')
anhxam = cv2.cvtColor(anh,6)


anhamban = 255 - anh

gocxoay = int(input('gocxoay='))
cao,rong = anh.shape[:2]
tamxoay = (rong//2,cao//2)
matranxoay = cv2.getRotationMatrix2D(tamxoay,gocxoay,1)
anhxoay = cv2.warpAffine(anh,matranxoay,(rong,cao))

ps1 = np.float32([[0,0],[rong,0],[0,cao],[rong,cao]])
m = int(input('m='))
n = int(input('n='))
ps2 = np.float32([[m,m],[n,m],[m,n],[n,n]])
matranphoicanh = cv2.getPerspectiveTransform(ps1,ps2)
anhphoicanh = cv2.warpPerspective(anh,matranphoicanh,(rong,cao))

gauss = cv2.GaussianBlur(anhxam,(5,5),0)
sobelx = cv2.convertScaleAbs(cv2.Sobel(gauss,6,1,0))
sobely = cv2.convertScaleAbs(cv2.Sobel(gauss,6,0,1))
anhsobel = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

contour,_ = cv2.findContours(anhsobel,1,2)
anhcontour = anh.copy()
cv2.drawContours(anhcontour,contour,-1,(0,0,255),2)

plt.gray()
plt.subplot(241),plt.imshow(cv2.cvtColor(anh,4))
plt.subplot(242),plt.imshow(cv2.cvtColor(anhamban,4))
plt.subplot(243),plt.imshow(cv2.cvtColor(anhxoay,4))
plt.subplot(244),plt.imshow(cv2.cvtColor(anhphoicanh,4))
plt.subplot(245),plt.imshow(cv2.cvtColor(anhsobel,4))
plt.subplot(246),plt.imshow(cv2.cvtColor(anhcontour,4))
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()