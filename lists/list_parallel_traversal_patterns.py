#27.06.2026 - 0:22h
# Task 110A — Customer Order Report
customers = ["Ivan", "Maria", "Petar", "Georgi"]
orders = [120, 250, 80, 300]
def customer_orders(cust_parameter, order_parameter):
    new_order_list = []
    for customer, order in zip(cust_parameter, order_parameter):
        new_order_list.append(customer + ': ' + str(order))
    return new_order_list
print(customer_orders(customers, orders))
# Task 110B — Customer Threshold Report
customers = ["Ivan", "Maria", "Petar", "Georgi"]
orders = [120, 250, 80, 300]
def clients(customers_p, orders_p, threshold):
    new_line = []
    for name, sale in zip(customers_p, orders_p):
        if sale >= threshold:
            new_line.append(name + ': ' + str(sale))
    return new_line
print(clients(customers, orders, 200))
# Task 111 — Indexed Customer Report
customers = ["Ivan", "Maria", "Petar", "Georgi", "Nikolay"]
orders = [120, 250, 80, 300, 150]
def dualparameter(parameter1, parameter2):
    new_line = []
    for i, (name, sale) in enumerate(zip(parameter1, parameter2)):
        if sale >= 100:
            if i % 2 == 0:
                new_line.append('PRIORITY ' + name + ': ' + str(sale))
            else:
                new_line.append('NORMAL ' + name + ': ' + str(sale))
    return new_line
print(dualparameter(customers, orders))
# Task 112 — Customer City Report
customers = ["Ivan", "Maria", "Petar", "Georgi"]
orders = [120, 250, 80, 300]
cities = ["Sofia", "Plovdiv", "Varna", "Burgas"]
def troy(item1, item2, item3):
    new_line = []
    for name, order, city in zip(item1, item2, item3):
        if order >= 100:
            new_line.append(name + ' | ' + city + ' | ' + str(order))
    return new_line
print(troy(customers, orders, cities))
# Task 113 — VIP Customer City Report
customers = ["Ivan", "Maria", "Petar", "Georgi", "Nikolay"]
orders = [120, 250, 80, 300, 150]
cities = ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse"]

def megatask(customer_p, order_p, city_p, threshold_p):
    new_line = []
    for i, (name, order, city) in enumerate(zip(customer_p, order_p, city_p)):
        if order >= threshold_p:
            if i % 2 == 0:
                new_line.append('VIP ' + name + ' | ' + city + ' | ' + str(order))
            else:
                new_line.append('STANDARD ' + name + ' | ' + city + ' | ' + str(order))
    return new_line
print(megatask(customers, orders, cities, 150))