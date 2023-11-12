import sys
from pytube import YouTube
from datetime import datetime


def shorten_title(title, max_length):
    # 제목을 지정된 최대 길이에 맞추어 자릅니다.
    return title if len(title) <= max_length else title[: max_length - 3] + "..."


def download_youtube_audio(url):
    base_path = "/Users/huh/Dropbox (Personal)/!  New"
    path = "/@ Resource/Audio"
    output_path = base_path + path
    # 파일 이름에 사용할 수 있는 최대 길이를 지정합니다.

    yt = YouTube(url)
    title = yt.title

    max_title_length = 100
    short_title = shorten_title(title, max_title_length)
    now = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
    filename = f"{now} - {short_title}.mp3"

    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path, filename=filename)
    print(f"{filename} has downloaded at {path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python3 extract_audio.py [YouTube URL]")
    else:
        url = sys.argv[1]
        download_youtube_audio(url)
