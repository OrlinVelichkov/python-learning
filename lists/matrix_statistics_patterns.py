#01.08.2026 - 20:00h
# Stage 11 — Lesson 8
# Matrix Statistics
# Mission 1
matrix = [
    [3, 5, 2],
    [8, 1, 4],
    [6, 7, 9]
]
even_count = 0
for row in matrix:
    for num in row:
        if num % 2 == 0:
            even_count +=1
print(f'Even numbers = {even_count}')
# 🎯 Mission 2
even_sum = 0
for row in matrix:
    for num in row:
        if num % 2 == 0:
            even_sum += num
print(f'Even numbers sum = {even_sum}')
# 🎯 Mission 3
even_sum = 0
even_count = 0
for row in matrix:
    for num in row:
        if num % 2 == 0:
            even_sum += num
            even_count += 1
print(f'Even numbers = {even_count}')
print(f'Even numbers sum = {even_sum}')
# 🚀 Stage 11 — Lesson 9
matrix = [
    [3, 5, 2],
    [8, 1, 4],
    [6, 7, 9]
]
for i, row in enumerate(matrix, start=1):
    even_numbers = 0
    for num in row:
        if num % 2 == 0:
            even_numbers += 1
    print(f'Row {i} even numbers = {even_numbers}')

for i, row in enumerate(matrix, start=1):
    even_sum = 0
    for num in row:
        if num % 2 == 0:
            even_sum += num
    print(f'Row {i} even sum = {even_sum}')

for i, row in enumerate(matrix, start=1):
    print(f'Row {i}')
    even_numbers = 0
    even_sum = 0
    for num in row:
        if num % 2 == 0:
            even_numbers += 1
            even_sum += num
    print(f'Even count = {even_numbers}')
    print(f'Even sum = {even_sum}')
# 🚀 Stage 11 — Lesson 10
# 🎯 Mission 1
matrix = [
    [3, 5, 2],
    [8, 1, 4],
    [6, 7, 9]
]
for i, row in enumerate(matrix,start=1):
    print(f'Row {i}')
    even_count = 0
    for num in row:
        if num % 2 == 0:
            even_count +=1
    print(f'Even count = {even_count}')
# 🎯 Mission 2
for i, row in enumerate(matrix, start=1):
    print(f'Row {i}')
    even_count = 0
    odd_count = 0
    for num in row:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f'Even count = {even_count}')
    print(f'Odd count = {odd_count}')
# 🎯 Mission 3
for i, row in enumerate(matrix, start=1):
    print(f'Row {i}')
    even_count = 0
    odd_count = 0
    even_sum = 0
    for num in row:
        if num % 2 == 0:
            even_count += 1
            even_sum += num
        else:
            odd_count += 1
    print(f'Even count = {even_count}')
    print(f'Odd count = {odd_count}')
    print(f'Even sum = {even_sum}')