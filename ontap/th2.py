#bai1
import cv2
anh = cv2.imread('data/quoc.jpg')
def ham(x):
    dotuongphan = cv2.getTrackbarPos('dotuongphan','anh')
    dosang = cv2.getTrackbarPos('dosang','anh')
    anhmoi = cv2.convertScaleAbs(anh,alpha=dotuongphan,beta=dosang)
    cv2.imshow('anh',anhmoi)
cv2.namedWindow('anh')
cv2.createTrackbar('dotuongphan','anh',10,100,ham)
cv2.createTrackbar('dosang','anh',10,100,ham)
ham(0)
cv2.waitKey(0)
cv2.destroyAllWindows()



#bai2
import cv2
anh = cv2.imread('data/quoc.jpg')
anhxam = cv2.cvtColor(anh,6)
def ham(x):
    nguong = cv2.getTrackbarPos('nguong','anh')
    _, anhnhiphan = cv2.threshold(anhxam,nguong,255,0)
    anhamban = 255 - anhnhiphan 
    cv2.imshow('anh',anhnhiphan)
    cv2.imshow('anhamban',anhamban)
    cv2.imwrite('anhamban.jpg',anhamban)
cv2.namedWindow('anh')
cv2.createTrackbar('nguong','anh',1,255,ham)
ham(0)
cv2.waitKey(0)
cv2.destroyAllWindows()



#bai3
import cv2
anh = cv2.imread('data/quoc.jpg')
tile = float(input('ti le ='))
cao = int(anh.shape[0]*tile)
rong = int(anh.shape[1]*tile)
anhthuphong = cv2.resize(anh,(rong,cao))
cv2.imshow('anhthuphong',anhthuphong)
cv2.waitKey(0)
cv2.destroyAllWindows()



#bai4
import cv2
anh = cv2.imread('data/quoc.jpg')
y1 = 10
y2 = 50
x1 = 10
x2 = 50
anhcat = anh[y1:y2,x1:x2]
cv2.imshow('anhcat',anhcat)
cv2.waitKey(0)
cv2.destroyAllWindows()



#bai5
import cv2
import numpy as np 
anh = cv2.imread('data/quoc.jpg')
cao,rong = anh.shape[:2]
def ham(x):
    dx = cv2.getTrackbarPos('dx','anh')
    dy = cv2.getTrackbarPos('dy','anh')
    matran = np.float32([[1,0,dx],[0,1,dy]])    
    anhdichchuyen = cv2.warpAffine(anh,matran,(rong,cao))
    cv2.imshow('anh',anhdichchuyen)
cv2.namedWindow('anh')
cv2.createTrackbar('dx','anh',10,100,ham)
cv2.createTrackbar('dy','anh',10,100,ham)
ham(0)
cv2.waitKey(0)
cv2.destroyAllWindows()



#bai6
import cv2
anh = cv2.imread('data/quoc.jpg')
cao,rong = anh.shape[:2]
tamxoay = (rong//2,cao//2)
def ham(x):
    gocxoay = cv2.getTrackbarPos('gocxoay','anh')
    matran = cv2.getRotationMatrix2D(tamxoay,gocxoay,1)
    anhxoay = cv2.warpAffine(anh,matran,(rong,cao))
    cv2.imshow('anh',anhxoay)
cv2.namedWindow('anh')
cv2.createTrackbar('gocxoay','anh',1,360,ham)
ham(0)
cv2.waitKey(0)
cv2.destroyAllWindows()



#bai7
import cv2
import numpy as np
anh = cv2.imread('data/quoc.jpg')
cao,rong = anh.shape[:2]
diemgoc = np.float32([[0,0],[rong,0],[0,cao],[rong,cao]])
diemmoi = np.float32([[50,50],[50,10],[10,50],[10,10]])
matran = cv2.getPerspectiveTransform(diemgoc,diemmoi)
anhphoicanh = cv2.warpPerspective(anh,matran,(rong,cao))
cv2.imshow('anhphoicanh',anhphoicanh)
cv2.waitKey(0)
cv2.destroyAllWindows()











