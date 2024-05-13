def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# 키워드인수로 전달할 때는 순서가 바껴도 key-value로 인식해서 똑바로 출력함
describe_pet(pet_name='harry', animal_type='hamster')
# 위치인수로 전달할 때는 순서대로 입력해야 함
describe_pet('harry','hamster')