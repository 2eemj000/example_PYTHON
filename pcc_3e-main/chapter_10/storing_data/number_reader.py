from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents) # 파일을 다시 메모리로 읽음

print(numbers)