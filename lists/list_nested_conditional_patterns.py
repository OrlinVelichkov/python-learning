#23.06.2026 - 23:52h
# Task 100 — Sales Report
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70, 220]
def top_orders(parameter):
    new_line = []
    for order in parameter:
        if 100 <= order <= 199:
            new_line.append('MEDIUM: ' + str(order))
        elif order >= 200:
            new_line.append('LARGE: ' + str(order))
    return new_line
print(top_orders(orders))
# Task 101 — VIP Every Third Order
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70, 220]
def orders_label(parameter):
    new_line = []
    for i, order in enumerate(parameter):
        if order >= 100:
            if i % 3 == 0: #малко теория по математика, тук избрах % 3 не по налучкване, а защото позициите които искаш при делене модулно на 3 връщат 0
                new_line.append('VIP: ' + str(order))
            else:
                new_line.append('STANDARD: ' + str(order))
    return new_line
print(orders_label(orders))
# Task 102 — VIP Large Orders Only
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70, 220]
def vip_orders(parameter):
    new_line = []
    for i, order in enumerate(parameter):
        if order >= 150:
            if i % 3 == 0:
                new_line.append('VIP: ' + str(order))
            else:
                new_line.append('STANDARD: ' + str(order))
    return new_line
print(vip_orders(orders))
# Task 103 — Priority Large Orders
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70, 220]
def order_now(sales):
    new_sales = []
    for i, sale in enumerate(sales):
        if sale >= 100:
            if i % 3 == 0:
                new_sales.append('PRIORITY: ' + str(sale))
            else:
                new_sales.append('NORMAL: ' + str(sale))
    return new_sales
print(order_now(orders))
# Task 104 — VIP Medium and Large Orders
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70, 220]
def new_orders(menu):
    new_list = []
    for i, today_sale in enumerate(menu):
            if 100 <= today_sale <= 199:
                    if i % 3 == 0:
                        new_list.append('VIP MEDIUM: ' + str(today_sale))
                    else:
                         new_list.append('MEDIUM: ' + str(today_sale))
            elif today_sale >= 200:
                    if i % 3 == 0:
                        new_list.append('VIP LARGE: ' + str(today_sale))     
                    else:
                         new_list.append('LARGE: ' + str(today_sale))
    return new_list
print(new_orders(orders))
