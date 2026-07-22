#22.07.2026 - 18:30h
# Stage 10 — Lesson 16B
# Function Composition + Numeric Data
# Stage 10 — Task 18
customers = ["Ivan", "Maria", "Petar", "Georgi", "Elena"]

cities = ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse"]

orders = [120, 80, 250, 40, 310]
def classify(order):
    if order >= 200:
        return 'VIP+'
    elif order >= 100:
        return 'VIP'
    else:
        return 'Regular'
def discount(order):
    category = classify(order)
    if category == 'VIP+':
        return order * 0.15
    elif category == 'VIP':
        return order * 0.10
    else:
        return 0
def final_price(order):
    discount_value = discount(order)
    return order - discount_value

def build_report(position, name, city, order):
    category = classify(order)
    discount_value = discount(order)
    final = final_price(order)
    return f'{position}. {name} | {city} | {category} | Discount: {discount_value} | Final: {final}'


#Класически вариант
results = []
for position, (name, city, order) in enumerate(zip(customers, cities, orders), start=1):
    results.append(build_report(position, name, city, order))
print(results)
#Comprehension вариант
results = [build_report(position, name, city, order) for position, (name, city, order) in enumerate(zip(customers, cities, orders), start=1)]
print(results)
