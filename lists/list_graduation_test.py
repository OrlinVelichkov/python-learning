#Моите решения за Final Integration Series — Stage 7 Graduation Test

# Challenge 1 — Warehouse Expansion

warehouse_a = ["monitor", "keyboard"]
warehouse_b = ["mouse", "chair"]
inventory = warehouse_a + warehouse_b
short_names = []
if 'mouse' in inventory and 'printer' not in inventory and len(inventory) == 4:
    print('Warehouse validated')
for i, product in enumerate(inventory):
    print(f'Индекс: {i}, Продукт: {product}')
    if len(product) <= 5:
        short_names.append(product)
print(short_names)
# Изисквания:
# 1. Ако:
#    "mouse" съществува
#    "printer" НЕ съществува
#    inventory има точно 4 продукта
#    print("Warehouse validated")
# 2. Изведи всички продукти с индекс.
# 3. Създай:
#    short_names = []
#    Добави в него всички продукти
#    с име до 5 символа включително.
# Накрая:
# print(short_names)

# Challenge 2 — Security Badge System
codes = ["A1", "B2", "C3"]
generated = codes * 4
a_codes = []
if 'A1' in generated and len(generated) == 12:
    print("Security system ready")
for i, code in enumerate(generated):
    print(i, code)
    if code == 'A1': #Тук обмислях дали да ползвам if 'A1' in generated вместо if code == 'A1':, какво мислиш по въпроса?
        a_codes.append(code)
print(a_codes)
# "A1" трябва да съществува
# len(generated) трябва да е 12
# print("Security system ready")
# След това:
# Изведи всички кодове с enumerate().
# След това създай:
# a_codes = []
# и добави само кодовете:
# A1

# Challenge 3 — Temperature Analyzer
temps = [18, 21, 20, 24, 24, 19]
for i in range(len(temps)-1):
    if temps[i + 1] > temps[i]:
        print('Rise')
    elif temps[i + 1] < temps[i]:
        print('Drop')
    elif temps[i + 1] == temps[i]: #тук обмислях да ползвам else: print('Same'), какво мислиш по въпроса?
        print('Same')

# Challenge 4 — Event Registration Audit
registered = ["Ivan", "Maria"]
vip = ["Georgi", "Petar"]
long_names = [] #чудех се дали да създам long_names = [] преди блока с проверки или след for i, person in enumerate(people):?
people = registered + vip
if 'Ivan' in people and 'Stefan' not in people and len(people) == 4:
    for i, person in enumerate(people): #Припомни ми как би изглеждал този ред ако не ползвам enumerate?
        print(f'Index: {i}, Person: {person}')
        if len(person) > 5:
            long_names.append(person)
print(long_names)

# Challenge 5 — Processing Graduation Test
nums = [4, 7, 10, 13, 16, 19, 22, 25]
even_nums = []
odd_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    # elif num % 2 != 0: #знам два варианта с elif и директно с else, дай ми менторски съвет в такъв случай кой метод е по удачен..
    else:
        odd_nums.append(num)
print(even_nums)
print(odd_nums)