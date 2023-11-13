
# 자동화 스크립트

### 오디오 추출
YouTube URL에서 오디오를 다운로드합니다.
```bash
python3 extract_audio.py [YouTubeUrl]
```

### YouTube 재생목록 자막을 텍스트로
YouTube 재생목록 URL에서 모든 영어 자막을 다운로드하고 병합합니다.
```bash
python3 yt_pl_transcript.py [YouTube Playlist Url]
```

### 텍스트 파일 병합
현재 폴더의 모든 `.txt` 파일을 하나의 `.txt` 파일로 병합합니다.
```bash
python3 combine_txt.py
```

### 타임스탬프 파일 이름 변경
지정된 디렉토리의 비디오 및 이미지 파일 이름에 파일의 마지막 수정 시간을 기반으로 한 타임스탬프 접두사를 추가하여 이름을 변경합니다.
```bash
python rename.py [directory] --extensions [.ext1] [.ext2] ...
```
예시:
```bash
python rename.py /path/to/folder --extensions .mp4 .jpg .png
```
