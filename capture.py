import os
import sys
import time

import cv2
import pyocr
from autocorrect import Speller

from win_config import win_config
from image import opencv2pil, imwrite


win_config()

# OCRエンジン取得
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
speller = Speller(lang="en")


def capture(
    video_path: str, color: bool = False, strict: bool = False, spell: bool = False
):
    video_title = os.path.splitext(os.path.basename(video_path))[0]

    capture = cv2.VideoCapture(video_path)
    fps = capture.get(cv2.CAP_PROP_FPS)

    length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT) / fps)
    len_m, len_s = divmod(length, 60)
    len_h, len_m = divmod(len_m, 60)
    print(
        f"Processing video: {os.path.basename(video_path)}",
        f"({len_h:02d}:{len_m:02d}:{len_s:02d})",
    )

    os.makedirs("./img", exist_ok=True)
    os.makedirs(f"./img/{video_title}", exist_ok=True)

    i = 0
    count = 0
    dir_time = -100
    dir_name = video_title
    start = time.time()
    while True:
        ret, frame = capture.read()
        if not ret:
            break

        # 1秒ごとに画像処理を行う
        if int(i % fps) != 0:
            i += 1
            continue

        seconds = int(i // fps)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)

        progress = seconds / length * 100
        now = time.time()
        pro_m, pro_s = divmod(int(now - start), 60)
        pro_h, pro_m = divmod(pro_m, 60)
        print(
            f"\r{h:02d}:{m:02d}:{s:02d} {progress:5.1f}% "
            + f"(Processing time: {pro_h:02d}:{pro_m:02d}:{pro_s:02d})",
            end="",
        )

        img = (
            opencv2pil(frame)
            if color or strict
            else opencv2pil(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        )
        txt = tool.image_to_string(img, lang="eng", builder=builder)
        if spell:
            txt = speller(txt)

        exists = False
        if "minecraft" in txt.lower():
            exists = True

        if not exists and strict:
            img = opencv2pil(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
            txt = tool.image_to_string(img, lang="eng", builder=builder)
            if spell:
                txt = speller(txt)

            if "minecraft" in txt.lower():
                exists = True

        if exists:
            # 60秒ごとにディレクトリを分けて画像を保存
            if seconds - dir_time > 60:
                dir_time = seconds
                dir_name = f"{video_title}_{h:02d}{m:02d}{s:02d}"
                os.makedirs(f"./img/{video_title}/{dir_name}", exist_ok=True)
                imwrite(
                    f"./img/{video_title}/{video_title}_{h:02d}{m:02d}{s:02d}.png",
                    frame,
                )

            count += 1
            imwrite(
                f"./img/{video_title}/{dir_name}/{video_title}_{h:02d}{m:02d}{s:02d}.png",
                frame,
            )

        i += 1

    print(f"\nExtracted images: {count}")
