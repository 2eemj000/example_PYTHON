def build_profile(first, last, **user_info): # **을 사용하면 dictionary
    """Build a dictionary containing everything we know about a user."""
    # dictionary에 key값 두개를 추가함
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
# dictionary는 함수에서 변경되면 main에서도 변경됨 (mutable)

print(user_profile)