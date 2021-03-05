import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
flag = 1
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
while flag:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print("Data", obj.data)
        flag=flag-1
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)     
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break