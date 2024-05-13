# 딕셔너리 내부에 딕셔너리 존재 (중첩)

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'job':'scientist',
        'salary': 10000,
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'job':'developer',
        'salary': 20000,
        },

    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    # 딕셔너리 내부의 딕셔너리 가져올때 : []
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# 확장형 for문 중첩
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    for k,v in user_info.items():
        print(f"key={k}, value={v}")