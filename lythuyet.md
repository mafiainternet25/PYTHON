1. Thao tác cơ bản với Ảnh và Video (Chương 1)

   Đọc, hiển thị và lưu ảnh: Sử dụng cv2.imread(filename, flag) (thêm 0 để đọc ảnh xám), cv2.imshow(), cv2.imwrite(),.
   Thao tác với Video: Dùng cap = cv2.VideoCapture() (mở file hoặc dùng số 0 cho webcam), cap.read() để lấy frame và cv2.VideoWriter() để ghi video,. Bạn có thể lấy thông số của video như số frame trên giây bằng cap.get(5) và tổng số khung hình bằng cap.get(7).
   Các thuộc tính của ảnh: Lấy kích thước bằng img.shape (trả về height, width, channels), tổng điểm ảnh img.size, và thao tác với giá trị pixel bằng img[y, x].
   Chuyển đổi không gian màu: Hàm cv2.cvtColor(src, code). Phổ biến là cv2.COLOR_BGR2GRAY (sang ảnh xám) .
   Cắt ảnh (Crop): Không có hàm cắt riêng, ta lấy trực tiếp một phần của ma trận numpy: crop = img[y1:y2, x1:x2].

2. Xử lý điểm ảnh và Biến đổi hình học (Chương 2)

   Chỉnh độ sáng và tương phản: Dùng hàm cv2.convertScaleAbs(image, alpha, beta) trong đó alpha điều chỉnh tương phản và beta điều chỉnh độ sáng.
   Tạo ảnh âm bản: Đơn giản bằng phép toán 255 - image.
   Dịch chuyển (Translation): Tạo ma trận tịnh tiến 2x3 M chứa tham số tx,ty, sau đó dùng cv2.warpAffine(img, M, (width, height)).
   Xoay ảnh (Rotation): Tạo ma trận xoay bằng M = cv2.getRotationMatrix2D(center, angle, scale) và xoay bằng cv2.warpAffine.
   Biến đổi phối cảnh (Perspective Transform): Tìm ma trận 3x3 M = cv2.getPerspectiveTransform(pts1, pts2) và gọi cv2.warpPerspective(img, M, (w,h)).

3. Tách biên và Khám phá đặc trưng (Chương 3)

   Lọc nhiễu ảnh: Dùng cv2.GaussianBlur(img, (3,3), 0) hoặc cv2.medianBlur(img, 5) trước khi tách biên để có kết quả tốt hơn,.
   Tách biên Gradient (Sobel): Chạy cv2.Sobel() theo 2 hướng x và y, lấy giá trị tuyệt đối bằng cv2.convertScaleAbs(), rồi tính tổng trọng số hai mảng bằng cv2.addWeighted(),.
   Tách biên đạo hàm bậc 2 (Laplace): Hàm cv2.Laplacian().
   Tách biên Canny: Đưa ra đường biên mảnh, nét và lọc nhiễu tốt. Dùng hàm cv2.Canny(image, lower_threshold, upper_threshold).

4. Phân vùng ảnh, Hình thái học và Contour (Chương 4)

   Phân ngưỡng ảnh (Thresholding):
   Phân ngưỡng tĩnh: cv2.threshold(img, threshold, max_value, type) với các type như THRESH_BINARY, THRESH_BINARY_INV, THRESH_TRUNC, THRESH_TOZERO.
   Phân ngưỡng tối ưu (Otsu): Cộng thêm cờ cv2.THRESH_OTSU vào thuộc tính của cv2.threshold() để máy tự động tìm ngưỡng tối ưu phù hợp cho ảnh có histogram 2 đỉnh.
   Phân ngưỡng thích nghi (Adaptive Thresholding): Khắc phục nhược điểm ánh sáng không đều. Dùng cv2.adaptiveThreshold() với phương pháp ADAPTIVE_THRESH_MEAN_C hoặc ADAPTIVE_THRESH_GAUSSIAN_C,.
   Đường bao đối tượng (Contour):
   Tìm và vẽ: Lấy danh sách contour qua cv2.findContours() và vẽ lên ảnh bằng cv2.drawContours(),.
   Tính toán Contour: Có thể dùng cv2.contourArea(contour) để tìm diện tích, hoặc cv2.boundingRect(contour) để tạo hình chữ nhật bao quanh đối tượng.

# ===================================================

# ĐỀ ÔN TẬP THI THỰC HÀNH - THỊ GIÁC MÁY TÍNH

# ===================================================

# Cho ảnh 'onhieuoi.jpg'. Thực hiện các yêu cầu sau:

PHẦN 1 - Thao tác cơ bản (Chương 1):

# 1. Đọc ảnh màu và ảnh xám (dùng flag)

# 2. In ra: kích thước, tổng pixel, giá trị pixel tại [50,50]

# 3. Cắt ảnh lấy vùng [100:300, 100:400]

# 4. Chuyển sang HSV và lưu ảnh xám ra file 'ket_qua.jpg'

#

PHẦN 2 - Xử lý điểm ảnh (Chương 2):

# 5. Tăng độ sáng (beta=50) và tương phản (alpha=1.5)

# 6. Tạo ảnh âm bản

# 7. Xoay ảnh 45 độ quanh tâm, scale=1

#

PHẦN 3 - Tách biên (Chương 3):

# 8. Lọc nhiễu Gaussian

# 9. Tách biên Sobel (x+y), Laplace, Canny(50,150)

#

PHẦN 4 - Phân vùng + Contour (Chương 4):

# 10. Phân ngưỡng Otsu, Adaptive

# 11. Tìm contour RETR_EXTERNAL

# 12. Vẽ contour đỏ + boundingRect xanh lá

# 13. In ra số lượng contour và diện tích từng contour

#

# Hiển thị tất cả kết quả bằng matplotlib

# ===================================================
