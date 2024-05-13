favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

# items()
for a,b in favorite_languages.items():
    print(a)
    print(b)

# keys()
for n in favorite_languages.keys():
    print(n.title())

# values()
for v in favorite_languages.values():
    print(v.title())