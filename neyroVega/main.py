from ultralytics import YOLO
import cv2

#здесь мы загружаем версию YOLO
model = YOLO('yolov8n.pt')

#Указываем файл на видео
video_path = './file4.mp4'
cap = cv2.VideoCapture(video_path)

motion = True

while motion:
    ret, frame = cap.read()

    if ret:
        results = model.track(frame, persist=True)

        frame_ = results[0].plot()

        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break