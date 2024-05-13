def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name} # person은 딕셔너리
    if age:
        person['age'] = age
    return person

# musician은 person을 return했으니까 이것도 딕셔너리
musician = build_person('jimi', 'hendrix', age=27) 
print(musician)