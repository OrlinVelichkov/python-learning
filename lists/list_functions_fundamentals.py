# Lists + Functions
# Active Coding — Session 1
#Task 1
def hello():
    print('Hello')
hello()
# Task 2
def greet(name):
    print(f'Hello, {name}')
greet('Orlin')

# Task 3
def show_city(city):
    print(f'Добре дошли в град {city}')
show_city('Sofia')
# Task 4
def show_number(number):
    print(f'Номера е {number}')
show_number(100)

# Task 5
def orders(sales):
    print(f'Брой продажбни: {sales}')
orders(100)
# Active Coding — Session 2
# Task 6
names = ['Ivan', 'Maria', 'Petar']
def get_first(name):
    return name[0]
print(get_first(names))

# Task 7
def get_last(name):
    return name[-1]
print(get_last(names))

# Task 8
cities = ["Sofia", "Varna", "Plovdiv"]
def get_second(second_city):
    return second_city[1]
print(get_second(cities))

# Task 9
bookstore = ['Atlantis', 'Nemo', 'Scheherezada', 'Robin Hood']
def first_title(title):
    return title[0]
print(first_title(bookstore))
# Mini Repair Drill
# Task 10
numbers = [100, 200, 300]
def get_first(item):
    return item[0]
print(get_first(numbers))
# Task 11
cities = ["Sofia", "Varna", "Plovdiv"]
def get_last(item):
    return item[-1]
print(get_last(cities))
# Task 12
books = ["Nemo", "Atlantis", "Robin Hood"]
def get_second(item):
    return item[1]
print(get_second(books))
# Task 13
clients = ["Ivan", "Maria", "Petar", "Georgi"]
def get_third(item):
    return item[2]
print(get_third(clients))
#End session 23:11