# Câu 2(2 điểm): Đọc ảnh màu và thực hiện các yêu cầu sau.
# a. tạo trackbar để chọn kích thước mặt nạ lọc.
# b. lọc ảnh bằng bộ lọc trung bình với kích thước mặt nạ lấy từ trackbar.
# c. tạo trackbar để chọn kích thước dx, dy.
# d. dịch chuyển ảnh với khoảng cách theo trục x và trục y là dx , dy lấy từ trackbar.

import cv2
import numpy as np
anh = cv2.imread('data/quoc.jpg')
cao,rong = anh.shape[:2]
def ham(x):pass 



cv2.namedWindow('anh')
cv2.createTrackbar('k','anh',10,50,ham)
while True:
    k = cv2.getTrackbarPos('k','anh')
    if k % 2 == 0 :k += 1
    anhloc = cv2.medianBlur(anh,k)
    cv2.imshow('anh',anhloc)
    if cv2.waitKey(1) == 27:break
cv2.destroyAllWindows()



cv2.namedWindow('anh')
cv2.createTrackbar('dx','anh',10,50,ham)
cv2.createTrackbar('dy','anh',10,50,ham)
while True:
    dx = cv2.getTrackbarPos('dx','anh')
    dy = cv2.getTrackbarPos('dy','anh')
    matran = np.float32([[1,0,dx],[0,1,dy]])
    anhdichchuyen = cv2.warpAffine(anh,matran,(rong,cao))
    cv2.imshow('anh',anhdichchuyen)
    if cv2.waitKey(1)==27:break
cv2.destroyAllWindows()