#23.07.2026 - 18:15h
# 🏆 Stage 10 — FINAL BOSS FIGHT
# Project: Customer Management Report System
customers = [
    "Ivan",
    "Maria",
    "Petar",
    "Georgi",
    "Elena",
    "Nikolay",
    "Dimitar"
]

cities = [
    "Sofia",
    "Plovdiv",
    "Varna",
    "Burgas",
    "Ruse",
    "Pleven",
    "Stara Zagora"
]

orders = [
    120,
    80,
    250,
    40,
    310,
    175,
    95
]

def classify(order):
    if order >= 250:
        return 'VIP+'
    elif order >= 100:
        return 'VIP'
    else:
        return 'Standard'

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

def customer_summary(name, city, order):
    category = classify(order)
    discount_value = discount(order)
    final = final_price(order)
    return {
        "name": name,
        "city": city,
        "category": category,
        "discount": discount_value,
        "final_price": final
    }

def build_report(position, customer):
    return (
        f'{position}. {customer["name"]} | {customer["city"]} | '
        f'{customer["category"]} | Discount: {customer["discount"]:.2f} | '
        f'Final: {customer["final_price"]:.2f}'
    )

#Класически вариант
results = []

for position, (name, city, order) in enumerate(zip(customers, cities, orders), start=1):
    customer = customer_summary(name, city, order) 
    results.append(build_report(position, customer))
print(results)
#Comprehension вариант
results = [build_report(position, customer_summary(name, city, order)) for position, (name, city, order) in enumerate(zip(customers, cities, orders),start=1)]
print(results)
total_customers = len(customers)
vip_plus_count = 0
vip_count = 0
standard_count = 0
for order in orders:
    category = classify(order)
    if category == 'VIP+':
        vip_plus_count += 1
    elif category == 'VIP':
        vip_count += 1
    else:
        standard_count +=1
total_revenue = 0
total_discount = 0
total_final_revenue = 0
for order in orders:
    total_revenue += order
    total_discount += discount(order)
    total_final_revenue += final_price(order)



print("Total customers:", total_customers)
print("VIP+:", vip_plus_count)
print("VIP:", vip_count)
print("Standard:", standard_count)
print("Total revenue:", total_revenue)
print("Total discount:", total_discount)
print("Final revenue:", total_final_revenue)