import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import*
import cvzone
import numpy as np

model = YOLO('yolov8n.pt') #указываем версию YOLO, которую будем использовать

def RGB(event, x, y): #функция для отслеживания мышки, чтобы сдлеать отладку зоны очереди
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)
  
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
cap = cv2.VideoCapture('file4.mp4') #файл с камеры видеонаблюдения


my_file = open("find_object.txt", "r") #объекты которые мы будем обнаруживать
data = my_file.read()
class_list = data.split("\n") 


count = 0
tracker = Tracker()

area1 = [(102, 128), (628, 90), (660, 120), (300, 300)] #указываем зону очереди


while True:
    ret, frame = cap.read() #считываем кадры
    if not ret: #останавливаем, если кадров нет
        break

    frame = cv2.resize(frame, (1020, 500))
   
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    list = [] #общее колиечстов людей
    peo = [] #количество людей в зоне очереди
    for index, row in px.iterrows():
 
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        
        c = class_list[d]
        if 'person' in c: #обозначение боксов обнаружение человека
            list.append([x1, y1, x2, y2])
        bbox_idx = tracker.update(list)

        for bbox in bbox_idx:
            x3, y3, x4, y4, id = bbox
            result = cv2.pointPolygonTest(np.array(area1,np.int32), (x4, y4), False)
            if result >= 0:
                cv2.circle(frame, (x4, y4), 4, (100, 0, 255), -1)
                cv2.rectangle(frame, (x3, y3), (x4, y4), (255, 255, 255), 2)
                cvzone.putTextRect(frame, f'{id}', (x3, y3), 1, 1)
                peo.append([x1, y1, x2, y2])
        #print(len(peo), "- человек внутри очереди")
        with open("output.txt", "w") as file:
            file.write(str(len(peo))) #записываем количество людей в файл для дальнейщего использования
        peo = []

    cv2.polylines(frame, [np.array(area1, np.int32)], True, (0,255,0), 1)
    cv2.imshow("RGB", frame)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()

