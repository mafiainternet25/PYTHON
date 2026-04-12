# BÁO CÁO CHI TIẾT ĐỀ TÀI: ĐẾM SỐ NGƯỜI TRONG PHÒNG BẰNG YOLOv8 + FLASK

## 1. Thông tin tổng quan

- Tên đề tài: Đếm số người trong phòng theo thời gian thực.
- Mục tiêu: Xây dựng hệ thống cho phép nhập nguồn video (webcam hoặc IP camera), phát hiện người trong khung hình và hiển thị số lượng người liên tục trên giao diện web.
- Bài toán giải quyết: Tự động hóa việc giám sát mật độ người trong một khu vực (phòng học, phòng họp, phòng thực hành, ...).

## 2. Mục tiêu cụ thể

Hệ thống cần đạt các yêu cầu sau:

1. Nhận video stream từ webcam hoặc camera mạng.
2. Phát hiện đối tượng person bằng mô hình YOLOv8.
3. Đếm số người trong mỗi frame.
4. Hiển thị video đã vẽ khung (bounding box) và tâm đối tượng.
5. Cập nhật số lượng người theo thời gian thực trên web.

## 3. Công nghệ sử dụng

- Ngôn ngữ chính: Python
- Framework web: Flask
- Thị giác máy tính: OpenCV (cv2)
- Mô hình phát hiện đối tượng: Ultralytics YOLOv8 (file trong project: yolov8n.pt, có sẵn thêm yolov8m.pt)
- Front-end: HTML + Bootstrap + JavaScript (AJAX polling)

## 4. Cấu trúc thư mục chính

Trong thư mục demsonguoitrongphong/:

- backboneYOLO.py: chương trình backend chính, xử lý video + suy luận + API Flask.
- templates/base.html: layout nền cho giao diện.
- templates/classroom.html: trang nhập IP camera và hiển thị video + bảng đếm người.
- static/style.css: style cơ bản.
- yolov8n.pt, yolov8m.pt: trọng số mô hình YOLOv8.

## 5. Phân tích kiến trúc hệ thống

Ứng dụng được tổ chức theo mô hình client-server:

1. Người dùng truy cập web và nhập nguồn camera.
2. Flask nhận thông tin nguồn video.
3. Hàm tạo frame đọc từng ảnh từ OpenCV, chạy YOLO để phát hiện người.
4. Kết quả frame đã xử lý được stream ngược lại trình duyệt qua MIME multipart/x-mixed-replace.
5. Trình duyệt định kỳ gọi endpoint /count mỗi 500ms để lấy số người hiện tại và cập nhật bảng.

## 6. Mô tả chi tiết code backend (backboneYOLO.py)

### 6.1 Khởi tạo hệ thống

- Tạo app Flask:

```python
app = Flask(__name__)
```

- Nạp mô hình YOLO:

```python
model = YOLO("yolov8n.pt")
```

- Biến toàn cục lưu kết quả đếm:

```python
count_var = 0
```

### 6.2 Các route Flask

#### a) /

- Chức năng: hiển thị giao diện mặc định.
- Trả về template classroom.html.

#### b) /classroom (GET, POST)

- Chức năng:
  - GET: tải trang nhập camera.
  - POST: nhận dữ liệu trường ip từ form.
- Sau khi nhận dữ liệu, truyền ip_address ra template để hiển thị và khởi tạo video stream.

#### c) /video_feed

- Chức năng: trả về luồng ảnh JPEG liên tục để hiển thị như video.
- Cơ chế:
  - Lấy query param ip.
  - Nếu ip == "0" thì gán camera index bằng 0 (webcam mặc định).
  - Gọi hàm sinh frame và stream về trình duyệt.

#### d) /count

- Chức năng: trả về số người hiện tại đang được đếm (count_var).
- Được JavaScript gọi lặp lại theo chu kỳ 500ms.

### 6.3 Hàm xử lý chính generate_frames(camera_index)

Quy trình xử lý mỗi frame:

1. Mở nguồn video:
   - cap = cv2.VideoCapture(camera_index)
2. Đọc frame liên tục trong vòng lặp while True.
3. Resize frame về kích thước 640x480 để ổn định tốc độ và giao diện.
4. Chạy suy luận:
   - results = model(frame)
5. Lấy danh sách class và tọa độ box.
6. Lọc class 0 (tương ứng person trong COCO).
7. Vẽ khung bao quanh và tính tâm mỗi người:
   - Rectangle màu đỏ.
   - Tâm đối tượng (centroid) bằng hình tròn.
8. Đếm số người:
   - count_var = len(people_centroids)
9. Vẽ text số lượng lên frame (People: N).
10. Mã hóa frame sang JPEG và yield dữ liệu theo định dạng stream HTTP.

## 7. Mô tả giao diện người dùng

Giao diện trong classroom.html gồm 2 khối:

1. Form nhập IP và port camera
   - Ô nhập ip.
   - Nút Create gửi POST đến /classroom.

2. Khối hiển thị dữ liệu
   - Bảng gồm 2 cột:
     - IP Address And PORT
     - Number Of People In Room
   - Khung video (<img>) lấy nguồn từ endpoint /video_feed.

JavaScript phía client:

- Dùng XMLHttpRequest gọi /count mỗi 500ms.
- Nếu nhận được response, cập nhật trực tiếp vào phần tử có id='count'.

## 8. Cách cài đặt và chạy hệ thống

### 8.1 Yêu cầu môi trường

- Python 3.8 trở lên (khuyến nghị 3.10+)
- Webcam hoặc đường dẫn stream hợp lệ
- Các thư viện:
  - flask
  - opencv-python
  - ultralytics
  - numpy

### 8.2 Cài đặt nhanh

```bash
python -m venv venv
source venv/bin/activate
pip install flask opencv-python ultralytics numpy
```

### 8.3 Chạy chương trình

Trong thư mục demsonguoitrongphong/:

```bash
python backboneYOLO.py
```

Ứng dụng mặc định chạy tại:

```text
http://127.0.0.1:8000
```

## 9. Đánh giá kết quả

### 9.1 Ưu điểm

1. Kiến trúc đơn giản, dễ triển khai và mở rộng.
2. Có khả năng stream video thời gian thực trên web.
3. Đếm người trực tiếp dựa trên mô hình học sâu, không cần tách nền.
4. Tích hợp nhanh với webcam hoặc nguồn IP camera.

### 9.2 Hạn chế hiện tại

1. Biến count_var là biến toàn cục:
   - Nếu có nhiều client đồng thời thì giá trị đếm có thể bị dùng chung.
2. Chưa có xử lý ngoại lệ mạnh:
   - Khi IP camera sai hoặc mất kết nối, giao diện chưa có thông báo lỗi rõ ràng.
3. Chưa tối ưu hiệu năng:
   - Mỗi frame đều suy luận đầy đủ, có thể gây tải cao trên máy yếu.
4. Chưa lưu lịch sử:
   - Hệ thống chỉ hiện tại, không lưu log theo thời gian.
5. Chưa tách model và chuỗi xử lý:
   - Tất cả logic đang nằm trong một file backend.

## 10. Hướng phát triển đề xuất

1. Hỗ trợ nhiều phòng hoặc nhiều camera đồng thời, mỗi camera một bộ đếm riêng.
2. Lưu lịch sử vào CSDL (SQLite hoặc PostgreSQL) để thống kê theo giờ hoặc ngày.
3. Thêm cảnh báo vượt ngưỡng người (email, âm thanh, websocket).
4. Chuyển polling sang WebSocket để cập nhật count realtime hiệu quả hơn.
5. Bổ sung xác thực đăng nhập và phân quyền quản trị.
6. Đóng gói Docker để triển khai dễ dàng.
7. Hỗ trợ chọn model (yolov8n, yolov8m) ngay trên giao diện.

## 11. Kết luận

Đề tài đã xây dựng thành công một hệ thống đếm số người trong phòng theo thời gian thực sử dụng YOLOv8 và Flask. Hệ thống đáp ứng các chức năng cơ bản: kết nối nguồn video, phát hiện người, đếm và hiển thị kết quả trên web. Đây là nền tảng tốt để phát triển thành bài toán giám sát thông minh với quy mô lớn hơn trong tương lai.

## 12. Phụ lục: Luồng dữ liệu tóm tắt

1. Người dùng nhập IP/PORT và gửi form POST.
2. Server nhận IP và tạo luồng /video_feed.
3. OpenCV đọc frame, YOLO detect person, sau đó tính số lượng.
4. Server stream frame đã annotate lên giao diện.
5. Trình duyệt gọi /count mỗi 500ms để cập nhật bảng số người.
