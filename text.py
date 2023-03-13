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

f = lambda s: s**2

dat = [1, 2, 3, 4, 5, 6]

print(sum(dat))

filtered_power_dat = [g for s in dat if((g := f(s)) > 8)]
print(filtered_power_dat)


dicto = {"A" : [40, 62, 65], "B": [35, 62, 70, 82], "C": [28, 45, 80], "D": [91, 77]}

q = {g: mean for g in dicto if((mean := (sum(dicto[g]) // len(dicto[g])))) > 60}

print(q)