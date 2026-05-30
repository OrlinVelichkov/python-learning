# Bridge Drill — range(len()) → enumerate()
words = ["red", "green", "blue"]
for i, num in enumerate(words):
    print(f'Index {i} contains {words[i]}')
# TRUE Active Coding Drill
#Вариант А
names = ["Ivan", "Maria", "Peter"]
scores = [5, 6, 4]
for i in range(len(scores)):
    print(f'{names[i]} -> {scores[i]}')
# TRUE Active Coding Drill — Parallel Traversal with 3 Lists
names = ["Ivan", "Maria", "Peter"]
scores = [5, 6, 4]
cities = ["Sofia", "Varna", "Plovdiv"]
for i in range(len(names)):
    print(f'{names[i]} -> {scores[i]} -> {cities[i]}')