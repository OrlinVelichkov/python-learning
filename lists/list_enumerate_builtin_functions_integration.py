# Integration Challenge
# Task 13
sales = [120, 90, 150, 80]
for i, sale in enumerate(sales, start=1):
    print(f'Day {i}: {sale}')
print(f'Total: {sum(sales)}')
print(f'Best: {max(sales)}')
print(f'Worst: {min(sales)}')
# Task 14
english_words = [25, 18, 30, 22]
for i, word in enumerate(english_words, start=1):
    print(f'Session {i}: {word}')
print(f'Total words: {sum(english_words)}')
print(f'Best session: {max(english_words)}')
print(f'Weakest session: {min(english_words)}')
print(sorted(english_words))
# Task 15
profits = [400, 120, 250, 90, 180]
for i, profit in enumerate(profits, start=1):
    print(f'Month {i}: {profit}')
sorted_ascending = sorted(profits)
sorted_descending = sorted(profits, reverse=True)
print(sorted_ascending)
print(sorted_descending)
# Task 16 (Real World)
cleaning_clients_cost = [650, 510, 499.80, 600]
for i, house in enumerate(cleaning_clients_cost, start=1):
    print(f'Клиент: {i}: {house:.2f} euro')
print(f'Total: {sum(cleaning_clients_cost)} euro')
print(f'Top client: {max(cleaning_clients_cost)} euro')
print(f'Worst client: {min(cleaning_clients_cost)} euro')
print(sorted(cleaning_clients_cost))
# Task 17