# 🥊 Mission 1 — Filtering
numbers = [4, 17, 8, 23, 11, 5, 30]
big_numbers = []
for num in numbers:
    if num >= 10:
        big_numbers.append(num)
print(big_numbers)
# 🥊 Mission 2 — Transformation
prices = [20, 50, 100, 200]
discounted_prices = []
for price in prices:
    discounted_prices.append(price * 0.9)
print(discounted_prices)
# 🥊 Mission 3 — Filter + Transform
numbers = [3, 10, 7, 20, 15, 2]
new_list = []
for num in numbers:
    if num >= 10:
        new_list.append(num * 3)
print(new_list)
# 🥊 Mission 4 — Counter
ages = [15, 22, 17, 31, 18, 16, 45]
counter = 0
for age in ages:
    if age >= 18:
        counter += 1
print(counter)
# 🥊 Mission 5 — Accumulator
sales = [120, 80, 250, 50, 300]
total_sum = 0
for sale in sales:
    total_sum += sale
print(total_sum)
# 🥊 Mission 6 — Counter + Accumulator
orders = [25, 120, 80, 200, 45, 150]
count = 0
sum_of = 0
for order in orders:
    if order >= 100:
        count += 1
        sum_of += order
print(count)
print(sum_of)
# 🥊 Mission 7 — Even/Odd Processing
numbers = [4, 7, 10, 15, 18, 21, 24]
even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
        even_sum += num
    else:
        odd_count += 1
        odd_sum += num
print(even_count)
print(even_sum)
print(odd_count)
print(odd_sum)
# 🔥 Mission 8 — Stage 6.5 Mini Checkpoint
products = [
    ["Keyboard", 70],
    ["Mouse", 25],
    ["Monitor", 350],
    ["Laptop", 1200],
    ["Webcam", 90]
]
new_list_price = []
new_list_discount = []
counter = 0
total = 0
for item in products:
    total += item[1]
    new_list_discount.append([item[0], item[1] * 0.9])
    if item[1] >= 100:
        new_list_price.append(f'{item[0]}: {item[1]}')
    elif item[1] < 100:
        counter += 1
print(new_list_price)
print(total)
print(new_list_discount)
