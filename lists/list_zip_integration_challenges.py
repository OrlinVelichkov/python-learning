#start learning at 21:51
# Integration Drill за zip()

# Task 9 — Store Report
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

sales = [12, 35, 18, 7]

for item, sale in zip(products, sales):
    print(f'{item}: {sale}')
print(f'Total sales: {sum(sales)}')
print(f'Best selling: {max(sales)}')
print(f'Worst selling: {min(sales)}')
print(f'Sorted sales: {sorted(sales)}')

# Task 10 — English Learning Report
days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
words = [25, 18, 30, 22]
for day, word in zip(days, words):
    print(f'{day}: {word}')
print(f'Total words: {sum(words)}')
print(f'Best day: {max(words)}')
print(f'Weakest day: {min(words)}')
print(f'Sorted: {sorted(words)}')

# Task 11 — Fitness Report
exercises = ["Bench", "Squat", "Deadlift", "Pull-up"]

reps = [10, 8, 5, 12]
for exercise, rep in zip(exercises, reps):
    print(f'{exercise}: {rep}')
print(f'Total reps: {sum(reps)}')
print(f'Max reps: {max(reps)}')
print(f'Min reps: {min(reps)}')
print(f'Sorted reps: {sorted(reps)}')

# Task 12 — enumerate() + zip()
clients = ["Ivan", "Maria", "Petar"]
payments = [120, 180, 90]
for i,(client, payment) in enumerate(zip(clients, payments),start=1):
    print(f'Client {i}: {client} -> {payment}')

# Task 13 — Real World
my_books = ['Nemo', 'Sherlock', 'King Arthur']
readed_pages = [120, 300, 500]
for i, (book, page) in enumerate(zip(my_books, readed_pages), start=1):
    print(f'Книга {i}: {book}, прочетени {page} страници')
print(f'Общо прочетени страници: {sum(readed_pages)}')
print(f'Книга с най-много прочетени страници: {book} {max(readed_pages)}') #как да покажа коя е книгата с най-много прочетени страници?

# Bonus Challenge
names = ["Ivan", "Maria"]
scores = [90, 80]
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(i, name, score)
#Output: 1 Ivan 90
#Output: 1 Maria 80