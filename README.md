# 👥 People Counting System (YOLOv8 + Flask)

## 📌 Overview

A real-time people counting system using YOLOv8 and Flask.
The application detects and counts people from a webcam or IP camera and displays the result on a web interface.

---

## 🚀 Technologies

* Python
* Flask
* OpenCV
* Ultralytics YOLOv8
* HTML, CSS, JavaScript (AJAX)

---

## ⚙️ Features

* Input video source (webcam or IP camera)
* Detect people in real-time
* Count number of people per frame
* Display video with bounding boxes
* Update count continuously on web

---

## 📂 Structure

* `backboneYOLO.py` – main backend (Flask + detection)
* `templates/` – HTML pages
* `static/` – CSS
* `yolov8n.pt`, `yolov8m.pt` – model weights

---

## ▶️ Run

```bash
python -m venv venv
source venv/bin/activate
pip install flask opencv-python ultralytics numpy
python backboneYOLO.py
```

Open: http://127.0.0.1:8000

---

## ⚠️ Notes

* Default uses webcam (`0`) or IP camera stream
* Do not upload API keys or sensitive data

---

## 👨‍💻 Author

Quoc Truong
