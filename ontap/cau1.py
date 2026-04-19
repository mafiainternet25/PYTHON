# Câu 1(3 điểm): Đọc ảnh màu và thực hiện các yêu cầu sau.
# a. in ra chiều rộng và cao của ảnh.
# b. in giá trị màu của ảnh tại điểm có tọa độ nhập vào.
# c. tăng độ tương phản của ảnh với hệ số tương phản nhập vào từ bàn phím, lưu lại ảnh kết quả.
# d. cắt một phần ảnh với các tọa độ nhập vào từ bàn phím , lưu ảnh vừa cắt.

import cv2
anh = cv2.imread('data/quoc.jpg')

cao,rong = anh.shape[:2]
print('cao:',cao)
print('rong:',rong)

x = int(input("x ="))
y = int(input("y ="))
print('mau tai diem x,y:',anh[y,x])

hesotuongphan = int(input("hesotuongphan ="))
anhtuongphan = cv2.convertScaleAbs(anh,alpha=hesotuongphan,beta=5)
cv2.imshow('anhtuongphan',anhtuongphan)

x1 = int(input("x1 ="))
x2 = int(input("x2 ="))
y1 = int(input("y1 ="))
y2 = int(input("y2 ="))
anhcat = anh[y1:y2,x1:x2]
cv2.imshow('anhcat',anhcat)
cv2.imwrite('anhcat.jpg',anhcat)

cv2.waitKey(0)
cv2.destroyAllWindows()
