#10.06.2026 - 23:08h
# Active Coding — Session 6
# Task 44
names = ["Ivan", "Maria", "Petar"]

ages = [25, 31, 28]
def combine_list(list_1, list_2):
    for name, age in zip(list_1, list_2):
        print(f'{name} -> {age}')
combine_list(names, ages)
# Task 45
products = ["Laptop", "Mouse", "Keyboard"]

prices = [1200, 50, 90]

def product_price(parameter_1, parameter_2):
    for product, price in zip(parameter_1, parameter_2):
        print(f'Продукт: {product}: {price} euro')
product_price(products, prices)
# Task 46
cities = ["Sofia", "Varna", "Plovdiv"]

population = [1300000, 330000, 340000]

def cities_population_standings(list_1, list_2):
    for i, (city, people) in enumerate(zip(list_1, list_2), start=1):
        print(f'{i}. {city} -> {people}')
cities_population_standings(cities, population)
# Task 47
team = ['Ronaldo', 'Messi', 'Zidane', 'Ronaldinho']
number_of_player = [7, 10, 10, 10]
golden_ball_awards = [5, 7, 2, 1]
def trinity_lists(item_1, item_2, item_3):
    for i, (first, second, third) in enumerate(zip(item_1, item_2, item_3), start=1):
        print(f'Играч {i}: {first} №{second}, Златни топки: {third}')
trinity_lists(team, number_of_player, golden_ball_awards)
# Task 48 — Real World
learning = ['python', 'english', 'CLI']
times = [60, 20, 60]
def learning_mode(item_1, item_2):
    for subject, time in zip(item_1, item_2):
        print(f'{subject}: {time}')
learning_mode(learning, times)
