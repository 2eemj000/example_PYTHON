# 중첩 : 리스트 안에 딕셔너리를 저장하거나 리스트를 딕셔너리의 값으로 저장

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for a in aliens:
  print(a)