#04.08.2026 - 18:30h
# Каква информация трябва да изведа?
# Какви променливи ще ми трябват?
# Тези променливи:
# живеят ли ✅ за всеки ред или ✅ за цялата матрица?
# олко пъти ще обхождам матрицата?
# Мога ли да събера повече информация с едно обхождане?
# 🏆 Stage 11 — Final Boss Fight
matrix = [
    [3, 5, 2],
    [8, 1, 4],
    [6, 7, 9]
]
total_even_numbers = 0
total_odd_numbers = 0
total_even_sum = 0
total_odd_sum = 0
matrix_total = 0
for position, row in enumerate(matrix, start=1):
    print(f'Row {position}')
    even_count = 0
    odd_count = 0
    even_sum = 0
    odd_sum = 0
    for num in row:
        if num % 2 == 0:
            even_count +=1
            even_sum += num
            # total_even_numbers += 1
            # total_even_sum += num
        else:
            odd_count += 1
            odd_sum += num
            # total_odd_numbers += 1 
            # total_odd_sum += num
    total_even_numbers += even_count
    total_even_sum += even_sum
    total_odd_numbers += odd_count
    total_odd_sum +=odd_sum
    row_total = even_sum + odd_sum
    matrix_total += row_total
    print(f'Even count = {even_count}')
    print(f'Odd count = {odd_count}')
    print(f'Even sum = {even_sum}')
    print(f'Odd sum = {odd_sum}')
    print(f'Row total = {row_total}')
    print()
print(f'====================')
print(f'MATRIX REPORT')
print(f'====================')
print(f'Total even numbers = {total_even_numbers}')
print(f'Total odd numbers = {total_odd_numbers}')
print(f'Total even sum = {total_even_sum}')
print(f'Total odd sum = {total_odd_sum}')
print(f'Matrix total = {matrix_total}')
#04.08.2026 - 19:30h