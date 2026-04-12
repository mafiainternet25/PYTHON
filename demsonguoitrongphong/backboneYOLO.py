from flask import Flask, render_template, Response, request
import cv2
from ultralytics import YOLO
import numpy as np
app = Flask(__name__)
model = YOLO("yolov8n.pt")
count_var = 0
@app.route("/")
def index():
    return render_template("classroom.html")
@app.route("/classroom", methods=['GET', 'POST'])
def classroom():
    ip_address = None
    if request.method == 'POST':
        ip_address = request.form.get('ip')
    return render_template("classroom.html", ip_address=ip_address)
def generate_frames(camera_index):
    global count_var
    cap = cv2.VideoCapture(camera_index)
    while True:
        ret, frame = cap.read()
        if not ret:break
        frame = cv2.resize(frame, (640, 480))
        results = model(frame)
        result = results[0]
        classes = result.boxes.cls.cpu().numpy().astype(int)
        boxes = result.boxes.xyxy.cpu().numpy().astype(int)
        people_centroids = []
        for i in range(len(classes)):
            if classes[i] == 0:  
                x1, y1, x2, y2 = boxes[i]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)
                people_centroids.append((cx, cy))
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
        count_var = len(people_centroids)
        cv2.putText(frame,f"People: {count_var}",(10, 30),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),2,)
        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
        )
@app.route("/video_feed")
def video_feed():
    ip_address = request.args.get("ip", "0")
    if ip_address == "0":ip_address = 0
    return Response(generate_frames(ip_address),mimetype="multipart/x-mixed-replace; boundary=frame",)
@app.route("/count")
def count():
    return str(count_var)
if __name__ == "__main__":app.run(debug=True, port=8000)