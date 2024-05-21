from pathlib import Path

#  경로 이동해서 파일 찾을 수 있도록 함
import os
print(os.getcwd) # 경로 확인
new_path = "pcc_3e-main/chapter_10/reading_from_a_file" # 새 경로 지정
os.chdir(new_path) # 경로 바꿈
path = Path('2_0_pi_million_digits.txt')

# 위에처럼 경로 안바꿔주려면 이런식으로
# path = Path('pcc_3e-main/chapter_10/reading_from_a_file/2_0_pi_million_digits.txt')

contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string: # 전체 string에 birthday string값이 포함되어있는지
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")