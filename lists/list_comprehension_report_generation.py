#20.07.2026 - 19:40h
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
# Stage 10 — Lesson 15
# Functions + Multiple Parameters
# Stage 10 — Task 16
def format_customer(name, order):
    return f'⭐ {name} | VIP Customer | Order: {order}' if order >=100 else f'{name} - Regular Customer | Order: {order}'
customers = ["Ivan", "Maria", "Petar", "Georgi", "Elena"]

orders = [120, 80, 250, 40, 310]
#Класически вариант
results = []
for customer_name, order in zip(customers, orders):
    results.append(format_customer(customer_name, order))
print(results)
#Comprehension вариант
results = [f"{customer_name} - VIP ({order})" if order >=100 else f"{customer_name} - Regular ({order})" for customer_name, order in zip(customers, orders)]
print(results)
#Comprehension вариант 2
results = [format_customer(customer_name, order) for customer_name, order in zip(customers, orders) ]
print(results)
# 📢 Stage 10 Boss Fight
# 🏆 Boss Fight A — Customer Report Generator
customers = ["Ivan", "Maria", "Petar", "Georgi", "Elena"]

orders = [120, 80, 250, 40, 310]

cities = ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse"]
def build_report(i, name, city, order):
    return f'Позиция: {i}. {name} | {city} | VIP | {order}' if order >= 100 else f'Позиция: {i}. {name} | {city} | Regular | {order}'
# #Класически вариант.
results = []
for i, (name, city, order) in enumerate(zip(customers, cities, orders),start=1):
    results.append(build_report(i, name, city, order))
print(results)
#Comprehension вариант
results = [build_report(i, name, city, order) for i, (name, city, order) in enumerate(zip(customers, cities, orders), start=1)]
print(results)