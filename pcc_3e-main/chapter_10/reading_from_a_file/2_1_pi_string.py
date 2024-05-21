from pathlib import Path

#  경로 이동해서 파일 찾을 수 있도록 함
import os
print(os.getcwd) # 경로 확인
new_path = "pcc_3e-main/chapter_10/reading_from_a_file" # 새 경로 지정
os.chdir(new_path) # 경로 바꿈

path = Path('2_0_pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
print (f"줄 수 = {len(lines)}")
pi_string = ''
for line in lines[:5]:
    print(f"각 줄 = {line}")
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))