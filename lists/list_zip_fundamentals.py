# Active Coding — Session 1
#zip()
# Task 1
names = ["Ivan", "Maria", "Petar"]

ages = [25, 31, 28]

for name, age in zip(names, ages):
    print(f'{name} {age}')
# Task 2
products = ["Laptop", "Mouse", "Keyboard"]

prices = [1200, 50, 90]
for product, price in zip(products, prices):
    print(f'{product} {price}')
# Task 3
cities = ["Sofia", "Varna", "Plovdiv"]

population = [1300000, 330000, 340000]
for city, people in zip(cities, population):
    print(f'{city} {people}')
# Task 4
boxes = [25, 30, 50]
models = ['Bags', 'Belts', 'Gloves']
for box, model in zip(boxes, models):
    print(f'{model}: {box}')
for i in range(len(boxes)):#това е към Bonus Observation-а
    print(f'{models[i]}: {boxes[i]}')
# Repair Drill — Различна дължина на списъците
# Active Coding — Repair Session
# Task 5
names = ["Ivan", "Maria", "Petar"]

scores = [88, 72]

for name, score in zip(names, scores):
    print(f'{name}: {score}')
# Task 6
products = ["Laptop", "Mouse"]

prices = [1200, 50, 90]
for product, price in zip(products, prices):
    print(f'{product}: {price}')
# Task 7
cities = ["Sofia", "Varna", "Plovdiv", "Burgas"]

population = [1300000, 330000]
for city, people in zip(cities, population):
    print(f'{city}: {people}')

# Task 8
today_workout = [50, 30, 45, 60]
muscles = ['biceps', 'triceps', 'abs']
for reps, muscle in zip(today_workout, muscles):
    print(f'{muscle}: {reps}')

# Mini Thinking Task
a = [1, 2, 3, 4]

b = ["A"]

for x, y in zip(a, b):
    print(x, y)
#Output: 1 A

# Integration Drill
# Task 9 — Store Report
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

sales = [12, 35, 18, 7]

for product, sale in zip(products, sales):
    print(f'{product}: {sale}')
print(f'Total sales: {sum(sales)}')
print(f'Best selling: {max(sales)}')
print(f'Worst selling: {min(sales)}')
print(sorted(sales))

# Task 10 — English Learning Report
days = ["Monday", "Tuesday", "Wednesday", "Thursday"]

words = [25, 18, 30, 22]

for day, word in zip(days, words):
    print(f'{day}: {word}')
print(f'Total words: {sum(words)}')
print(f'Best day: {max(words)}')
print(f'Weakest day: {min(words)}')
print(sorted(words))
# Task 11 — Fitness Report
exercises = ["Bench", "Squat", "Deadlift", "Pull-up"]

reps = [10, 8, 5, 12]

for workout, rep in zip(exercises, reps):
    print(f'{workout}: {rep}')
print(f'Total reps: {sum(reps)}')
print(f'Max reps: {max(reps)}')
print(f'Min reps: {min(reps)}')
print(f'Sorted reps:{sorted(reps)}')

# Task 12 — enumerate() + zip()
clients = ["Ivan", "Maria", "Petar"]

payments = [120, 180, 90]

for i, (client, payment) in enumerate(zip(clients, payments), start=1):
    print(f'Client {i}: {client} -> {payment}')
# Client 1: Ivan -> 120
# Client 2: Maria -> 180
# Client 3: Petar -> 90