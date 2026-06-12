#12.06.2026 - 22:35h
# Integration Drill 2 (Task 54–59)
# Task 54
temperatures = [24, 31, 22, 28]
def get_lowest(parameter):
    return min(parameter)
print(get_lowest(temperatures))

# Task 54b
temperatures = [24, 31, 22, 28]
def min_degree(parameter):
    min_degree = parameter[0]
    for degree in parameter:
        if degree < min_degree:
            min_degree = degree
    return min_degree # return трябва да е извън цикъла ли?
print(min_degree(temperatures))

# Task 54c
temperatures = [24, 31, 22, 28]
def min_value(parameter):
    min_values = parameter[0]
    for i in range(len(parameter)):
        if parameter[i] < min_values:
            min_values = parameter[i]
    return min_values# return трябва да е извън цикъла ли?
print(min_value(temperatures))
# Task 55
sales = [120, 90, 150, 80]
def total_sum(items):
    return sum(items)
print(total_sum(sales))
# Task 55b
sales = [120, 90, 150, 80]
def total_sum2(items):
    total_amount = 0
    for num in items:
        total_amount += num
    return total_amount
print(total_sum2(sales))
# Task 56
clients = ["Ivan", "Maria", "Petar", "Georgi"]
def alphabet(items):
    return sorted(items)
print(alphabet(clients))
# Task 57
numbers = [10, 20, 30, 40, 50, 60]
def second(items):
    return items[::2]
print(second(numbers))
# Task 57b Искам мнение за това решение..
numbers = [10, 20, 30, 40, 50, 60]
def second2(items):
    new_numbers = []
    for i in range(len(items)):
        if i % 2 == 0:
            new_numbers.append(items[i])
    return new_numbers
print(second2(numbers))
# Task 58
movies = ["Batman", "Avatar", "Interstellar"]
def rev(items):
    return items[::-1] #така ли трябваше да го направя? не с reverse=True?
print(rev(movies))
# Task 59 — Real World
#уморен съм да мисля сценарии за real world, днес ще се съсредоточа върху задания с условие
# Bonus Thinking
def get_last(items):
    return items[-1]
cities = ["Sofia", "Varna", "Plovdiv"]
print(get_last(cities))
#Output: Plovdiv