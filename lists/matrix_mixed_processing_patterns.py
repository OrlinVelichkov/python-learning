#31.07.2026 - 18:50h
# Matrix Bootcamp — Module 3: Mixed Operations
matrix = [
    [3, 5, 2],
    [8, 1, 4],
    [6, 7, 9]
]
# 🎯 Mission 1
last_row_sum = 0
first_column_sum = 0
for num in matrix[-1]:
    last_row_sum += num
for row in matrix:
    first_column_sum += row[0]
print(f'Last row sum = {last_row_sum}')
print(f'First column sum = {first_column_sum}')
# 🎯 Mission 2
for num in matrix[0]:
    if num % 2 != 0:
        print(num)
for row in matrix:
    if row[2] % 2 == 0:
        print(row[2])
# 🎯 Mission 3
even_numbers_sum = 0
for row in matrix:
    if row[1] % 2 == 0:
        even_numbers_sum += row[1]
print(f'Even numbers sum = {even_numbers_sum}')
#лично упражнение от мен си
for column in range(len(matrix[0])):
    print(f'Колона {column +1}')
    for row in matrix:
        print(row[column])
# Stage 11 — Lesson
# Тема: Processing Rows and Columns Together
# 🔥 Lesson 7 — Mission 1
matrix = [
    [3, 5, 2],
    [8, 1, 4],
    [6, 7, 9]
]
for i, row in enumerate(matrix,start=1):    
    row_sum = 0
    for num in row:
        row_sum +=num
    print(f'Row {i} sum = {row_sum}')
# 🔥 Lesson 7 — Mission 2
for position, row in enumerate(matrix,start=1):
    print(f'Row {position}:')
    for num in row:
        if num % 2 == 0:
            print(num)
# извеждане само на четните числа от матрицата
even_matrix = [num for row in matrix for num in row if num % 2 == 0]
print(even_matrix)