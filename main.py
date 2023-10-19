import os
import sys

from capture import capture


def main():
    args = sys.argv
    if len(args) < 2:
        print("Please specify the video file path as an argument")
        sys.exit(1)

    color = False
    strict = False
    if len(args) > 2:
        for arg in args[2:]:
            if arg == "--color" or arg == "-c":
                color = True
            elif arg == "--strict" or arg == "-s":
                strict = True
            else:
                print(f"Unknown option: {arg}")

    video_path = args[1]
    if not os.path.exists(video_path):
        print(f"File not found: {video_path}")
        sys.exit(1)

    if not video_path.endswith((".mp4", ".avi", ".mov")):
        print(
            "File format not supported:",
            os.path.splitext(os.path.basename(video_path))[1],
            "\nSupported formats: mp4, avi, mov",
        )
        sys.exit(1)

    capture(video_path, color, strict)


if __name__ == "__main__":
    main()
