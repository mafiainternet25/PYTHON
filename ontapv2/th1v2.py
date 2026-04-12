#bai1
import cv2
anh = cv2.imread('data/quoc.jpg')
cv2.imshow('anh',anh)
cv2.waitKey(0)
cv2.destroyAllWindows()



#bai2
import cv2
anh = cv2.imread('data/quoc.jpg')
x = int(input('x ='))
y = int(input('y ='))
print('mau tai diem x,y :',anh[y,x])



#bai3
import cv2
anh = cv2.imread('data/quoc.jpg')
anhxam = cv2.cvtColor(anh,6)
cv2.imshow('anh',anh)
cv2.imshow('anhxam',anhxam)
cv2.waitKey(0)
cv2.destroyAllWindows()



#bai4
import cv2
video = cv2.VideoCapture('data/quoc.mp4')
while True:
    doc,khung = video.read()
    phim = cv2.waitKey(1)
    cv2.imshow('video',khung)
    if phim == ord('s'): cv2.imwrite('anhghi.jpg',khung)
    if phim == ord('q'): break
video.release()
cv2.destroyAllWindows()



#bai5
import cv2
video = cv2.VideoCapture('data/quoc.mp4')
fps = video.get(5)
tongkhung = video.get(7)
print('fps :',fps)
print('tongkhung :',tongkhung)
while True:
    doc,khung = video.read()
    khungxam = cv2.cvtColor(khung,6)
    cv2.imshow('videoxam',khungxam)
    if cv2.waitKey(1) == 27: break
video.release()
cv2.destroyAllWindows()



#bai6
import cv2
import matplotlib.pyplot as plt
anh1 = cv2.imread('data/quoc.jpg')
anh2 = cv2.imread('data/quoc2.jpg') 
anh1x = cv2.cvtColor(anh1,6)
anh2x = cv2.cvtColor(anh2,6)
anh1rgb = cv2.cvtColor(anh1,4)
anh2rgb = cv2.cvtColor(anh2,4)
plt.subplot(221),plt.imshow(anh1x,cmap='gray')
plt.subplot(222),plt.imshow(anh2x,cmap='gray')
plt.subplot(223),plt.imshow(anh1rgb)
plt.subplot(224),plt.imshow(anh2rgb)
plt.show()