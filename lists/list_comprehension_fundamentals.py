#09.07.2026 - 22:30h
# Identity List Comprehension
# Stage 10 — Task 1
nums = [5, 10, 15, 20, 25]
new_num = [num for num in nums]
print(new_num)

#Класическо решение
new_num_classic = []
for num in nums:
    new_num_classic.append(num)
print(new_num_classic)

# Stage 10 — Lesson 2
# Filtering List Comprehension
# Task 2 — First Filtering Comprehension
nums = [15, 120, 40, 300, 80, 150, 20]
new = [numbers for numbers in nums if numbers >= 100]
print(new)
#Класически вариант
new = []
for number in nums:
    if number >= 100:
        new.append(number)
print(new)
# Stage 10 — Lesson 3
# Transformation List Comprehension
# Stage 10 — Task 3
# First Transformation Comprehension
nums = [3, 6, 9, 12, 15]
result = [num * 2 for num in nums]
print(result)

#Класически вариант
result = []
for num in nums:
    result.append(num * 2)
print(result)
# Stage 10 — Lesson 4
# Filtering + Transformation
nums = [10, 120, 30, 200]
result = [num * 2 for num in nums if num >= 100]
print(result)
#Класически вариант
result = []
for num in nums:
    if num >= 100:
        result.append(num * 2)
print(result)
# Stage 10 — Lesson 5
# Methods inside List Comprehension
# Stage 10 — Task 5
names = [
    "ivan",
    "maria",
    "petar",
    "georgi",
    "elena"
]
new_list = [name.upper() for name in names]
print(new_list)
#Класически вариант
new_list = []
for name in names:
    new_list.append(name.upper())
print(new_list)
# Stage 10 — Lesson 6
# Functions inside List Comprehension
# Stage 10 — Task 6
words = [
    "Python",
    "Developer",
    "AI",
    "Cursor",
    "GitHub"
]
new_list = [len(word) for word in words]
print(new_list)
#Класически вариант
new_list = []
for word in words:
    new_list.append(len(word))
print(new_list)