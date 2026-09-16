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
for row in matrix:
    print(row)
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
for row in matrix:
    print(sum(row))
for row in matrix:
    sum_row = 0
    for num in row:
        sum_row += num
    print(sum_row)
# 🥊 Mission 5 — Largest Row Sum
matrix = [
    [4, 8, 12],
    [10, 20, 30],
    [7, 9, 11]
]
max_sum = None
position_row = None
for position, row in enumerate(matrix):
    max_sum_row = 0
    for num in row:
        max_sum_row += num
    if max_sum is None or max_sum_row > max_sum:
        max_sum = max_sum_row
        position_row = position
print(f"Позиция {position_row}, {max_sum}")

min_sum = None
position_row2 = None
for index, row in enumerate(matrix):
    row_sum = 0
    for num in row:
        row_sum += num
    if min_sum is None or row_sum < min_sum:
        min_sum = row_sum
        position_row2 = index
print(f"Позиция {position_row2}, {min_sum}")
# 🥊 Mission 6 — Specific Column
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
column_index = 1
column_sum = 0
for row in matrix:
    column_sum += row[column_index]
print(f"Сума: {column_sum}")
# print(sum(row[column_index] for row in matrix))

# 🥊 Mission 7 — All Column Sums
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for col in range(len(matrix[0])):
    col_sum = 0
    for row in matrix:
        col_sum += row[col]
    print(col_sum)
# 🔥 Mission 8 — Stage 11 Mini Checkpoint
sales = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 130],
    [300, 250, 280]
]
for row in sales:
    row_sum_total = 0
    for num in row:
        row_sum_total += num
    print(row_sum_total)

max_sum2 = None
for row in sales:
    row_sum2 = 0
    for num in row:
        row_sum2 += num
    if max_sum2 is None or row_sum2 > max_sum2:
        max_sum2 = row_sum2
print(f"..{max_sum2}")

min_sum2 = None
for row in sales:
    min_sum_row = 0
    for num in row:
        min_sum_row += num
    if min_sum2 is None or min_sum_row < min_sum2:
        min_sum2 = min_sum_row
print(f"..{min_sum2}")

total_sum = 0
for row in sales:
    for num in row:
        total_sum += num
print(total_sum)

for column in range(len(sales[0])):
    column_sum_total = 0
    for row in sales:
        column_sum_total += row[column]
    print(column_sum_total)