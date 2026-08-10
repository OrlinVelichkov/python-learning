#10.08.2026 - 23:10h
# 🥊 Lambda Coding Drill
# 🔹 Drill 1 — Загрявка
players = [
    ["Alex", 18],
    ["Martin", 32],
    ["Daniel", 11],
    ["Victor", 25]
]
sorted_players = sorted(players, key=lambda player: player[1])
print(sorted_players)

def sorted_players_score(player):
    return player[1]
sorted_players_classic_function = sorted(players, key=sorted_players_score)
print(sorted_players_classic_function)
# 🔹 Drill 2 — Смяна на индекса
games = [
    ["Cyberpunk", 2020, 59],
    ["Minecraft", 2011, 29],
    ["Elden Ring", 2022, 69],
    ["GTA V", 2013, 39]
]
games_by_year = sorted(games, key=lambda game: game[1])
games_by_price = sorted(games, key=lambda game: game[2])
print(games)
print(games_by_year)
print(games_by_price)

def sorted_by_years(game):
    return game[1]
def sorted_by_price(game):
    return game[2]
games_by_year_classic_function = sorted(games, key=sorted_by_years)
games_by_price_classic_function = sorted(games, key=sorted_by_price)
print(games_by_year_classic_function)
print(games_by_price_classic_function)
# 🔹 Drill 3 — Добавяме reverse=True
products = [
    ["Belt", 19.90],
    ["Knee Support", 14.90],
    ["Wrist Support", 8.90],
    ["Backpack", 39.90]
]
def products_highest_price_item(item):
    return item[1]
products_highest_price_classic_function = sorted(products, key=products_highest_price_item, reverse=True)
products_highest_price = sorted(products, key=lambda item: item[1], reverse=True)
print(products_highest_price_classic_function)
print(products_highest_price)
# 🔹 Drill 4 — Не ти давам индекса
cars = [
    ["BMW", "Germany", 250],
    ["Toyota", "Japan", 180],
    ["Ferrari", "Italy", 340],
    ["Volvo", "Sweden", 210]
]
def cars_by_power_rank(car):
    return car[2]
cars_by_power_classic_function = sorted(cars, key=cars_by_power_rank, reverse=True)
cars_by_power = sorted(cars, key=lambda car: car[2], reverse=True)
print(cars_by_power_classic_function)
print(cars_by_power)
# 🔥 Drill 5 — Два различни критерия
orders = [
    ["Order-101", 3, 59.70],
    ["Order-102", 1, 19.90],
    ["Order-103", 5, 99.50],
    ["Order-104", 2, 39.80]
]
def orders_by_quantity_rank(order):
    return order[1]
def orders_by_total_rank(order):
    return order[2]

orders_by_quantity_classic_function = sorted(orders, key=orders_by_quantity_rank)
orders_by_total_classic_function = sorted(orders, key=orders_by_total_rank, reverse=True)
orders_by_quantity = sorted(orders, key=lambda order: order[1])
orders_by_total =sorted(orders, key=lambda order: order[2], reverse=True)
print(orders_by_quantity_classic_function)
print(orders_by_total_classic_function)
print(orders_by_quantity)
print(orders_by_total)
# 🔥 Drill 6 — def → lambda
movies = [
    ["Interstellar", 169],
    ["Alien", 117],
    ["Dune", 155],
    ["Avatar", 162]
]
def get_duration(movie):
    return movie[1]
sorted_movies = sorted(movies, key=get_duration)
sorted_movies_lambda = sorted(movies, key=lambda movie: movie[1])
print(sorted_movies)
print(sorted_movies_lambda)
# 🧨 Drill 7 — Без подсказки
laptops = [
    ["HP EliteBook", 32, 1299],
    ["Lenovo ThinkPad", 16, 999],
    ["Dell Precision", 64, 1899],
    ["ASUS Zenbook", 24, 1199],
    ["HP ZBook", 48, 1599]
]
def by_ram(model):
    return model[1]
def by_price(price):
    return price[2]
laptops_by_ram = sorted(laptops, key=by_ram, reverse=True)
print(laptops_by_ram)
laptops_by_price = sorted(laptops, key=by_price)
print(laptops_by_price)
laptops_ranking_lambda_by_ram = sorted(laptops, key=lambda model: model[1], reverse=True)
print(laptops_ranking_lambda_by_ram)
laptops_ranking_lambda_by_price = sorted(laptops, key=lambda model: model[2])
print(laptops_ranking_lambda_by_price)
# 👑 Drill 8 — Mini Boss
employees = [
    ["Anna", "Developer", 4200, 5],
    ["Peter", "Designer", 3100, 7],
    ["Maria", "Developer", 4800, 8],
    ["Georgi", "Manager", 5500, 10],
    ["Elena", "QA", 2900, 3]
]
def by_salary_def(employee):
    return employee[2]
def by_experience_def(employee):
    return employee[3]
def by_name_def(employee):
    return employee[0]
by_salary = sorted(employees, key=by_salary_def, reverse=True)
by_experience = sorted(employees, key=by_experience_def, reverse=True)
by_name = sorted(employees, key=by_name_def)
print(by_salary)
print(by_experience)
print(by_name)

by_salary_lambda = sorted(employees, key=lambda employee: employee[2], reverse=True)
by_experience_lambda = sorted(employees, key=lambda employee: employee[3],reverse=True)
by_name_lambda = sorted(employees, key=lambda employee: employee[0])
print(by_salary_lambda)
print(by_experience_lambda)
print(by_name_lambda)