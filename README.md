# README
This repository i tried to learning about thread in python by using `opencv2` to straming http camera webcam, using `Bottle` to create minimal API.
- set backend cv2 at the `/camera/camStream` directory
- check open camera by run  `/camera/camCheck.py`

## Installation and Setup 
- Create venv or you can use python global interpreter to compile 
- Create `.env` and set env variables 
    - CAM_ID
    - CAM_WIDTH
    - CAM_HEIGHT
    - CAM_FPS
- Run `pip install -r requirements.txt` to install dependencies.
- Run `app.py` to start server (http://localhost:8080)

## API Path
- GET `/` : health check 
- GET `/stream` : open camera streaming  
