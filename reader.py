import cv2
import numpy as np
import io
from PIL import Image, ImageTk

MAGIC_HEADER = b'AYAS_FORMAT_2026'

def apply_comic_effect(image_path):
    img = cv2.imread(image_path)
    color = cv2.bilateralFilter(img, 9, 250, 250)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
    comic_img = cv2.bitwise_and(color, color, mask=edges)
    return comic_img

def save_ayas(cv_img, output_path):
    _, buffer = cv2.imencode('.png', cv_img)
    img_bytes = buffer.tobytes()

    with open(output_path, 'wb') as f:
        f.write(MAGIC_HEADER)
        f.write(img_bytes)

def load_ayas(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(len(MAGIC_HEADER))
        if header!=MAGIC_HEADER:
            raise ValueError("Not a valid .ayas file type!")
        
        img_bytes = f.read()
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)