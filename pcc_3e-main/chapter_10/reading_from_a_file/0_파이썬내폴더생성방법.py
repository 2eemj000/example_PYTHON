# mkdir 함수는 단일 디렉토리를 만들고, makedirs 함수는 중첩된 디렉토리 구조를 만들 수 있음

import os

# 새 디렉토리를 만들 경로
directory_path = "/path/to/new/directory"

try:
    # 디렉토리 생성
    os.mkdir(directory_path)
    print(f"디렉토리가 성공적으로 생성되었습니다: {directory_path}")
except FileExistsError:
    print(f"디렉토리가 이미 존재합니다: {directory_path}")
except Exception as e:
    print(f"디렉토리 생성 중 오류가 발생했습니다: {e}")



import os

# 새 디렉토리를 만들 경로 (중첩된 디렉토리 구조)
nested_directory_path = "/path/to/new/nested/directory"

try:
    # 중첩된 디렉토리 구조 생성
    os.makedirs(nested_directory_path)
    print(f"디렉토리가 성공적으로 생성되었습니다: {nested_directory_path}")
except FileExistsError:
    print(f"디렉토리가 이미 존재합니다: {nested_directory_path}")
except Exception as e:
    print(f"디렉토리 생성 중 오류가 발생했습니다: {e}")