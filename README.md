# Minecraft Coords Capture

マインクラフトの動画から、座標が映ったシーンをキャプチャーします。

## Tesseract OCR のインストール

OCR エンジンを用いた文字認識を行います。

Tesseract OCR をインストールしてください。
インストーラーは[こちらからダウンロード](https://github.com/UB-Mannheim/tesseract/wiki)することができます。

Windows で PC 全体にデフォルトパス (`C:\Program Files\Tesseract-OCR`) でインストールを行うことを想定して、プログラム上から PATH を通しています。
インストール先を変更する場合は、`win_config.py`のパスを変更してください。

## 使い方

Python3 の環境が必要です。

venv などの仮想環境を使用することを推奨します。

### venv を用いた仮想環境の構築 (Windows)

```bash
python -m venv venv
.\venv\Scripts\activate
```

### インストール

git を用いてクローンし、必要なライブラリをインストールします。

```bash
git clone https://github.com/Yusuke4869/MinecraftCoordsCapture
cd MinecraftCoordsCapture
pip install -r requirements.txt
```

ページ上方の緑色の Code ボタンから、zip でダウンロードして解凍することもできます。

```bash
cd MinecraftCoordsCapture
pip install -r requirements.txt
```

### 実行

動画ファイルを引数に与えて実行します。

```bash
python main.py video.mp4
```

### オプション

|短いオプション|長いオプション|実行内容|

|:--|:--|:--|
|`-c`|`--color`|カラーで画像解析を行います。設定しない場合はグレースケールで解析を行います。|
|`-s`|`--strict`|グレースケールでの解析に加え、カラーでの解析も行い検出の精度を高めます。実行時間が大幅に増加します。|

## 検出の仕組み

1 秒ごとに動画を解析し、`minecraft` という文字列が検出されたフレームをキャプチャーします。
そのため、タイトル画面などでも検出することがありますので、注意してください。

また、動画の解像度のまま解析を行っているため、解像度が高いほど実行時間も増加します。
必要に応じて解像度を下げてから実行してください。

### 画像の保存

検出された画像は、`./img` ディレクトリにカラーで保存されます。
大量の画像が連続して保存されることがあるため、連続した 1 分間のシーンはサブディレクトリに保存されます。

## 不具合報告など

不具合報告などは気軽に Issue でお寄せください。
機能追加、修正などの Pull Request も歓迎します。

## License

MIT License
