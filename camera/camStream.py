import threading
import time
import cv2

from config import CAM_ID, CAM_WIDTH, CAM_HEIGHT, CAM_FPS
CAM_BACKEND = cv2.CAP_DSHOW  # or cv2.CAP_ANY

class CamStream: 
    def __init__(self, cam_id=CAM_ID ,width=CAM_WIDTH, height=CAM_HEIGHT, fps=CAM_FPS):
        self.cap = cv2.VideoCapture(cam_id, CAM_BACKEND)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        # self.cap.set(cv2.CAP_PROP_FPS, fps)

        self.running = True
        self.latest_frame = None
        self.thread = threading.Thread(target=self._update_frame)
        self.thread.start()

    def _update_frame(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.latest_frame = frame
            else:
                print("Error reading frame")
                time.sleep(0.1)
        time.sleep(0.1)

    def _snap_shot(self):
        if self.latest_frame is not None:
            return self.latest_frame.copy()
        return None

    def stop(self):
        self.running = False
        self.thread.join()
        self.cap.release()