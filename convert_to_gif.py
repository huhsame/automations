import os
import argparse
from moviepy.editor import VideoFileClip


def convert_videos_to_gifs(folder_path, resize_factor=None, speed_factor=None):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mov"):
            video_path = os.path.join(folder_path, filename)
            video_clip = VideoFileClip(video_path)

            # 해상도 조절
            if resize_factor:
                video_clip = video_clip.resize(resize_factor)

            # 속도 조절
            if speed_factor:
                video_clip = video_clip.speedx(factor=speed_factor)

            gif_path = os.path.join(folder_path, filename.replace(".mov", ".gif"))
            video_clip.write_gif(gif_path)

            print(f"Converted {video_path} to {gif_path}")


def main():
    parser = argparse.ArgumentParser(description="Convert MOV files to GIFs.")
    parser.add_argument(
        "folder_path", type=str, help="Path to the folder containing MOV files"
    )
    parser.add_argument(
        "--resize",
        type=float,
        default=None,
        help="Factor to resize the video (e.g., 0.5 for half size)",
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=None,
        help="Factor to adjust the speed (e.g., 2 for double speed)",
    )

    args = parser.parse_args()

    convert_videos_to_gifs(args.folder_path, args.resize, args.speed)


if __name__ == "__main__":
    main()
