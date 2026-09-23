words = ["cat", "elephant", "dog", "hippopotamus"]

results = sorted(words, key=len, reverse=True)
print(results)

lister = [
    ["Mouse", 25],
    ["Keyboard", 70],
    ["Monitor", 350],
    ["Nano", 70]
]

results = sorted(lister, key=lambda item: item[1], reverse=True)
print(results)

# 🥊 Mission 1 — sort() vs sorted()
numbers = [8, 3, 12, 1, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
numbers.sort()
print(numbers)
# 🥊 Mission 2 — Descending Order
scores = [82, 95, 71, 88, 100]
new_score = sorted(scores, reverse=True)
print(new_score)

# 🥊 Mission 3 — key=len
words = [
    "Python",
    "AI",
    "Developer",
    "Code",
    "Automation"
]
words.sort(key=len)
print(words)
# 🥊 Mission 4 — Nested List Sorting
products = [
    ["Keyboard", 70],
    ["Mouse", 25],
    ["Monitor", 350],
    ["Laptop", 1200]
]
new_list_products = sorted(products, key=lambda product: product[1])
print(new_list_products)

# 🥊 Mission 5 — Descending Nested Sort
new_list_products_2 = sorted(products, key=lambda product: product[1], reverse=True)
print(new_list_products_2)
# 🥊 Mission 6 — Two Criteria
employees = [
    ["Ivan", 3000],
    ["Maria", 4000],
    ["Georgi", 3000],
    ["Elena", 4000],
    ["Boris", 3000]
]
new_employees = sorted(employees, key=lambda person: (person[1], person[0]))
print(new_employees)
# 🥊 Mission 7 — Mixed Directions
new_employees2 = sorted(employees, key=lambda person: (-person[1], person[0]))
print(new_employees2)
# 🥊 Mission 8 — Three Criteria
players = [
    ["Ivan", 10, 5],
    ["Maria", 10, 8],
    ["Georgi", 8, 12],
    ["Elena", 10, 8],
    ["Boris", 8, 7]
]
new_team = sorted(players, key=lambda player: (-player[1], -player[2], player[0]))
print(new_team)
# 🥊 Mission 9 — Sorting + Processing
products = [
    ["Keyboard", 70, 15],
    ["Mouse", 25, 42],
    ["Monitor", 350, 8],
    ["Laptop", 1200, 5]
]
def report_pro(name, price, stockit):
    return f'{name} | {price} | {stockit}'
new_products_2027 = sorted(products, key=lambda item: item[1], reverse=True)
for name, price, stock in new_products_2027:
    print(report_pro(name, price, stock))

# 🔥 Mission 10 — Stage 12 Final Checkpoint
products = [
    ["Keyboard", 70, 15],
    ["Mouse", 25, 42],
    ["Monitor", 350, 8],
    ["Laptop", 1200, 5],
    ["Webcam", 70, 10],
    ["Tablet", 350, 12]
]
def my_sortded(pro):
    return -pro[1], pro[0]
option_one = sorted(products, key=lambda pro: pro[1])
# option_two = sorted(products, key=lambda pro: (-pro[1], pro[0]))
option_two = sorted(products, key=my_sortded)
option_three = sorted(products, key=lambda pro: (-pro[2], pro[1], pro[0]))
print(option_one)
print(f'Резултат: {option_two}')
print(option_three)