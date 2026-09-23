# matrix = [
#     [2, 4, 6],
#     [10, 20, 30],
#     [5, 5, 5]
# ]
# for row in matrix:
#     print(sum(row))

# matrix = [
#     [4, 8, 12],
#     [10, 20, 30],
#     [7, 9, 11]
# ]

# max_row_sum = None
# for row in matrix:
#     current_row = 0
#     for num in row:
#         current_row += num
#     if max_row_sum is None or current_row > max_row_sum:
#         max_row_sum = current_row
# print(f'1. {max_row_sum}')

# col = 1
# column_sum = 0
# for row in matrix:
#     column_sum += row[col]
# print(column_sum)

# result = sum(row[col] for row in matrix)
# print(f'3. {result}')


# result2 = [sum(row[col] for row in matrix) for col in range(len(matrix[0]))]
# print(f'Result {result2}')

sales = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 130],
    [300, 250, 280]
]

for col in range(len(sales[0])):
    column = 0
    for row in sales:
        column += row[col]
    print(column)

results = [sum(row[col] for row in sales) for col in range(len(sales[0]))]
print(f'Results: {results}')

for row in sales:
    print(sum(row))

results3 = sum([sum(row) for row in sales])
print(f'Result 3: {results3}')



results4 = [sum(row[col] for row in sales) for col in range(len(sales[0]))]
print(results4)