#15.07.2026 - 22:30h
# Stage 10 — Task 11: Formatted Customer Report
customers = ["Ivan", "Maria", "Petar", "Georgi", "Elena"]

orders = [120, 80, 250, 40, 310]

cities = ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse"]
#Класически вариант
results = []
for name, order, city in zip(customers, orders, cities):
    if order >= 100:
        results.append(f'{name} | {city} | {order}')
print(results)
#Comprehension вариант
results = [f'{name} | {city} | {order}' for name, order, city in zip(customers, orders, cities) if order >= 100]
print(results)
#16.07.2026 - 19:00h
# Stage 10 — Lesson 11
# enumerate() + List Comprehension
# Stage 10 — Task 12
names = [
    "Ivan",
    "Maria",
    "Petar",
    "Georgi",
    "Elena"
]
#Класически вариант (добавих start за позиция от 1)
results = []
for i, name in enumerate(names, start=1):
    results.append(f'{i}. {name}')
print(results)
#Comprehension вариант
results = [f'{i}. {name}' for i, name in enumerate(names, start=1)]
print(results)
# Stage 10 — Lesson 12
# Stage 10 — Task 13
customers = ["Ivan", "Maria", "Petar", "Georgi", "Elena"]
orders = [120, 80, 250, 40, 310]
#Класически вариант 
results = []
for i, (name, order) in enumerate(zip(customers, orders), start=1):
    if order >= 100:
        results.append(f'{i}. {name} - {order}')
print(results)
#Comprehension вариант
results = [f'{i}. {name} - {order}' for i, (name, order) in enumerate(zip(customers, orders), start=1) if order >= 100]
print(results)
# Repair Drill 10A — if...else Expression
nums = [30, 120, 80, 250, 60]
#Класически вариант 
results = []
for num in nums:
    if num >= 100:
        results.append('VIP')
    else:
        results.append('Regular')
print(results)
#Comprehension вариант
results = ['VIP' if num >= 100 else 'Regular' for num in nums]
print(results)
# Repair Drill 10B — Numbers + Text
nums = [25, 120, 45, 310, 90]
#Класически вариант 
results = []
for num in nums:
    if num >= 100:
        results.append(f'VIP ({num})')
    else:
        results.append(f'Regular ({num})')
print(results)
#Comprehension вариант
results = [f'VIP ({num})' if num >=100 else f'Regular ({num})' for num in nums]
print(results)
# Repair Drill 10C — Integration
customers = ["Ivan", "Maria", "Petar", "Georgi", "Elena"]

orders = [120, 80, 250, 40, 310]
#Класически вариант 
results = []
for name, order in zip(customers, orders):
    if order >= 100:
        results.append(f'{name} - VIP')
    else:
        results.append(f'{name} - Regular')
print(results)
#Comprehension вариант
results = [f'{name} - VIP' if order >= 100 else f'{name} - Regular' for name, order in zip(customers, orders)]
print(results)
#Това е решението ми за # Repair Drill 10C — Integration
