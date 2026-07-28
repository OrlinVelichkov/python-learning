#28.07.2026 - 20:10h
# 🚀 Stage 11 – Lesson 6
# Column Processing (Обработка по колони)
matrix = [
    [5, 8, 1, 10],
    [7, 3, 9, 15],
    [4, 6, 2, 20]
]
for column in range(len(matrix[0])):
    sum_column = 0
    for row in matrix:
        sum_column += row[column]
    print(f"Column {column + 1} sum = {sum_column}")
# Exercise 1
matrix = [
    [2, 8, 5, 1, 9],
    [7, 4, 6, 3, 2],
    [1, 5, 8, 7, 4],
    [9, 2, 3, 6, 5]
]
for column in range(len(matrix[0])):
    sum_column = 0 
    for row in matrix:
        sum_column += row[column] 
    print(f'Column {column + 1} sum = {sum_column}')
# 🏁 Stage 11 – Lesson 6
# Final Challenge
matrix = [
    [4, 7, 2, 9],
    [8, 1, 5, 3],
    [6, 4, 7, 2],
    [9, 3, 1, 8]
]
sum_row = []
sum_column = []
for i, row in enumerate(matrix):
    row_sum = 0
    for num in row:
        row_sum += num
    sum_row.append(row_sum)
    print(f'Row {i + 1} sum = {row_sum}')
# for i, column in enumerate(matrix[0]): 
#     col_sum = 0
#     for row in matrix:
#         col_sum += row[i]
#         sum_column.append(row[i])
#     print(f'Column {i + 1} sum {col_sum}')
for column in range(len(matrix[0])):
    col_sum = 0
    for row in matrix:
        col_sum += row[column]
    sum_column.append(col_sum)
    print(f'Column {column + 1} sum {col_sum}') 
if sum_row[0] > sum_column[0]:
    print(f'Row 1 is bigger')
else:
    print(f'Column 1 is bigger')