#bai1
import cv2
import matplotlib.pyplot as plt
anh = cv2.imread('data/quoc.jpg')
loctrungbinh = cv2.blur(anh, (5, 5))
loctrungvi = cv2.medianBlur(anh, 5)
locgauss = cv2.GaussianBlur(anh, (5, 5), 0)
locbilateral = cv2.bilateralFilter(anh, 9, 75, 75)
plt.subplot(231),plt.imshow(cv2.cvtColor(anh, 4))
plt.subplot(232),plt.imshow(cv2.cvtColor(loctrungbinh, 4))
plt.subplot(233),plt.imshow(cv2.cvtColor(loctrungvi, 4))
plt.subplot(234),plt.imshow(cv2.cvtColor(locgauss, 4))
plt.subplot(235),plt.imshow(cv2.cvtColor(locbilateral, 4))
plt.show()



#bai2
import cv2
import numpy as np
anh = cv2.imread('data/quoc.jpg')
nhieu = np.zeros(anh.shape, np.uint8)
cv2.randu(nhieu, 0, 255)
anhnhieu = anh.copy()
anhnhieu[nhieu < 30] = 0
anhnhieu[nhieu > 225] = 255
anhloc = anhnhieu.copy()
def ham(x):
    global anhloc
    kichthuoc = cv2.getTrackbarPos('Kernel', 'Anh') * 2 + 1
    if kichthuoc < 1:kichthuoc = 1
    anhloc = cv2.medianBlur(anhnhieu, kichthuoc)
    cv2.imshow('Anh', anhloc)
cv2.namedWindow('Anh')
cv2.imshow('Anh nhieu', anhnhieu)
cv2.createTrackbar('Kernel', 'Anh', 1, 10, ham)
ham(0)
while True:
    phim = cv2.waitKey(0)
    if phim == ord('s'):cv2.imwrite('anhkhunhieu.jpg', anhloc)
    if phim == ord('q'):break
cv2.destroyAllWindows()



#bai3
import cv2
anh = cv2.imread('data/quoc.jpg')
anhloc = anh.copy()
def ham(x):
    global anhloc
    k = cv2.getTrackbarPos('Kernel', 'Anh') * 2 + 1
    anhloc = cv2.GaussianBlur(anh, (k, k), 0)
    cv2.imshow('Anh', anhloc)
cv2.namedWindow('Anh')
cv2.createTrackbar('Kernel', 'Anh', 1, 20, ham)
ham(0)
while True:
    phim = cv2.waitKey(0)
    if phim == 13:cv2.imwrite('anhgauss.jpg', anhloc)
    if phim == ord('q'):break
cv2.destroyAllWindows()



#bai4
import cv2
import easyocr
anh = cv2.imread('data/image.jpg')
anhmoi = cv2.convertScaleAbs(anh, alpha=1.5, beta=30)
anhxam = cv2.cvtColor(anhmoi, 6)
cv2.imshow('Anh goc', anh)
cv2.imshow('Anh xam', anhxam)
cv2.waitKey(1)
reader = easyocr.Reader(['vi', 'en'])
ketqua = reader.readtext('data/image.jpg')
for dong in ketqua:
    print(dong[1])
cv2.waitKey(0)
cv2.destroyAllWindows()





