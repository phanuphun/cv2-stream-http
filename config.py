import os
from dotenv import load_dotenv
load_dotenv()

CAM_ID = int(os.getenv("CAM_ID", 0))
CAM_WIDTH = int(os.getenv("CAM_WIDTH", 1920))
CAM_HEIGHT = int(os.getenv("CAM_HEIGHT", 1080))
CAM_FPS = int(os.getenv("CAM_FPS", 60))