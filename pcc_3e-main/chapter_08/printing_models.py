def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs: # list가 empty가 아니면 true
        current_design = unprinted_designs.pop() # 리스트 끝부분에서 하나씩 빼냄 
        print(f"Printing model: {current_design}")
        completed_models.append(current_design) # 출력한 디자인을 completed_models으로 옮김

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for a in completed_models:
        print(a)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs[], [completed_models]) # 8.4.1 의미
print_models(unprinted_designs[:], [completed_models]) # 8.4.2 의미
print(f"원래변수 출력 {unprinted_designs}") # empty가 됨
print(f"수정여부 출력 {completed_models}")
show_completed_models(completed_models)
