import csv
import instaloader
import os
import sys
from urllib.parse import urlparse


def get_shortcode_from_url(url):
    path = urlparse(url).path
    return path.split("/")[-2]


def download_instagram_content(csv_file):
    # Instaloader 인스턴스 생성
    L = instaloader.Instaloader()

    # CSV 파일 경로에서 디렉토리 경로 추출
    csv_dir = os.path.dirname(csv_file)
    csv_filename = os.path.splitext(os.path.basename(csv_file))[0]

    # 출력 디렉토리 생성 (CSV 파일 이름을 따서 새 폴더 생성)
    output_dir = f"{csv_filename}_downloads"
    os.makedirs(output_dir, exist_ok=True)

    # CSV 파일 읽기
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # 헤더 행 건너뛰기 (필요한 경우)

        for row in csv_reader:
            url = row[0]  # URL이 첫 번째 열에 있다고 가정
            shortcode = get_shortcode_from_url(url)

            try:
                # 게시물 다운로드
                post = instaloader.Post.from_shortcode(L.context, shortcode)
                L.download_post(post, target=output_dir)
                print(f"다운로드 완료: {url}")
            except Exception as e:
                print(f"다운로드 실패: {url}")
                print(f"오류: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python script.py <csv_file_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    if not os.path.exists(csv_file_path):
        print(f"오류: 파일을 찾을 수 없습니다: {csv_file_path}")
        sys.exit(1)

    download_instagram_content(csv_file_path)

    # /Users/huh/Dropbox (Personal)/Mac/Downloads/틈 인스타그램 다운로드 - 시트1.csv
