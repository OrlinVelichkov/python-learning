#24.07.2026 - 19:45h
# 🚀 Stage 11 — Lesson 1
# Nested Lists (2D Lists)
# Task 1
matrix = [
    [5, 8, 1],
    [7, 3, 9],
    [4, 6, 2]
] 
print(matrix[0][0])
print(matrix[1][2])
print(matrix[2][1])
print(matrix[1])
print(matrix[0])
# 🚀 Stage 11 – Lesson 2
# Matrix Traversal
matrix = [
    [5, 8, 1],
    [7, 3, 9],
    [4, 6, 2]
]
for i, row in enumerate(matrix, start=1):
    print(f'Row {i}: {row}')
# 🚀 Stage 11 – Lesson 3
# Nested Traversal
matrix = [
    [5, 8, 1],
    [7, 3, 9],
    [4, 6, 2]
]
for row in matrix:
    for number in row:
        print(number)
# 🚀 Stage 11 – Lesson 4
matrix = [
    [5, 8, 1],
    [7, 3, 9],
    [4, 6, 2]
]
total_sum = 0
for row in matrix:
    for number in row:
        total_sum += number
print(f'Обща сума на всички числа: {total_sum}')
# 🚀 Stage 11 — Lesson 5
# Row Processing
# 🎯 Task 1
matrix = [
    [5, 8, 1],
    [7, 3, 9],
    [4, 6, 2]
]
for position, row in enumerate(matrix, start=1):
    total_sum = 0
    for number in row:
        total_sum += number
    print(f'Row {position} sum = {total_sum}')
