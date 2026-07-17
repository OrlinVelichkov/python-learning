#17.07. 2026 - 19:05h
# 🔹 Module 1 — Custom Functions inside List Comprehension
# 🔹 Module 2 — Nested List Comprehension
# 🔹 Module 3 — Stage 10 Boss Fight
# Stage 10 — Lesson 13
# Custom Functions inside List Comprehension
# Stage 10 — Task 14
def classify(sale):
    return 'VIP' if sale >= 100 else 'Regular'
orders = [40, 120, 80, 300, 90]
# Класически вариант
results = []
for sale in orders:
    results.append(classify(sale))
print(results)
#Comprehension вариант
results = [classify(sale) for sale in orders]
print(results)
#Comprehension вариант без функция - за упражняване на синтаксис
results = ['VIP' if sale >= 100 else 'Regular' for sale in orders]
print(results)
# Stage 10 — Lesson 14
def classify(order):
    return 'VIP' if order >= 100 else 'Regular'
customers = ["Ivan", "Maria", "Petar", "Georgi", "Elena"]
orders = [120, 80, 250, 40, 310]
# Класически вариант
results = []
for name, sale in zip(customers, orders):
    results.append(f'{name} - {classify(sale)}')
print(results)
#Comprehension вариант
results = [f'{name} - {classify(sale)}' for name, sale in zip(customers, orders)]
print(results)
#Comprehension вариант без функция
results = [f'{name} - VIP' if order >=100 else f'{name} - Regular' for name, order in zip(customers, orders)]
print(results)