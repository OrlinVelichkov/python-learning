#29.07.2026 - 20:00h
# Stage 11 — Automation Drills (Session 1)

# Какво обхождам – редове или колони?
# Къде започва акумулаторът?
# Къде приключва акумулацията?
# Кога трябва да направя append()?
# Кога ми трябва enumerate(), а кога не?


# Drill 1 — Индексиране
# matrix = [
#     [4, 7, 2, 9],
#     [8, 1, 5, 3],
#     [6, 4, 7, 2],
#     [9, 3, 1, 8]
# ]
# matrix[1] --> [8, 1, 5, 3]
# matrix[2][3] --> 2
# matrix[0][2] --> 2
# matrix[3][0] --> 9


# # Drill 2 — Какво съдържа променливата?
# Итерация 1

# row = [4, 7, 2, 9]

# --------------

# Итерация 2

# row =  [8, 1, 5, 3]

# --------------

# Итерация 3

# row = [6, 4, 7, 2],


# --------------

# Итерация 4

# row = [9, 3, 1, 8]
# # Drill 3 — Какво съдържа column?
# for column in range(len(matrix[0])):
# Итерация 1

# column = 0

# --------------

# Итерация 2

# column = 1

# --------------

# Итерация 3

# column = 2

# --------------

# Итерация 4

# column = 3

# Drill 4 — Най-важният
# for column in range(len(matrix[0])):
#     for row in matrix:
#         print(row[column], end=" ")

#     print()
#Резултат
# 4 8 6 9
# 7 1 4 3
# 2 5 7 1
# 9 3 2 8
# 🚀 Drill 5 — Акумулатор
matrix = [
    [3, 5, 2],
    [8, 1, 4],
    [6, 7, 9]
]
second_row_sum = 0
# for column in range(len(matrix[0])):
#     for row in matrix:
#         second_row_sum += row[column]
# print(second_row_sum)
for num in matrix[1]: 
    second_row_sum += num
print(second_row_sum)

# 🚀 Drill 6 — Избор на колона
column_sum = 0
for row in matrix:
    print(row[2])
