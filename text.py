words = ['falcon', 'sky', 'ab', 'water', 'a', 'forest']

for word in words:
    if ((n := len(word)) < 3):
        print(f"Warning the word {word} has {n} characters")


users = [
    {'name': 'John Doe', 'occupation': 'Trade'},
    {'name': 'Fatai', 'occupation': 'Gradner'},
    {'name': 'Adeleke Fakoya', 'occupation': 'Lecturer'},
    {'name': 'Adebayo Salami', 'occupation': 'Actor'},
]

for user in users:
    if ((name := user.get('name')) is not None):
        print(f"{name}")