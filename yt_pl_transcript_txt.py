import os
import sys
from pytube import Playlist
from langchain.document_loaders import YoutubeLoader
from datetime import datetime

loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=QsYGlZkevEg", add_video_info=True
)
loader.load()


def download_transcripts(playlist_url):
    playlist = Playlist(playlist_url)
    playlist_name = playlist.title

    now = datetime.now().strftime("%Y.%m.%d_%H:%M:%S")
    base_path = "/Users/huh/Dropbox (Personal)/!  New"
    target_path = "/@ Resource/Transcript"
    output_path = base_path + target_path
    output_file = os.path.join(output_path, f"{now} - {playlist_name}.txt")
    all_transcripts = ""

    for video in playlist.videos:
        # print(vars(video))

        loader = YoutubeLoader.from_youtube_url(video.watch_url, add_video_info=True)
        loaded_documents = loader.load()
        if loaded_documents:
            video_document = loaded_documents[0]
            all_transcripts += f"{video_document.metadata['title']} \n\n {video_document.page_content} \n\n\n"
            print(f"Loaded: {video_document.metadata['title']}")
        else:
            print(f"No transcript")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(all_transcripts)

    print(f"{playlist_name}.txt has been downloaded.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 yt_pl_transcript_txt.py [YouTube Playlist URL]")
    else:
        playlist_url = sys.argv[1]
        download_transcripts(playlist_url)
