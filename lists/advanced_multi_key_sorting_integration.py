#18.08.2026 - 19:15h
# 🔥 Stage 12 — Final Integration / Boss Fight
products = [
    ["Laptop Pro", "Electronics", 1499, 8, 4.8],
    ["Office Chair", "Furniture", 249, 24, 4.5],
    ["Gaming Mouse", "Electronics", 79, 45, 4.7],
    ["Standing Desk", "Furniture", 599, 12, 4.6],
    ["Mechanical Keyboard", "Electronics", 129, 31, 4.8],
    ["Desk Lamp", "Furniture", 79, 18, 4.3],
    ["USB Hub", "Electronics", 49, 52, 4.5],
    ["Monitor 27", "Electronics", 399, 12, 4.7],
    ["Ergonomic Chair", "Furniture", 399, 9, 4.8],
    ["Webcam HD", "Electronics", 79, 27, 4.4]
]
# 🥊 Mission 1 — Price Report
def marketing_report(item):
    return item[2]
report_for_marketing = sorted(products, key=lambda item: item[2], reverse=True)
report_for_marketing_def = sorted(products, key=marketing_report, reverse=True)
print(report_for_marketing)
print(report_for_marketing_def)
# 🥊 Mission 2 — Restock Priority

def restock_sorting(item):
    return item[3]
restock = sorted(products, key=lambda item: item[3])
restock_def = sorted(products, key=restock_sorting)
print(restock)
print(restock_def)
# 🥊 Mission 3 — Customer Rating
def customer_rating(item):
    return -item[4], item[2]
customer_rating_list = sorted(products, key=customer_rating)
customer_rating_list_lambda = sorted(products, key=lambda item: (-item[4], item[2]))
print(f'Customer rating: {customer_rating_list}')
print(f'Customer rating 2: {customer_rating_list_lambda}')
# 🥊 Mission 4 — Category Catalog
def product_by_category_and_name(item):
    return item[1], item[0]
new_products_list = sorted(products, key=lambda item: (item[1], item[0]))
new_products_list_def = sorted(products, key=product_by_category_and_name)
print(new_products_list)
print(new_products_list_def)
# 🥊 Mission 5 — Price Tie Breaker

def by_price_and_quantity(item):
    return item[2], -item[3]
products_by_price = sorted(products, key=by_price_and_quantity)
products_by_price_lambda = sorted(products, key=lambda item: (item[2], -item[3]))
print(products_by_price)
print(products_by_price_lambda)
# 🥊 Mission 6 — Real Mutation
products.sort(key=lambda item: item[0])
print(products)
# 🔥 Mission 7 — Management Ranking
employees = [
    ["Ivan", "Development", 4200, 6],
    ["Maria", "Marketing", 3400, 8],
    ["Georgi", "Development", 4200, 9],
    ["Elena", "Management", 5100, 7],
    ["Petar", "Support", 2800, 5],
    ["Daniel", "Development", 4200, 6],
    ["Nikol", "Marketing", 3400, 4]
]
new_ranking = sorted(employees, key=lambda employee: (-employee[2], -employee[3], employee[0]))
print(new_ranking)
# 👑 Mission 8 — Decision Mission
new_employees_list = sorted(employees, key=lambda employee: (employee[1], -employee[3], -employee[2]))
print(new_employees_list)