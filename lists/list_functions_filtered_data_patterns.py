#13.06.2026 - 23:30h
# Functions Returning Processed Data — Level 2
# Active Coding — Session 7
# Task 60
numbers = [10, 15, 20, 25, 30, 35]
def even_numbers(nums):
    even_numbers_list = []
    for num in nums:
        if num % 2 == 0:
            even_numbers_list.append(num)
    return even_numbers_list
print(even_numbers(numbers))

# Task 61
numbers = [10, 15, 20, 25, 30, 35]
def odd_numbers(nums):
    new_odd_list = []
    for num in nums:
        if num % 2 != 0:
            new_odd_list.append(num)
    return new_odd_list
print(odd_numbers(numbers))
# Task 62
names = ["Ivan", "Maria", "Petar", "Ana"]
def four_character(name_len):
    for name in name_len:
        if len(name) > 4:
            return name #тук не мога да изнеса return с различна идентация, и хваща само първото име с повече от 4 букви
print(four_character(names))

# Task 62b
names = ["Ivan", "Maria", "Petar", "Ana"]
def four_character(name_len):
    for name in name_len:
        if len(name) > 4:
            print(name)
four_character(names)
# Task 63
scores = [88, 72, 95, 61, 100, 67]
def above80(above):
    for num in above:
        if num > 80:
            print(num)
above80(scores)
# Task 64
cities = ["Sofia", "Varna", "Plovdiv", "Burgas"]
def cities_reverse(towns):
    new_cities = []
    for city in towns:
        new_cities.insert(0, city)
    return new_cities
print(cities_reverse(cities))