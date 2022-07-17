from threading import Thread
import cv2
from cv2 import waitKey 
import numpy as np

# global varaibles


class CameraOpenCV:
    def __init__(self):
        self.frame_global = np.empty(0)

    def cameraRead(self, windowName:str):
        cap = cv2.VideoCapture(0)
        self.cameras = True
        while True:
            ret, frame = cap.read()

            self.frame_global_base = frame

            cv2.imshow(windowName,frame)

            if waitKey (1) == 27 or self.cameras != True:
                break
        cv2.destroyAllWindows()

    def cameraStop(self):
        self.cameras = False
    
    def getFrameBase(self):
        return self.frame_global_base

    def getFrameCorner(self):
        pass
