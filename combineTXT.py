import os

# 합치고 싶은 파일들이 있는 디렉토리를 지정하세요.
directory = "/Users/huh/Dropbox (Personal)/!  New/GPTs/2023.11.09 - 오은영박사님"

# 최종적으로 생성될 파일의 이름을 지정하세요.
output_filename = directory + "/오박사 강연 모음.txt"

# 해당 디렉토리에서 모든 txt 파일을 찾아서 하나로 합치기
with open(output_filename, "w") as outfile:
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r") as readfile:
                outfile.write(readfile.read() + "\n")  # 파일 내용을 쓰고 줄바꿈 추가

print(f"All text files have been combined into {output_filename}")
