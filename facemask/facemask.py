from attendance.attendance import attendance
from json import decoder
import numpy as np
import keras
import keras.backend as k
from keras.layers import Conv2D, MaxPooling2D, SpatialDropout2D, Flatten, Dropout, Dense
from keras.models import Sequential, load_model
from keras.optimizers import Adam
from keras.preprocessing import image
import cv2
import datetime


class mask(object):
    def detect_mask(self):
        flag = 1
        while flag:
            self.mymodel = load_model('facemask/mymodel.h5')
            self.cap = cv2.VideoCapture(0)
            self.face_cascade = cv2.CascadeClassifier(
                'facemask/haarcascade_frontalface_default.xml')
            count_test = 0
            while self.cap.isOpened():
                _, img = self.cap.read()
                face = self.face_cascade.detectMultiScale(
                    img, scaleFactor=1.1, minNeighbors=4)
                #count_test = 0
                print(count_test)
                for(x, y, w, h) in face:
                    face_img = img[y:y+h, x:x+w]
                    cv2.imwrite('temp.jpg', face_img)
                    test_image = image.load_img(
                        'temp.jpg', target_size=(150, 150, 3))
                    test_image = image.img_to_array(test_image)
                    test_image = np.expand_dims(test_image, axis=0)
                    pred = self.mymodel.predict_classes(test_image)[0][0]
                    if pred == 1:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, 'NO MASK', ((x+w)//2, y+h+20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                        cv2.putText(img, 'MASK', ((x+w)//2, y+h+20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                        count_test += 1
                    datet = str(datetime.datetime.now())
                    cv2.putText(img, datet, (400, 450),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

                cv2.imshow('img', img)
                print(count_test)
                if count_test == 5:
                    print(True)
                    self.cap.release()
                    cv2.destroyAllWindows()
                    attendance().mark()
                    count_test = 0

                if cv2.waitKey(1) == ord('q'):
                    self.cap.release()
                    cv2.destroyAllWindows()
                    flag = 0
                    break
