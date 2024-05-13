favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

# set()으로 감싸면 중복을 제거함
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())