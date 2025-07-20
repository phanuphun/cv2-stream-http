# README
This repository i tried to learning about thread in python by using cv2 to straming http camera webcam
- set backend cv2 at the `/camera/camStream` directory
- check open camera by run  `/camera/camCheck.py`

## Installation and Setup 
- Create venv or you can use python global interpreter to compile 
- Create `.env` and set env variables 
    - CAM_ID
    - CAM_WIDTH
    - CAM_HEIGHT
    - CAM_FPS
- Run `app-bottle.py` to start server (http://localhost:8080)

## API Path
- GET `/` : health check 
- GET `/stream` : open camera streaming  