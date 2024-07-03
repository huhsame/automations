import os
import sys
import pandas as pd
from pytube import YouTube
import instaloader
from moviepy.editor import VideoFileClip


def sanitize_filename(name):
    return "".join(
        char for char in name if char.isalnum() or char in [" ", "-", "_"]
    ).rstrip()


def trim_video(video_path, max_duration=29.5):
    clip = VideoFileClip(video_path)
    if clip.duration > max_duration:
        clip = clip.subclip(0, max_duration)
        clip.write_videofile(video_path)
        print(f"Trimmed video to {max_duration} seconds: {video_path}")
    clip.close()


def download_youtube_video(url, download_folder):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    safe_title = sanitize_filename(yt.title)
    safe_author = sanitize_filename(yt.author)
    filename = f"{safe_author} - {safe_title}.mp4"
    video_path = os.path.join(download_folder, filename)
    stream.download(output_path=download_folder, filename=filename)
    print(f"Downloaded YouTube video: {filename}")
    trim_video(video_path)


def download_instagram_video(url, download_folder):
    L = instaloader.Instaloader(
        download_videos_only=True,
        download_pictures=False,
        download_video_thumbnails=False,
    )
    shortcode = url.split("/")[-2]
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    video_url = post.video_url
    if video_url:
        video_filename = f"{post.owner_username} - {shortcode}.mp4"
        caption_filename = f"{post.owner_username} - {shortcode}.txt"
        video_path = os.path.join(download_folder, video_filename)
        # 동영상 다운로드
        L.download_video(url=video_url, target=video_path)
        print(f"Downloaded Instagram video: {video_filename}")
        trim_video(video_path)
        # 캡션 저장
        with open(
            os.path.join(download_folder, caption_filename), "w", encoding="utf-8"
        ) as file:
            file.write(post.caption if post.caption else "No caption")
        print(f"Saved caption for {video_filename}")


def download_video(url, download_folder):
    if "youtube.com" in url or "youtu.be" in url:
        download_youtube_video(url, download_folder)
    # elif "instagram.com" in url:
    # download_instagram_video(url, download_folder)


def handle_csv(csv_filename, csv_folder, download_folder):
    csv_path = os.path.join(csv_folder, csv_filename)
    df = pd.read_csv(csv_path)

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for index, row in df.iterrows():
        url = row.iloc[0]
        download_video(url, download_folder)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_arg = sys.argv[1]
        download_folder = (
            "/Users/huh/Dropbox (Personal)/!  New/컨텐츠/kpopai/viggle/따라할영상"
        )
        csv_folder = "/Users/huh/Dropbox (Personal)/!  New/컨텐츠/kpopai/viggle/csv"

        if ".csv" in input_arg:
            handle_csv(input_arg, csv_folder, download_folder)
        elif (
            "youtube.com" in input_arg
            or "youtu.be" in input_arg
            or "instagram.com" in input_arg
        ):
            download_video(input_arg, download_folder)
        else:
            print(
                "Invalid input. Please provide a valid YouTube or Instagram link, or a CSV filename."
            )
    else:
        print("Please provide an input.")
