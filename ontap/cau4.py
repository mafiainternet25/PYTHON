# Câu 4(2 điểm): Viết chương trình thực hiện các yêu cầu sau.
# a. đọc video từ tệp , in ra thông tin số khung hình trong 1 giây của video.
# b. xem video với màu xám.
# c. đọc video từ tệp , lấy ra 1 ảnh từ video khi ấn phím x.
# d. thực hiện phép phân ngưỡng thích nghi đối với ảnh lấy được.


import cv2
video = cv2.VideoCapture(0)
print('fps:',video.get(5))
while True:
    docvideo,khunghinh = video.read()
    khunghinhxam = cv2.cvtColor(khunghinh,6)
    cv2.imshow('videoxam',khunghinhxam)
    if cv2.waitKey(1) == ord('x'):
        blur = cv2.blur(khunghinhxam,(5,5))
        adapt = cv2.adaptiveThreshold(blur,255,1,0,15,2)
        cv2.imshow('adapt',adapt)
    if cv2.waitKey(1) == 27:break
video.release()
cv2.destroyAllWindows()