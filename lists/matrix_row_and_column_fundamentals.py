#30.07.2026 - 19:45h - Bootcamp
# Matrix Bootcamp — Module 1: Rows (Missions 1–3)
matrix = [
    [3, 5, 2],
    [8, 1, 4],
    [6, 7, 9]
]
# Mission 1 — Последният ред
for num in matrix[2]:
    print(num)
# Mission 2 — Сума на първия ред
first_row_sum = 0
for num in matrix[0]:
    first_row_sum += num
print(first_row_sum)
# Mission 3 — Четни числа във втория ред
for num in matrix[1]:
    if num % 2 == 0:
        print(num)
# Matrix Bootcamp — Module 2: Columns
matrix = [
    [3, 5, 2],
    [8, 1, 4],
    [6, 7, 9]
]
# 🎯 Mission 1
for row in matrix:
    print(row[0])
# 🎯 Mission 1.2 (просто исках да опитам това...)
for column in range(len(matrix[0])):
    for row in matrix:
        if column % 2 != 0:
            print(row[column])
        else:
            print(row[column])
# 🎯 Mission 2
for row in matrix:
    print(row[2])
# 🎯 Mission 3
second_column_sum = 0
for row in matrix:
    second_column_sum +=row[1]
print(f'Second column sum = {second_column_sum}')
