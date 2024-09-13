import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from notifypy import Notify
import mediapipe
class Model:
    notification = Notify()
    def send_notification(self, title, message):
        self.notification.application_name = 'ComputerViewer'
        self.notification.title = title
        self.notification.message = message
        self.notification.send(block=False)    

    def __init__(self):
            self.cap = cv2.VideoCapture(0)
            self.detector = FaceMeshDetector(maxFaces=1)

    def is_cap_opened(self):
            return self.cap.isOpened()

    def get_face(self, img):
            _, faces = self.detector.findFaceMesh(img, draw=False)
            if faces:
                return faces[0]
            return None

    def get_img(self):
            _, img = self.cap.read()
            return img

    def update_distance(self):
        face = self.get_face(self.get_img())
        if face is not None:
            w_small, _ = self.detector.findDistance(face[145], face[374])  # Numbers that align to the left eye and right eye
            w_big = 6.3
            f = 1320
            distance = (w_big * f) / w_small
            return distance    