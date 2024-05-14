# 파이썬은 *을 보고 이 함수가 전달받는 인수를 *튜플(여기서는 toppings튜플)에 모음
# 인수의 갯수와 관계없이 비슷한 방식으로 동작

def make_pizza(size, *toppings): 
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for t in toppings: # toppings는 튜플, t는 각각의 element
        print(f"- {t}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# making_pizza 파일에서 import할 것 [방법 4가지 알기]