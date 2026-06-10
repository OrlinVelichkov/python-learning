#10.06.2026 - 23:08h
# Integration Drill 2
# Functions Returning Processed Data
# Task 49
scores = [88, 72, 95, 61]
def get_first(item):
    return item[0]
print(get_first(scores))
# Task 50
cities = ["Sofia", "Varna", "Plovdiv", "Burgas"]
def last_city(item):
    return item[-1]
print(last_city(cities))
# Task 50b
cities = ["Sofia", "Varna", "PloVdiv", "Burgas"]
def middle(item):
    return item[len(item)//2][len(item[len(item)//2])//2]
print(middle(cities))
# Task 51
books = ["Nemo", "Atlantis", "Robin Hood", "Sherlock"]
def first_two(items):
    return items[:2]
print(first_two(books))
# Task 52
orders = [10, 20, 30, 40, 50, 60]
def last_three_orders(items):
    return items[-3:]
print(last_three_orders(orders))
# Task 53
profits = [120, 90, 250, 180]
def top_profit(top):
    return max(top)
print(top_profit(profits))
# Task 53b тук исках да покажа най голямата печалба по този начин, какво мислиш? Заши печата и none?
profits = [120, 90, 250, 180]
def top_profit2(top):
    max_num = 0
    for i in range(len(top)):
        if top[i] > max_num:
            max_num = top[i]
    return max_num
print(top_profit2(profits))