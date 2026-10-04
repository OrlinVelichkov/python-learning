#🥊 Mission 1 — Traverse Keys
product = {
    "name": "Mouse",
    "price": 25,
    "stock": 42
}
for key in product.keys():
    print(key)
# 🥊 Mission 2 — Traverse Values
for value in product.values():
    print(value)
# 🥊 Mission 3 — Traverse Items
user = {
    "name": "Ivan",
    "age": 30,
    "city": "Sofia"
}
for key, value in user.items():
    print(f"{key} -> {value}")
    # 🥊 Mission 4 — Filter
scores = {
    "Ivan": 82,
    "Maria": 95,
    "Georgi": 68,
    "Elena": 88
}
for name, score in scores.items():
    if score >= 80:
        print(f"Name: {name}, Score: {score}")
# 🥊 Mission 5 — Counter
count = 0
for score in scores.values():
    if score >= 80:
        count += 1
print(count)
# 🥊 Mission 6 — Accumulator
prices = {
    "mouse": 25,
    "keyboard": 70,
    "monitor": 350,
    "headphones": 55
}
total = 0
for value in prices.values():
    total += value
print(total)
# 🥊 Mission 7 — Update Through Traversal
stock = {
    "mouse": 10,
    "keyboard": 5,
    "monitor": 3
}
for key in stock.keys():
    stock[key] += 2 
print(stock)
# 🥊 Mission 8 — Key + Value Logic
products = {
    "mouse": 25,
    "keyboard": 70,
    "monitor": 350,
    "cable": 10
}
for key, value in products.items():
    if value > 50:
        print(f"{key}: {value}") 
# 🔥 Mission 9 — Stage 6 Mini Checkpoint
inventory = {
    "mouse": 12,
    "keyboard": 7,
    "monitor": 5,
    "headphones": 20
}
count = 0
total = 0
for key in inventory.keys():
    print(key)
for value in inventory.values():
    if value >= 10:
        count += 1
    total += value
print(total)
print(f"Брой: {count}")
print(f"Общо: {total}")
for key, value in inventory.items():
    print(key, value)
for key in inventory.keys():
    inventory[key] += 1
print(inventory)
#