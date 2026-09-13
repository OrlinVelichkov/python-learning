# 🥊 Mission 1 — Transformation
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)
# Mission 2 — Filtering
numbers = [5, 12, 7, 18, 3, 25]
new_list = [num for num in numbers if num >= 10]
print(new_list)
# Mission 3 — Filter + Transformation
numbers = [5, 12, 7, 18, 3, 25]
new_list_2 = [num * 2 for num in numbers if num >= 10]
print(new_list_2)
# Mission 4 — Conditional Expression
numbers = [1, 2, 3, 4, 5, 6]
labels = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(labels)
# Mission 5 — Conditional Numeric Transformation
numbers = [10, 15, 20, 25]
new_list_3 = [num * 2 if num >= 20 else num for num in numbers]
print(new_list_3)
# Mission 6 — Comprehension + zip()
products = ["Keyboard", "Mouse", "Monitor"]
prices = [70, 25, 350]
new_list_4 = [f'{item}: {price}' for item, price in zip(products, prices)]
new_list_4_1 = [f'№{i}. Product: {item}, Price: {price}' for i, (item, price) in enumerate(zip(products, prices), start=1)]
print(new_list_4)
print(new_list_4_1)
# 🥊 Mission 7 — Filter with zip()
products = ["Keyboard", "Mouse", "Monitor", "Laptop"]
prices = [70, 25, 350, 1200]
new_list_5 = [item.upper() for item, price in zip(products, prices) if price >= 300]
print(new_list_5)
# 🥊 Mission 8 — Triple zip()
products = ["Keyboard", "Mouse", "Monitor"]
prices = [70, 25, 350]
stock = [15, 42, 8]
new_list_6 = [[product, price, stock] for product, price, stock in zip(products, prices, stock)]
print(new_list_6)
any_check = any(any(item == "Mouse" for item in group) for group in new_list_6)
print(any_check)
# 🔥 Mission 9 — Stage 10 Mini Checkpoint
products = ["Keyboard", "Mouse", "Monitor", "Laptop"]
prices = [70, 25, 350, 1200]
stock = [15, 42, 8, 5]
prices_above_100 = [price for price in prices if price > 100]
prices_10percent_discount = [price * 0.9 for price in prices]
product_below_10 = [item for item, stock in zip(products, stock) if stock < 10]
nested_list = [[item, price] for item, price in zip(products, prices)]
print(prices_above_100)
print(prices_10percent_discount)
print(product_below_10)
print(nested_list)
nested_list[1:1] = [[nested_list[len(nested_list)-2][0].upper()]]
print(nested_list)
def report(item, price, stock):
    return f'{item} | {price} | {stock}'
report2 = [report(item, price, stock) for item, price, stock in zip(products, prices, stock)]
report = [f'{item} | {price} | {stock}' for item, price, stock in zip(products, prices, stock)]
print(report)
print(report2)