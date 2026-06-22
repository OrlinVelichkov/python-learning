#22.06.2026 - 23:16h
# Task 93 — Premium Delivery Orders
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70]
def orders_limits(limits):
    new_line = []
    for order in limits:
        if order >= 150:
            new_line.append('PREMIUM: ' + str(order))
        elif order < 150:
            new_line.append('STANDARD: ' + str(order))
    return new_line
    # for i in range(len(limits)):
    #     if limits[i] >= 150:
    #         new_line.append('PREMIUM: ' + str(limits[i]))
    #     elif limits[i] < 150:
    #         new_line.append('STANDARD: ' + str(limits[i]))
    # return new_line
print(orders_limits(orders))

# Task 94 — Mixed Order Categories
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70]
def order_cat(precart):
    new_line = []
    for order in precart:
        if order < 100:
            new_line.append('SMALL: ' + str(order))
        elif 100 <= order <= 199:
            new_line.append('MEDIUM: ' + str(order))
        else:
            new_line.append('LARGE: ' + str(order))
    return new_line
print(order_cat(orders))
# Task 95 — Large Orders Only
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70]
def large_orders(parameter):
#     large_sales = []
#     for order in parameter:
#         if order >= 150:
#             large_sales.append(order)
#     return large_sales
# print(large_orders(orders))
    parameter[:] = [x for x in parameter if x >=150]
    return parameter
print(large_orders(orders))
# Task 96 — VIP Orders Report
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70]
def large_label(parameter):
    new_line = []
    for order in parameter:
        if order >= 150:
            new_line.append('VIP: ' + str(order))
    return new_line
print(large_label(orders))
# Task 97 — Premium Medium Orders
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70]
def medium(parameter):
    new_line = []
    for order in parameter:
        if 100 <= order <= 199:
            new_line.append('MEDIUM: ' + str(order))
    return new_line
print(medium(orders))
# Task 98 — Large Orders Report
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70]
def largest(parameter):
    new_line = []
    for order in parameter:
        if order >= 200:
            new_line.append('LARGE: ' + str(order))
    return new_line
print(largest(orders))
# Task 99 — VIP & Large Orders
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70]
def vip_large(parameter):
    new_line = []
    for order in parameter:
        if 100 <= order <= 199:
            new_line.append('VIP: ' + str(order))
        elif order >= 200:
            new_line.append('LARGE: ' + str(order))
    return new_line
print(vip_large(orders)) 