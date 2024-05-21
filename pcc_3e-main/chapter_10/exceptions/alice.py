# TRY - EXCEPT - ELSE

from pathlib import Path


path = Path('alice.txt') # 파일 경로찾기
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else: 
    # 예외가 아니면 다시 여기로 돌아와서 실행
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")