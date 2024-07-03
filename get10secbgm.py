import os
from moviepy.editor import VideoFileClip

def extract_audio(input_folder, output_folder='cut10'):
    # 결과 폴더 생성 (입력 폴더 안에)
    output_folder_path = os.path.join(input_folder, output_folder)
    os.makedirs(output_folder_path, exist_ok=True)
    
    # 지정된 폴더 내의 모든 파일을 순회
    for filename in os.listdir(input_folder):
        # 비디오 파일 확장자 확인
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + "_audio.mp3"
            output_path = os.path.join(output_folder_path, output_filename)

            # 결과 파일이 이미 존재하는지 확인
            if os.path.exists(output_path):
                print(f"Output file {output_filename} already exists, skipping {filename}")
                continue

            video_clip = VideoFileClip(video_path)
            
            # 비디오 길이 확인
            if video_clip.duration < 10:
                # 파일 삭제
                video_clip.close()
                os.remove(video_path)
                print(f"Deleted {filename} as its duration is {video_clip.duration} seconds")
            else:
                # 오디오 추출
                audio_clip = video_clip.audio.subclip(0, 10)
                
                # 오디오 파일 저장
                audio_clip.write_audiofile(output_path, codec='mp3')
                print(f"Extracted audio from {filename} to {output_filename}")
                
                # 리소스 해제
                audio_clip.close()
                video_clip.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_folder> [output_folder]")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2] if len(sys.argv) > 2 else 'cut10'
        extract_audio(input_folder, output_folder)
