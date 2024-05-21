import os

# 현재 작업 디렉토리 확인
current_directory = os.getcwd()
print(f"현재 작업 디렉토리: {current_directory}")

# 변경할 디렉토리 경로
new_directory = "/path/to/new/directory"

# 디렉토리 변경
os.chdir(new_directory)

# 변경된 작업 디렉토리 확인
current_directory = os.getcwd()
print(f"변경된 작업 디렉토리: {current_directory}")