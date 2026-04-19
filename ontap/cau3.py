# Câu 3(3 điểm): Đọc ảnh màu và thực hiện các yêu cầu sau.
# a. khử nhiễu ảnh bằng bộ lọc gauss.
# b. thực hiện phân ngưỡng ảnh bằng thuật toán phân ngưỡng tối ưu.
# c. tách biên ảnh bằng phương pháp tách biên canny.
# e. khử nhiễu ảnh bằng bộ lọc trung bình.
# f. thực hiện phân ngưỡng ảnh bằng thuật toán phân ngưỡng thích nghi.
# j. tách biên ảnh bằng phương pháp tách biên laplace.
# d. hiển thị ảnh ban đầu , các ảnh kết quả trên matplotlib.

import cv2
import matplotlib.pyplot as plt 
anh = cv2.imread('data/quoc.jpg')
anhxam = cv2.cvtColor(anh,6)

gauss = cv2.GaussianBlur(anhxam,(15,15),0)

blur = cv2.blur(anhxam,(5,5))
_,otsu = cv2.threshold(blur,1,255,0+8)

canny = cv2.Canny(anhxam,50,150)

median = cv2.medianBlur(anhxam,5)

adapt = cv2.adaptiveThreshold(blur,255,1,0,15,2)

laplace = cv2.Laplacian(anhxam,6)



plt.gray()
plt.subplot(241),plt.imshow(cv2.cvtColor(anh,4))
plt.subplot(242),plt.imshow(cv2.cvtColor(gauss,4))
plt.subplot(243),plt.imshow(cv2.cvtColor(otsu,4))
plt.subplot(244),plt.imshow(cv2.cvtColor(canny,4))
plt.subplot(245),plt.imshow(cv2.cvtColor(median,4))
plt.subplot(246),plt.imshow(cv2.cvtColor(adapt,4))
plt.subplot(247),plt.imshow(cv2.convertScaleAbs(laplace))
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows
