lst = list(['123456789'])
print(lst)

xs = [10, 20, 30]
i = 7

# 1. проверка на границите
value = xs[i] if -len(xs) <= i < len(xs) else None

# 2. try / except — идиоматично за Python (EAFP)
try:
    value = xs[i]
except IndexError:
    value = None

# 3. срез — срезовете никога не хвърлят IndexError
value = (xs[i:i + 1] or [None])[0]

area = [1, 2, 3]
id(area) == id(area)
before = id(area)
# area.append(4)   
# print(area)
       # мутация — обектът остава същият
id(area) == before
area.append(4)  
area = area + [4]     
print(area)
    # ново присвояване — НОВ обект
id(area) == before

my_list = [1, 3, 5, 7, 9]
print(my_list)
my_list_range = list(range(1, 10, 2))
print(my_list_range)
my_list_comprehension = [2 * x + 1 for x in range(5)]
print(my_list_comprehension)