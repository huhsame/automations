import os
import argparse
from moviepy.editor import VideoFileClip


def convert_videos_to_gifs(
    folder_path, file_extensions, max_length, resize_factor=None, speed_factor=None
):
    for filename in os.listdir(folder_path):
        if any(filename.endswith(ext) for ext in file_extensions):
            video_path = os.path.join(folder_path, filename)
            video_clip = VideoFileClip(video_path)

            # 영상 길이 확인
            if video_clip.duration > max_length:
                print(f"Skipping {filename}: longer than {max_length} seconds")
                continue

            # 해상도 조절
            if resize_factor:
                video_clip = video_clip.resize(resize_factor)
            else:
                # 1080p 해상도 제한
                max_height = 1080
                if video_clip.h > max_height:
                    video_clip = video_clip.resize(height=max_height)

            # 속도 조절
            if speed_factor:
                video_clip = video_clip.speedx(factor=speed_factor)

            gif_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".gif")
            video_clip.write_gif(gif_path)

            print(f"Converted {video_path} to {gif_path}")
    print("Finished")


def main():
    parser = argparse.ArgumentParser(
        description="Convert video files to GIFs with specific constraints."
    )
    parser.add_argument(
        "folder_path", type=str, help="Path to the folder containing video files"
    )
    parser.add_argument(
        "--extensions",
        type=str,
        nargs="+",
        default=[".mov", ".mp4", ".MOV", ".MP4"],
        help="List of video file extensions to convert",
    )
    parser.add_argument(
        "--max_length", type=int, default=30, help="Maximum video length in seconds"
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

    convert_videos_to_gifs(
        args.folder_path, args.extensions, args.max_length, args.resize, args.speed
    )


if __name__ == "__main__":
    main()
