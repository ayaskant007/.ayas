import cv2
import numpy as np
import io
from PIL import Image, ImageTk

MU_MAGIC_HDR = b'AYAS_FORMAT_2026'

def apply_comic_effect(path_x):
    img_z = cv2.imread(path_x)
    clr_a = cv2.bilateralFilter(img_z, 9, 250, 250)
    gry_b = cv2.cvtColor(img_z, cv2.COLOR_BGR2GRAY)
    blr_c = cv2.medianBlur(gry_b, 7)
    edgs_d = cv2.adaptiveThreshold(blr_c, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
    res_img = cv2.bitwise_and(clr_a, clr_a, mask=edgs_d)
    return res_img

def save_ayas(img_cv_z, out_p):
    _, buf_q = cv2.imencode('.png', img_cv_z)
    bytes_r = buf_q.tobytes()

    with open(out_p, 'wb') as fh:
        fh.write(MU_MAGIC_HDR)
        fh.write(bytes_r)

def load_ayas(fp_s):
    with open(fp_s, 'rb') as fh2:
        hdr_t = fh2.read(len(MU_MAGIC_HDR))
        if hdr_t != MU_MAGIC_HDR:
            raise ValueError("Not a valid .ayas file type!")

        bts_u = fh2.read()
        arr_v = np.frombuffer(bts_u, np.uint8)
        img_w = cv2.imdecode(arr_v, cv2.IMREAD_COLOR)
        return cv2.cvtColor(img_w, cv2.COLOR_BGR2RGB)