# 🥊 Mission 1 — Basic Slice
numbers = [10, 20, 30, 40, 50, 60]
new_number = numbers[1:4]
print(new_number)
# 🥊 Mission 2 — Start / Stop Omission
cities = [
    "Sofia",
    "Plovdiv",
    "Varna",
    "Burgas",
    "Ruse",
    "Pleven"
]
first_three = cities[:3]
from_third = cities[-4:]
print(first_three)
print(from_third)
# 🥊 Mission 3 — Step
numbers = [0, 10, 20, 30, 40, 50, 60, 70]
new_list = numbers[::2]
print(new_list)
# 🥊 Mission 4 — Last Elements
products = [
    "Keyboard",
    "Mouse",
    "Monitor",
    "Laptop",
    "Webcam",
    "Headphones"
]
last_three = products[-3:]
print(last_three)
# 🥊 Mission 5 — Remove From View, Not Mutation
without_last_two = products[:]
without_last_two[-2:] = []
# del without_last_two[-2:]
print(without_last_two)
# 🥊 Mission 6 — Reverse Copy
scores = [10, 20, 30, 40, 50]
reversed_scores = scores[::-1]
print(scores)
print(reversed_scores)
# 🥊 Mission 7 — Controlled Reverse Slice
numbers = [10, 20, 30, 40, 50, 60, 70]
# numbers = numbers[5:2:-1]
numbers = numbers[-2:2:-1]
print(numbers)
# 🔥 Mission 8 — Stage 8 Mini Checkpoint
data = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H"
]
first_four = data[:4]
last_three = data[-3:]
every_second = data[::2]
entire_list = data[::-1]
fed = data[5:2:-1]
fed2 = data[-3:-6:-1]
print(first_four)
print(first_three)
print(every_second)
print(entire_list)
print(fed)