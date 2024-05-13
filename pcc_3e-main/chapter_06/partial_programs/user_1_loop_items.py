user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

# key & 값 쌍 순회하기
# items() -> key & 값 쌍 반환하는 메서드
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")