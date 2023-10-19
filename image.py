import os

import cv2
from PIL import Image


# 画像形式変換
def opencv2pil(in_image):
    new_image = in_image.copy()
    if new_image.ndim == 2:
        pass
    elif new_image.shape[2] == 3:
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    else:
        return None
    new_image = Image.fromarray(new_image)
    return new_image


# 画像出力
def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode="w+b") as f:
                n.tofile(f)
    except Exception as e:
        print(e)
