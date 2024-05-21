from pathlib import Path
import json

username = input("이름을 입력하세요 ! ") 
path = Path('username.json') # 데이터 읽기
contents = json.dumps(username) # JSON 문자열로 변환
path.write_text(contents)

print(f"Welcome back, {username}!")