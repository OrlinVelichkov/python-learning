#15.08.2026 - 22:15h
# 🚀 Stage 12 — Lesson 5
# Sorting върху Nested Lists / Custom Sorting
# 🥊 Coding Mission 1 — Product Price Ranking
products = [
    ["Keyboard", 70, 15],
    ["Mouse", 25, 42],
    ["Monitor", 350, 8],
    ["Laptop", 1200, 5],
    ["Headphones", 110, 27]
]
def item_sorting(item):
    return item[1]

new_product_list = sorted(products, key=item_sorting, reverse=True) #Направих вариант с класическа функция
print(f'Original {products}')
print(f'By price {new_product_list}')

new_product_list_lamda = sorted(products, key=lambda item: item[1], reverse=True) #Вариант с lambda
print(f'Original {products}')
print(f'By price {new_product_list_lamda}')
# 🥊 Coding Mission 2 — Stock Priority
products = [
    ["Keyboard", 70, 15],
    ["Mouse", 25, 42],
    ["Monitor", 350, 8],
    ["Laptop", 1200, 5],
    ["Headphones", 110, 27]
]
def item_sorting_by_quantity(item):
    return item[2]
new_product_list_by_quantity = sorted(products, key=item_sorting_by_quantity)
print(f'Original {products}')
print(f'By quantity {new_product_list_by_quantity}')
new_product_list_by_quantity_lambda = sorted(products, key=lambda item: item[2])
print(f'Original {products}')
print(f'By quantity {new_product_list_by_quantity_lambda}')
# 🥊 Coding Mission 3 — Alphabetical Catalog
def sorting_by_alphabetical(item):
    return item[0]
new_alphabetical_list = sorted(products, key=sorting_by_alphabetical)
new_alphabetical_list_lambda = sorted(products, key=lambda item: item[0])
print(new_alphabetical_list)
print(new_alphabetical_list_lambda)
# 🥊 Coding Mission 4 — Реална mutation
products.sort(key=lambda item: item[2], reverse=True)
print(products)
# 🔥 Mission 5 — Multi-field Dataset
employees = [
    ["Ivan", "Developer", 3200, 4],
    ["Maria", "Designer", 2800, 6],
    ["Georgi", "Developer", 4100, 8],
    ["Elena", "Manager", 4500, 7],
    ["Petar", "Support", 2200, 3]
]
employees_by_salary = sorted(employees, key=lambda employee: employee[2], reverse=True)
employees_by_experience = sorted(employees, key=lambda employee: employee[3])
employees_by_name = sorted(employees, key=lambda employee: employee[0])
print(employees_by_salary)
print(employees_by_experience)
print(employees_by_name)
print(employees)
# 🥊 Lesson 5 — Multi-key Mini Drill
products = [
    ["Keyboard", 70, 15],
    ["Mouse", 25, 42],
    ["Monitor", 350, 8],
    ["Laptop", 1200, 5],
    ["Headphones", 70, 27],
    ["Webcam", 70, 9]
]

def two_factor_sorting(item):
    return item[1], item[2]
new_product_list_two_factor = sorted(products, key=two_factor_sorting)
new_product_list_two_factor_lambda = sorted(products, key=lambda item: (item[1], item[2]))
print(new_product_list_two_factor)
print(new_product_list_two_factor_lambda)
# 🥊 Lesson 5 — Mixed Direction Sorting Drill
employees = [
    ["Ivan", "Developer", 3200, 4],
    ["Maria", "Designer", 3200, 6],
    ["Georgi", "Developer", 4100, 8],
    ["Elena", "Manager", 3200, 7],
    ["Petar", "Support", 2200, 3]
]

employees_sorted = sorted(employees, key=lambda employee: (-employee[2], employee[0]))
print(employees_sorted)