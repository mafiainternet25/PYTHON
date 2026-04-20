# #cau:1
# import cv2
# anh = cv2.imread('data/quoc.jpg')
# cao ,rong = anh.shape[:2]
# print("cao:",cao)
# print("rong:",rong)
# x = int(input("x ="))
# y = int(input("y ="))
# print("mau tai diem (x,y):",anh[y,x])
# hesotuongphan = int(input("he so tuong phan ="))
# anhtuongphan = cv2.convertScaleAbs(anh,alpha=hesotuongphan,beta=0)
# cv2.imwrite("anhtuongphan.jpg",anhtuongphan)
# x1 = int(input("x1 ="))
# x2 = int(input("x2 ="))
# y1 = int(input("y1 ="))
# y2 = int(input("y2 ="))
# anhcat = anh[y1:y2,x1:x2]
# cv2.imwrite("anhcat.jpg",anhcat)




# #cau2ab
# import cv2
# anh = cv2.imread('data/quoc.jpg')
# def ham(x): pass
# cv2.namedWindow('boloc')
# cv2.createTrackbar('kichthuoc','boloc',15,51,ham)
# while True:
#     giatri = cv2.getTrackbarPos('kichthuoc','boloc')
#     anhmo = cv2.blur(anh,(giatri,giatri),0)
#     cv2.imshow('boloc',anhmo)
#     if cv2.waitKey(1) == 27: break
# cv2.destroyAllWindows()




# #cau:2cd
# import cv2
# import numpy as np
# anh = cv2.imread('data/quoc.jpg')
# def ham(x): pass
# cao , rong = anh.shape[:2]
# cv2.namedWindow('dichchuyen')
# cv2.createTrackbar('dx','dichchuyen',15,51,ham)
# cv2.createTrackbar('dy','dichchuyen',15,51,ham)
# while True:
#     dx = cv2.getTrackbarPos('dx','dichchuyen')
#     dy = cv2.getTrackbarPos('dy','dichchuyen')
#     matran = np.float32([[1,0,dx],[0,1,dy]])
#     anhdichchuyen = cv2.warpAffine(anh,matran,(rong,cao))
#     cv2.imshow('dichchuyen',anhdichchuyen)
#     if cv2.waitKey(1) == 27: break
# cv2.destroyAllWindows()




# #cau:3
# import cv2
# import matplotlib.pyplot as plt
# anh = cv2.imread('data/quoc.jpg')
# anhxam = cv2.cvtColor(anh,6)
# gauss = cv2.GaussianBlur(anhxam,(5,5),0)
# blur = cv2.blur(anhxam,(5,5))
# _,otsu = cv2.threshold(blur,1,255,0+8)
# _,nhiphan = cv2.threshold(blur,127,255,0)
# adapt = cv2.adaptiveThreshold(blur,255,1,0,15,2)
# canny = cv2.Canny(anhxam,50,150)
# laplace = cv2.convertScaleAbs(cv2.Laplacian(anhxam,6))
# plt.gray()
# plt.subplot(241), plt.imshow(cv2.cvtColor(anh,4))
# plt.subplot(242), plt.imshow(cv2.cvtColor(gauss,4))
# plt.subplot(243), plt.imshow(cv2.cvtColor(blur,4))
# plt.subplot(244), plt.imshow(otsu)
# plt.subplot(245), plt.imshow(adapt)
# plt.subplot(246), plt.imshow(canny)
# plt.subplot(247), plt.imshow(laplace)
# plt.subplot(248), plt.imshow(nhiphan)
# plt.show()




# #cau:4
# import cv2
# video = cv2.VideoCapture('data/quoc.mp4')
# print('FPS:', video.get(5))
# while True:
#     docvideo, khunghinh = video.read()
#     anhxam = cv2.cvtColor(khunghinh, 6)
#     cv2.imshow('video xam', anhxam)
#     phiman = cv2.waitKey(1)
#     if phiman == ord('x'):
#         anhlay = anhxam.copy()
#         blur = cv2.blur(anhlay,(5,5))
#         adaptive = cv2.adaptiveThreshold(blur,255,1,0,15,2)
#         cv2.imshow('adaptive', adaptive)
#     if phiman == 27: break
# video.release()
# cv2.destroyAllWindows()




#cau:5
import cv2
import numpy as np
import matplotlib.pyplot as plt
anh    = cv2.imread('data/quoc.jpg')
anhxam = cv2.cvtColor(anh, 6)
cao, rong = anh.shape[:2]
anhamban = 255 - anh
gocxoay = int(input("goc xoay = "))
tamxoay = (rong//2, cao//2)
matran1 = cv2.getRotationMatrix2D(tamxoay, gocxoay, 1)
anhxoay = cv2.warpAffine(anh, matran1, (rong, cao))
ps1 = np.float32([[0,0],[rong,0],[0,cao],[rong,cao]])
ps2 = np.float32([[500,500],[100,500],[500,100],[100,100]])
matran2 = cv2.getPerspectiveTransform(ps1, ps2)
anhphoicanh = cv2.warpPerspective(anh, matran2, (rong, cao))
gauss = cv2.GaussianBlur(anhxam, (3, 3), 0)
sobelx = cv2.convertScaleAbs(cv2.Sobel(gauss, 6, 1, 0))
sobely = cv2.convertScaleAbs(cv2.Sobel(gauss, 6, 0, 1))
sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
contours, _ = cv2.findContours(sobel, 1, 2)
anhcontour  = anh.copy()
cv2.drawContours(anhcontour, contours, -1, (0, 0, 255), 2)
plt.gray()
plt.subplot(231), plt.imshow(cv2.cvtColor(anh,4))
plt.subplot(232), plt.imshow(cv2.cvtColor(anhamban,4))
plt.subplot(233), plt.imshow(cv2.cvtColor(anhxoay,4))
plt.subplot(234), plt.imshow(cv2.cvtColor(anhphoicanh,4))
plt.subplot(235), plt.imshow(cv2.cvtColor(anhcontour,4))
plt.subplot(236), plt.imshow(sobel),  
plt.show()