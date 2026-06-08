#08.06.2026 - 22:10h
# Integration Drill 1
# Task 29
scores = [88, 72, 95, 61]
def get_first_result(items):
    return items[0]
print(get_first_result(scores))
# Task 30
cities = ["Sofia", "Varna", "Plovdiv", "Burgas"]
def last_city(items):
    return items[-1]
print(last_city(cities))
def middle_city(items):
    return items[len(items)//2]
print(middle_city(cities))

# Task 31
books = ["Nemo", "Atlantis", "Robin Hood", "Sherlock"]
def first_two(title):
    return title[:2]
print(first_two(books))
# Task 32
orders = [10, 20, 30, 40, 50, 60]
def get_last_three(order):
    return order[-3:]
print(get_last_three(orders))
# Task 33
profits = [120, 90, 250, 180]
def get_maximus(profit):
    return max(profit)
print(get_maximus(profits))
# Task 34
temperatures = [24, 31, 22, 28]
def get_lower(degree):
    return min(degree)
print(get_lower(temperatures))
# Task 35
sales = [120, 90, 150, 80]
def total_sales(sale):
    return sum(sale)
print(total_sales(sales))
# Task 36
clients = ["Ivan", "Maria", "Petar", "Georgi"]
def alphabet_sorted(words):
    return sorted(words)
print(alphabet_sorted(clients))
# Task 37 — Real World
total_python_learning = [80, 80, 60, 100, 500, 1000, 1500, 2000]
def total_minutes(hour):
    return sum(hour) // 60
print(total_minutes(total_python_learning))

# Bonus
def get_first(items):
    return items[0]
numbers = [10, 20, 30]
print(get_first(numbers))
#Output 10
#Край 08.06.2026 - 23:14h