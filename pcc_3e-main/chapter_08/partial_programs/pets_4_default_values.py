def describe_pet(pet_name, animal_type='dog'): # default value
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie') # animal_type에 값을 안주면 default value 가져옴

describe_pet(pet_name='willie', animal_type='cat') # animal_type에 값을 주면 바뀜 