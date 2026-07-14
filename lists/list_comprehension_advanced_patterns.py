#14.07.2026 - 19:00h
names = [
    "ivan",
    "maria",
    "ai",
    "petar",
    "go"
]
#Класически вариант
results = []
for name in names:
    if len(name) >= 4:
        results.append(name.upper())
print(results)
#Comprehension вариант
results = [name.upper() for name in names if len(name) >= 4]
print(results)
# Stage 10 — Lesson 8
# if...else inside List Comprehension
# Stage 10 — Task 8
#Класически вариант
nums = [20, 120, 40, 250, 90]
results = []
for num in nums:
    if num >= 100:
        results.append(num * 2)
    else:
        results.append(num)
print(results)
#Comprehension вариант
results = [num * 2 if num >= 100 else num for num in nums]
print(results)
# Lesson 9 — Multiple Conditions
# Task 9 — Multiple Conditions
nums = [35, 80, 120, 155, 200, 215, 300, 410]
#Класически вариант
results = []
for num in nums:
    if num >= 100 and num % 2 == 0:
        results.append(num)
print(results)
#Comprehension вариант
results = [num for num in nums if num >= 100 and num % 2 == 0]
print(results)
# 🚀 Lesson 10 — zip() + List Comprehension
# Stage 10 — Lesson 10
# Stage 10 — Task 10
customers = [
    "Ivan",
    "Maria",
    "Petar",
    "Georgi",
    "Elena"
]

orders = [
    120,
    80,
    250,
    40,
    310
]
# Класически вариант
results = []
for name, order in zip(customers, orders):
    if order >= 100:
        results.append(name)
print(results)
#Comprehension вариант
results = [name for name, order in zip(customers, orders) if order >= 100]
print(results)