import os
import datetime
import argparse


def add_timestamp_to_filenames(directory, file_extensions):
    # 폴더의 모든 파일을 나열
    files = os.listdir(directory)

    for file in files:
        # 파일 확장자 확인 (비디오 및 이미지 파일)
        if file.lower().endswith(file_extensions):
            # 파일의 전체 경로 구성
            file_path = os.path.join(directory, file)

            # 파일의 마지막 수정 시간 가져오기
            mod_time = os.path.getmtime(file_path)

            # 마지막 수정 시간을 기반으로 새 파일명 생성
            mod_datetime = datetime.datetime.fromtimestamp(mod_time)
            new_filename = mod_datetime.strftime("%Y%m%d_%H%M%S") + "_" + file

            # 새 파일 경로
            new_file_path = os.path.join(directory, new_filename)

            # 파일 이름 변경
            os.rename(file_path, new_file_path)
            print(f"Renamed {file} to {new_filename}")


def main():
    parser = argparse.ArgumentParser(
        description="Add timestamp to filenames of video and image files."
    )
    parser.add_argument(
        "directory", type=str, help="Directory containing files to be processed"
    )
    parser.add_argument(
        "--extensions",
        type=str,
        nargs="+",
        default=[".mp4", ".avi", ".mov", ".mkv", ".jpg", ".jpeg", ".png"],
        help="List of file extensions to process",
    )
    args = parser.parse_args()
    add_timestamp_to_filenames(args.directory, tuple(args.extensions))


if __name__ == "__main__":
    main()
