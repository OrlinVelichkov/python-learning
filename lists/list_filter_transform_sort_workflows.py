#19.08.2026 - 19:40h
# 🚀 Stage 13 — Real World Combinations
# 🥊 Coding Mission 1 — Sales Pipeline
products = [
    ["Keyboard", "Electronics", 70, 15],
    ["Mouse", "Electronics", 25, 42],
    ["Monitor", "Electronics", 350, 8],
    ["Desk", "Furniture", 420, 6],
    ["Chair", "Furniture", 180, 19],
    ["Laptop", "Electronics", 1200, 5],
    ["Lamp", "Furniture", 65, 31]
]
new_products_list = [product for product in products if product[2] >= 100 and product[3] >= 8]
new_products_list.sort(key=lambda product: product[2], reverse=True)
print(new_products_list)
new_products_list_items = sorted((product for product in products if product[2] >= 100 and product[3] >= 8), reverse=True)
print(new_products_list_items)
# 🥊 Coding Mission 2 — Discounted Product Report
products = [
    ["Keyboard", "Electronics", 70, 15],
    ["Mouse", "Electronics", 25, 42],
    ["Monitor", "Electronics", 350, 8],
    ["Desk", "Furniture", 420, 6],
    ["Chair", "Furniture", 180, 19],
    ["Laptop", "Electronics", 1200, 5],
    ["Lamp", "Furniture", 65, 31]
]
electronics_list = [product for product in products if product[1] == 'Electronics' and product[2] >= 70]
print(electronics_list)
discount_list = [[product[0], product[2] * 0.9] for product in electronics_list]
discount_list.sort(key=lambda product: product[1], reverse=True)
print(discount_list)
# 🥊 Coding Mission 3 — Inventory Report
products = [
    ["Keyboard", "Electronics", 70, 15],
    ["Mouse", "Electronics", 25, 42],
    ["Monitor", "Electronics", 350, 8],
    ["Desk", "Furniture", 420, 6],
    ["Chair", "Furniture", 180, 19],
    ["Laptop", "Electronics", 1200, 5],
    ["Lamp", "Furniture", 65, 31]
]
low_stock_availability = [[product[0], product[3], product[2] * product[3]] for product in products if product[3] <= 15]
low_stock_availability.sort(key=lambda product: product[2], reverse=True)
for name, stock, stock_value in low_stock_availability:
    print(f'{name} | Stock: {stock} | Stock Value: {stock_value}')