from bottle import Bottle, run, request, response
from datetime import datetime
import cv2
from config import CAM_ID, CAM_WIDTH, CAM_HEIGHT, CAM_FPS
from camera.camStream import CamStream

app = Bottle()

@app.route('/')
def index():
    response.content_type = 'application/json'
    return {
        "service": "opencv2-threading",
        "status": "running",
        "timestamp": datetime.now().isoformat(),
    }

@app.route('/stream', method='GET')
def stream():
    response.content_type = 'multipart/x-mixed-replace; boundary=frame'
    def generate():
        while True:
            frame = cam_thread.latest_frame
            if frame is None:
                continue

            (flag, encodedImage) = cv2.imencode(".jpg", frame)
            if not flag:
                continue

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

    return generate()

@app.route('/snapshot', method='GET')
def snapshot():
    response.content_type = 'image/jpeg'
    frame = cam_thread._snap_shot()
    if frame is not None:
        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        if flag:
            return encodedImage.tobytes()
    return b''

@app.route('/stop', method='GET')
def stop():
    cam_thread.stop()
    response.content_type = 'application/json'
    return {
        "status": "stopped",
        "timestamp": datetime.now().isoformat(),
    }

if __name__ == "__main__":
    cam_thread = CamStream(CAM_ID, CAM_WIDTH, CAM_HEIGHT, CAM_FPS)
    run(app, 
        host="localhost", 
        port=8080 , 
        server='paste', # Use 'paste' server for use multi threading (need to install paste additional package)
        debug=True,
        reloader=False
        )