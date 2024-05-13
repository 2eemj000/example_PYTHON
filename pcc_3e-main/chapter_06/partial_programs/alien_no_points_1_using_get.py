alien_0 = {'color': 'green', 'speed': 'slow'}
# key값으로 값을 찾기
point_value = alien_0['points']
print(point_value)
# 같은 의미로 get활용할 때
print(alien_0.get('color'))

# points라는 ket가 없으면 , 뒤의 값이 저장 (error메시지 확인 용이)
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)