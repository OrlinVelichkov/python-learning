#03.07.2026 - 19:10h
# Task 114 — Integrated Processing I
customers_list = ["Ivan", "Maria", "Petar", "Georgi", "Nikolay"]
orders_list = [120, 250, 80, 300, 150]
def report_orders(customers, orders, threshold, priority_label):
    new_line = []
    for i, (customer, order) in enumerate(zip(customers, orders)):
        if order >= threshold:
            if i % 2 == 0:
                new_line.append(priority_label + ' ' + customer + ': ' + str(order))
            else:
                new_line.append('STANDARD ' + customer + ': ' + str(order))
    return new_line
print(report_orders(customers_list, orders_list, 150, "VIP"))

# Task 115 — Multi-Level Customer Report
customers_list = ["Ivan", "Maria", "Petar", "Georgi", "Nikolay", "Elena"]

orders_list = [120, 250, 80, 320, 180, 450]
def order_insight(customers, orders, threshold, priority_label, vip_label):
    new_line = []
    for i, (customer, order) in enumerate(zip(customers, orders)):
        if order >= threshold:
            if order >= 300:
                new_line.append(vip_label + ' ' + customer + ': ' + str(order))
            else:
                if i % 2 == 0:
                    new_line.append(priority_label + ' ' + customer + ': ' + str(order))
                else:
                    new_line.append('STANDARD ' + customer + ': ' + str(order))
    return new_line
print(order_insight(customers_list, orders_list, 150, "FAST", "VIP"))

