#15.06.2026 - 23:22h
# Task 67 — Product Price Transformation
prices = [12, 25, 18, 40, 7, 30]
def increase(parameter):
    new_price = []
    for price in parameter:
        new_price.append(price + 5)
    return new_price
print(increase(prices))
# Task 68 — Customer Names Transformation
customers = ["ivan", "maria", "petar", "georgi"]
def uppercase_names(parameter):
    new_uppercase = []
    for name in parameter:
        new_uppercase.append(name.upper())
    return new_uppercase
print(uppercase_names(customers))
# Task 69 — Customer Labels
customers = ["Ivan", "Maria", "Petar", "Georgi"]
def added_text(paramter):
    new_list = []
    for name in paramter:
        new_list.append('Customer: ' + name)
    return new_list
print(added_text(customers))
# Task 70 — Study Minutes Upgrade
study_minutes = [80, 45, 90, 30, 120, 60]
def multiply(parameter):
    new_study_minutes = []
    for minute in parameter:
        new_study_minutes.append(minute * 2)
    return new_study_minutes
print(multiply(study_minutes))
# Task 71 — Order Labels
orders = [101, 102, 103, 104]
def order_title(parameter):
    new_orders = []
    for order in parameter:
        order = str(order)
        new_orders.append('Order ' + '#' + order)
    return new_orders
print(order_title(orders))
# Task 72 — Discount Labels
prices = [20, 35, 50, 80]
discount = 5
def discounted(parameter1, parameter2):
    new_prices = []
    for price in parameter1:
        new_prices.append(price - parameter2)
    return new_prices
print(discounted(prices, discount))

