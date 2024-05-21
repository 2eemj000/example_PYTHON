from pathlib import Path # Path 클래스 임포트
import os

# 현재 작업 디렉토리 확인
current_directory = os.getcwd()
print(f"현재 작업 디렉토리: {current_directory}")

# 변경할 디렉토리 경로
new_path = "pcc_3e-main/chapter_10/reading_from_a_file"

# 디렉토리 변경
os.chdir(new_path)

# 변경된 작업 디렉토리 확인
current_directory = os.getcwd()
print(f"변경된 작업 디렉토리: {current_directory}")


path = Path('pi_digits.txt') # Path 객체를 만들어 path 변수에 할당 (생성자) 
contents = path.read_text()
contents = contents.rstrip().lstrip()
print(contents)

lines = contents.splitlines() # 행단위로 접근
for line in lines:
    print(f"각 줄은 = {line}")

pi_string = ''
for line in lines:
    line = line.lstrip() # 공백을 없애려고
    pi_string += line  # 파일의 숫자를 공백없이 하나로 합침
    print(pi_string)