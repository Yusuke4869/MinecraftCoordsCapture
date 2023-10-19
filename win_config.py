import os


"""
Tesseractのパスを通す（Windowsの場合）

デフォルトパスは以下の通り
C:\\Program Files\\Tesseract-OCR

自分のユーザーにのみインストールした場合は以下のパスになる
C:\\Users\\<User Name>\\AppData\\Local\\Programs\\Tesseract-OCR
"""


def win_config():
    if os.name != "nt":
        return

    tesseract_path = "C:\\Program Files\\Tesseract-OCR"
    if tesseract_path not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + tesseract_path
