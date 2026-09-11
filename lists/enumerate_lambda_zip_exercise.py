products = [
    ["Keyboard", 70],
    ["Mouse", 25],
    ["Monitor", 350],
    ["TV", 350]
]
max_price_items = max(item[1] for item in products)
max_price = [item for item in products if item[1] == max_price_items]
print(max_price)
most_expensive = max(
    products,
    key=lambda product: product[1]
)
print(most_expensive)
def report(name, score):
    return f"{name.upper()}: {score}"

names = ["Ivan", "Maria"]
scores = [82, 94]
for name, score in zip(names, scores):
    print(report(name, score))

def square(number):
    return number ** 2

result = square(6)
print(result)
# 🥊 Mission 2 — Multiple Parameters
def calculate_total(price, quantity):
    return price * quantity
result = calculate_total(70, 4)
print(result)
# 🥊 Mission 3 — sum(), min(), max()
prices = [70, 25, 350, 1200, 90]
sum_prices = sum(prices)
max_prices = max(prices)
min_prices = min(prices)
print(sum_prices)
print(max_prices)
print(min_prices)
# 🥊 Mission 4 — max() with custom key
products = [
    ["Keyboard", 70],
    ["Mouse", 25],
    ["Monitor", 350],
    ["Laptop", 1200]
]
def most_expensive_price(item):
    return item[1]
most_expensive_item = max(products, key=lambda item: item[1])
# most_expensive_item = max(products, key=most_expensive_price)
print(most_expensive_item)
# 🥊 Mission 5 — zip()
products = ["Keyboard", "Mouse", "Monitor"]
prices = [70, 25, 350]
for item, price in zip(products, prices):
    print(f"{item} -> {price}")
    # 🥊 Mission 6 — enumerate()
players = ["Ivan", "Maria", "Georgi", "Elena"]
for i, player in enumerate(players, start=1):
    print(f"{i}. {player}")
    # 🥊 Mission 7 — enumerate(zip(...))
products = ["Keyboard", "Mouse", "Monitor"]
prices = [70, 25, 350]
for i, (item, price) in enumerate(zip(products, prices), start=1):
    print(f"{i}. {item} - {price}")
# 🥊 Mission 8 — Function + zip()
names = ["Ivan", "Maria", "Georgi"]
scores = [82, 94, 76]
def format_result(name, score):
    return f"{name}: {score} points"
for name, score in zip(names, scores):
    print(format_result(name, score))
# 🔥 Mission 9 — Stage 9B Mini Checkpoint
products = ["Keyboard", "Mouse", "Monitor", "Laptop"]
prices = [70, 25, 350, 1200]
stock = [15, 42, 8, 5]
total_price = sum(prices)
max_price_check = max(prices)
min_price_check = min(prices)
print(total_price)
print(max_price_check)
print(min_price_check)
def my_report(position, product, price, stock):
    return f"{position}. {product} | Price: {price} | Stock: {stock}"
for position,(product, price, quantity) in enumerate(zip(products, prices, stock), start=1):
    print(my_report(position, product, price, quantity))
def stock_value(price, quantity):
    return price * quantity
for item, price, quantity in zip(products, prices, stock):
    print(f"{item}: {stock_value(price, quantity)}")