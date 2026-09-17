# 🥊 Mission 1 — Nested Indexing
matrix = [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
]
print(matrix[1][1])
print(matrix[2][2])
print(matrix[0][1])

# 🥊 Mission 2 — Row Traversal
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
for i, row in enumerate(matrix, start=1):
    print(f'Ред {i}: {row}')

# 🥊 Mission 3 — All Elements
for row in matrix:
    for element in row:
        print(element)

# 🥊 Mission 4 — Row Sums
matrix = [
    [2, 4, 6],
    [10, 20, 30],
    [5, 5, 5]
]
for row in matrix: #option 1
    print(sum(row))

for row in matrix:#option 2
    row_sum = 0
    for element in row:
        row_sum += element
    print(row_sum)
# 🥊 Mission 5 — Largest Row Sum
matrix = [
    [4, 8, 12],
    [10, 20, 30],
    [7, 9, 11]
]
max_sum_row = None
position = None
for i, row in enumerate(matrix):
    current_max_row = 0
    for element in row:
        current_max_row += element
    if max_sum_row is None or current_max_row > max_sum_row:
        max_sum_row = current_max_row
        position = i
print(f'{position}: {max_sum_row}')

# 🥊 Mission 6 — Specific Column
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

column = 1
column_sum = 0
for row in matrix:
    column_sum += row[column]
print(f'Резултат: {column_sum}')

# 🥊 Mission 7 — All Column Sums
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for column_index in range(len(matrix[0])):
    col_sum = 0
    for row in matrix:
        col_sum += row[column_index]
    print(f'Сума на колона {column_index}: {col_sum}')

# 🔥 Mission 8 — Stage 11 Mini Checkpoint
sales = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 130],
    [300, 250, 280]
]
#A
for row in sales:
    print(sum(row))
#A.1
for row in sales:
    row_sum2 = 0
    for element in row:
        row_sum2 += element
    print(row_sum2)
#B
max_sum_of_row = None #global result
for row in sales:
    current_result = 0 #local_result
    for element in row:
        current_result += element
    if max_sum_of_row is None or current_result > max_sum_of_row:
        max_sum_of_row = current_result
print(f'Резултат: {max_sum_of_row}')

#C
min_sum_row = None #global
for row in sales:
    min_sum = 0 #local
    for element in row:
        min_sum += element
    if min_sum_row is None or min_sum < min_sum_row:
        min_sum_row = min_sum
print(f'Резултат: {min_sum_row}')

#D
total_sum = 0
for row in sales:
    for element in row:
        total_sum += element
print(f'Резултат: {total_sum}')

#D.1
total = 0
for row in sales:
    total += sum(row)
print(total)

#D.2
total_sum_2 = sum(sum(row) for row in sales)
print(total_sum_2)

#E
for col in range(len(sales[0])):
    column = 0
    for row in sales:
        column += row[col]
    print(f'Резултат: {column}')
