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
    sum_row = 0
    for element in row:
        sum_row += element
    print(sum_row)

max_row_sum = None
for row in sales:
    current_sum = 0
    for element in row:
        current_sum += element
    if max_row_sum is None or current_sum > max_row_sum:
        max_row_sum = current_sum
print(max_row_sum)

min_row_sum = None
for row in sales:
    min_sum = 0
    for element in row:
        min_sum += element
    if min_row_sum is None or min_sum < min_row_sum:
        min_row_sum = min_sum
print(min_row_sum)

#D
total = 0
for row in sales:
    for element in row:
        total += element
print(total)
#D.1
tottal = 0
for row in sales:
    tottal += sum(row)
print(tottal)

#E
for column in range(len(sales[0])):
    column_value = 0
    for row in sales:
        column_value += row[column]
    print(f'Резултат: {column_value}')

#F
column_one = 1
column_result = 0
for row in sales:
    column_result += row[column_one]
print(column_result)

for row in sales:
    print(max(row))

fruits = ['Banana', 'Kiwi', 'Orange']
while fruits:
    print(fruits[0])
    fruits.remove(fruits[0])