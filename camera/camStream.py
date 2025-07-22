import threading
import time
import cv2

from config import CAM_ID, CAM_WIDTH, CAM_HEIGHT, CAM_FPS
CAM_BACKEND = cv2.CAP_DSHOW  

class CamStream: 
    def __init__(self, cam_id=CAM_ID ,width=CAM_WIDTH, height=CAM_HEIGHT, fps=CAM_FPS):
        self.cap = cv2.VideoCapture(cam_id, CAM_BACKEND)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        # สร้าง lock ขึ้นมาสำหรับ Instant เพื่อให้แต่ละ thread ผลัดกันเข้าถึง
        # Instant เดียวกันจะใช้กุญแจชุดเดียวกัน
        self.lock = threading.Lock()    

        self.running = True
        self.latest_frame = None
        self.thread = threading.Thread(target=self._update_frame)

        self.thread.start()

    def _update_frame(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                try: 
                    # ให้ thread แต่ละตัวรอก่อนจนกว่าจะได้รับการ relase จาก thread อื่น
                    self.lock.acquire()
                    self.latest_frame = frame.copy()
                finally:
                    self.lock.release()

            else:
                print("Error reading frame")
                time.sleep(0.1)
        time.sleep(0.1)

    def _snap_shot(self):
        try:
            self.lock.acquire()
            frame = self.latest_frame.copy() if self.latest_frame is not None else None
        finally:
            self.lock.release()
        return frame

    def stop(self):
        self.running = False
        self.thread.join()
        self.cap.release()