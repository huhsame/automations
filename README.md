
# Automations

### Extract Audio
Downloads the audio from a YouTube URL.
```bash
python3 extract_audio.py [YouTubeUrl]
```

### YT Playlist Transcript to Text
Downloads and merges all English transcripts from a YouTube playlist URL.
```bash
python3 yt_pl_transcript.py [YouTube Playlist Url]
```

### Combine Text Files
Combines all the `.txt` files in the current folder into a single `.txt` file.
```bash
python3 combine_txt.py
```

### File Renamer with Timestamp
Renames video and image files in a specified directory by adding a timestamp prefix based on the file's last modification time.
```bash
python rename.py [directory] --extensions [.ext1] [.ext2] ...
```
Example:
```bash
python rename.py /path/to/folder --extensions .mp4 .jpg .png
```
