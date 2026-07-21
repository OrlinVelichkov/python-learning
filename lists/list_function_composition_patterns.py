#21.07.2026 - 19:00h
# Stage 10 — Boss Fight B
# Customer Sales Report System
customers = ["Ivan", "Maria", "Petar", "Georgi", "Elena"]

cities = ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse"]

orders = [120, 80, 250, 40, 310]
def classify(order):
    return 'VIP+' if order >=200 else 'VIP' if order >= 100 else 'Regular'
def build_report(position, name, city, order):
    category = classify(order)
    return f'{position}. {name} | {city} | {category} | {order}'
#Класически вариант
results = []
for position, (name, city, order) in enumerate(zip(customers, cities, orders), start=1):
    results.append(build_report(position, name, city, order))
print(results)
#Comprehension вариант
results = [build_report(position, name, city, order) for position, (name, city, order) in enumerate(zip(customers, cities, orders),start=1)]
print(results)
# Stage 10 — Lesson 16A
# Function Composition
# Stage 10 — Task 17
customers = ["Ivan", "Maria", "Petar", "Georgi", "Elena"]

cities = ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse"]

orders = [120, 80, 250, 40, 310]
def classify(order):
    if order >=200:
        return 'VIP+'
    elif order >= 100:
        return 'VIP'
    else:
        return 'Regular'

def discount(order):
    category = classify(order)
    if category == 'VIP+': #това ли е правилния начин за решение чрез category == '...'?
        return '15%'#наистина аз разбрах че трябва да върна сумата след дадената отстъпка...
    elif category == 'VIP':
         return '10%'
    else:
        return '0%'

def build_report(position, name, city, order):
    category = classify(order)
    discount_percent = discount(order)
    return f'{position}. {name} | {city} | {category} | {discount_percent} | {order}'
#Класически вариант
results = []
for position, (name, city, order) in enumerate(zip(customers, cities, orders), start=1):
    results.append(build_report(position,name, city, order))
print(results)
#Comprehension вариант
results = [build_report(position, name, city, order) for position, (name, city, order) in enumerate(zip(customers, cities, orders), start=1)]
print(results)