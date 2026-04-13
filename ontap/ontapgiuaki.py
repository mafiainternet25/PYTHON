#cau1
import cv2
anh = cv2.imread('data/quoc.jpg')
anhxam = cv2.cvtColor(anh,6)
_, otsu = cv2.threshold(anhxam,0,255,0+8)
canny = cv2.Canny(anh,50,150)
cv2.imshow('otsu',otsu)
cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()



#cau2
import cv2
import numpy as np
anh = cv2.imread('data/quoc.jpg')
kernel = np.ones((5,5),np.uint8)
erode = cv2.erode(anh,kernel)
dilate = cv2.dilate(erode,kernel)
cv2.imshow('anhgoc',anh)
cv2.imshow('anhketqua',dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()



#cau3
import cv2
import numpy as np
video = cv2.VideoCapture('data/quoc.mp4')
print('rong',video.get(3))
print('cao',video.get(4))
print('fps',video.get(5))
while True:
    doc,khunghinh = video.read()
    videoxam = cv2.cvtColor(khunghinh,6)
    laplace = cv2.Laplacian(videoxam,6)
    laplace = np.uint8(np.absolute(laplace))
    cv2.imshow('tach bien laplace',laplace)
    if cv2.waitKey(1)==27:break
video.release()
cv2.destroyAllWindows()

