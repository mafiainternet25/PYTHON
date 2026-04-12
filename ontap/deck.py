#cau:1
import cv2
anh = cv2.imread('data/image.jpg')
cao ,rong = anh.shape[:2]
print("cao:",cao)
print("rong:",rong)
x = int(input("x ="))
y = int(input("y ="))
print("mau tai diem (x,y):",anh[y,x])
hesotuongphan = int(input("he so tuong phan ="))
anhtuongphan = cv2.convertScaleAbs(anh,alpha=hesotuongphan,beta=0)
cv2.imwrite("anhtuongphan.jpg",anhtuongphan)
x1 = int(input("x1 ="))
x2 = int(input("x2 ="))
y1 = int(input("y1 ="))
y2 = int(input("y2 ="))
anhcat = anh[y1:y2,x1:x2]
cv2.imwrite("anhcat.jpg",anhcat)




#cau2ab
import cv2
anh = cv2.imread('data/image.jpg')
def ham(x): pass
cv2.namedWindow('boloc')
cv2.createTrackbar('kichthuoc','boloc',15,51,ham)
while True:
    giatri = cv2.getTrackbarPos('kichthuoc','boloc')
    anhmo = cv2.blur(anh,(giatri,giatri),0)
    cv2.imshow('boloc',anhmo)
    if cv2.waitKey(1) == 27: break
cv2.destroyAllWindows()




#cau:2cd
import cv2
import numpy as np
anh = cv2.imread('data/image.jpg')
def ham(x): pass
cao , rong = anh.shape[:2]
cv2.namedWindow('dichchuyen')
cv2.createTrackbar('dx','dichchuyen',15,51,ham)
cv2.createTrackbar('dy','dichchuyen',15,51,ham)

while True:
    dx = cv2.getTrackbarPos('dx','dichchuyen')
    dy = cv2.getTrackbarPos('dy','dichchuyen')
    matran = np.float32([[1,0,dx],[0,1,dy]])
    anhdichchuyen = cv2.warpAffine(anh,matran,(rong,cao))
    cv2.imshow('dichchuyen',anhdichchuyen)
    if cv2.waitKey(1) == 27: break
cv2.destroyAllWindows()




#cau:3
import cv2
import matplotlib.pyplot as plt
anh = cv2.imread('data/image.jpg')
anhxam = cv2.cvtColor(anh,6)
gauss = cv2.GaussianBlur(anh,(15,15),15)
blur = cv2.blur(anh,(15,15))
otsu = cv2.threshold(anhxam,15,15,15)[1]
adapt = cv2.adaptiveThreshold(anhxam,15,0,0,15,15)
canny = cv2.Canny(anhxam,15,15)
laplace = cv2.Laplacian(anhxam,6)
plt.gray()
plt.subplot(241), plt.imshow(cv2.cvtColor(anh,4))
plt.subplot(242), plt.imshow(cv2.cvtColor(gauss,4))
plt.subplot(243), plt.imshow(cv2.cvtColor(blur,4))
plt.subplot(244), plt.imshow(otsu)
plt.subplot(245), plt.imshow(adapt)
plt.subplot(246), plt.imshow(canny)
plt.subplot(247), plt.imshow(laplace)
plt.show()




#cau:4
import cv2
import numpy as np
video = cv2.VideoCapture('data/video.mp4')
matran = np.ones((5,5),np.uint8)
fps = video.get(5)
print('fps:',fps)
while True:
    docvideo, khunghinh = video.read()
    anhxam = cv2.cvtColor(khunghinh,6)
    cv2.imshow('videoxam',anhxam)
    phiman = cv2.waitKey(15)
    if phiman == ord('x'):
        anhgianno = cv2.dilate(khunghinh,matran,iterations=1)
        cv2.imshow('anhgianno',anhgianno)
    if phiman == 27: break
video.release()
cv2.destroyAllWindows()
