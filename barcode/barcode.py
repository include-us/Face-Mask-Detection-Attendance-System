import cv2
import pyzbar.pyzbar as pyzbar


class barcode_read(object):
    def reader(self):
        flag = 1
        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN
        while flag:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                string = obj.data
                cv2.putText(frame, str(obj.data), (50, 50),
                            font, 2, (255, 0, 0), 3)
                flag = flag-1
                cap.release()
                cv2.destroyAllWindows()
                return str(string)[2:-1]
            cv2.imshow("Barcode Scanner", frame)

            key = cv2.waitKey(1)
            if key == 27:
                break
