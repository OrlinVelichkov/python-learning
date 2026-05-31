# Моите решение за Part 6: Integrated List Operations.

# Challenge 1 — Warehouse Control System
warehouse_a = ["monitor", "keyboard", "mouse"]
warehouse_b = ["chair", "desk"]
inventory = warehouse_a + warehouse_b
if 'mouse' in inventory and 'printer' not in inventory and len(inventory) >= 5:
    print("Inventory validated")
    for i, item in enumerate(inventory):
        print(f"На index: {i} -> {item}")
# Изисквания:
# 1. Ако inventory съдържа "mouse"
#    и НЕ съдържа "printer"
#    и има поне 5 продукта
#    print("Inventory validated")
# 2. След това обхождане:
#    Изведи всеки продукт с неговия индекс.
# Пример:
# 0 monitor
# 1 keyboard

# Challenge 2 — Access Badge Generator
codes = ["A1", "B2", "C3"]
generated = codes * 3
if 'A1' in generated and len(generated) == 9:
    print('Generation successful')
for i, code in enumerate(generated):
    print(f"Index: {i} Code: {code}")
# Изисквания:
# 1. Ако:
#    "A1" съществува
#    и дължината е 9
#    print("Generation successful")
# 2. Изведи:
#    Index: 0 Code: A1
#    Index: 1 Code: B2
# Използвай enumerate()

# Challenge 3 — Neighbor Validation
temps = [18, 21, 20, 24, 28]
for i in range(len(temps)-1):
    if temps[i + 1] > temps[i]:
        print('Rise')
    elif temps[i + 1] < temps[i]:
        print("Drop")
# Направи обхождане така, че:
# ако следващата температура е по-висока от текущата:
# print("Rise")
# ако е по-ниска:
# print("Drop")

# Challenge 4 — Registration System
registered = ["Ivan", "Maria"]
vip = ["Georgi", "Petar"]
people = registered + vip
if 'Ivan' in people and 'Stefan' not in people and len(people) == 4:
    print('Registration valid')
for i, person in enumerate(people):
    print(f'Index: {i}, Person: {person}')
# "Ivan" трябва да съществува
# "Stefan" НЕ трябва да съществува
# people трябва да са точно 4
# Ако е вярно:
# print("Registration valid")
# След това:
# изведи всички участници с индекс.

# Challenge 5 — Processing Pattern
nums = [4, 7, 10, 13, 16, 19]
even_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
print(even_nums)
# Създай
# even_nums = []
# Добави в него само четните числа.
# Накрая:
# print(even_nums)