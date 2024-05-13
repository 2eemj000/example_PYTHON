prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# 플래그 : 전체 프로그램의 실행여부를 결정하는 변수
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)