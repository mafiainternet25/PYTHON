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





import cv2
import numpy as np
anh = cv2.imread('data/quoc.jpg')
cao,rong = anh.shape[:2]
matran = np.float32([[1,0,50],[0,1,0]])
ketqua = cv2.warpAffine(anh,matran,(rong,cao))
blur = cv2.medianBlur(ketqua,5)
anhxam = cv2.cvtColor(blur,6)
_,nhiphan = cv2.threshold(anhxam,127,255,0)


cv2.imshow('anh',anh)           

