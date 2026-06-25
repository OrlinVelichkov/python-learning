#26.06.2026 - 0:25h
# Task 106 — Approved Priority Sales
orders = [80, 120, 150, 210, 260, 90, 300, 180, 400]
def order_in_line(parameter):
    new_line = []
    for i, sale in enumerate(parameter):
        if 100 <= sale <= 300:
            if 100 <= sale <= 199:
                if i % 2 == 0:
                    new_line.append('PRIORITY MEDIUM: ' + str(sale))
                else:
                    new_line.append('MEDIUM: ' + str(sale))
            elif 200 <= sale <= 300:
                if i % 2 == 0:
                    new_line.append('PRIORITY LARGE: ' + str(sale))
                else:
                    new_line.append('LARGE: ' + str(sale))
    return new_line
print(order_in_line(orders))
# Task 107 — Premium Approval Report
orders = [50, 120, 180, 220, 260, 90, 310, 150, 280]
def new_sales(parameter):
    new_line = []
    for i, sale in enumerate(parameter):
        if 100 <= sale <= 300:
            if 100 <= sale <= 199:
                if i % 2 == 1:
                    new_line.append('PRIORITY MEDIUM: ' + str(sale))
                else:
                    new_line.append('MEDIUM: ' + str(sale))
            elif 200 <= sale <= 300:
                if i % 2 == 1:
                    new_line.append('PRIORITY LARGE: ' + str(sale))
                else:
                    new_line.append('LARGE: ' + str(sale))
    return new_line
print(new_sales(orders))
# Task 108 — Dynamic Threshold Report
orders = [50, 120, 180, 220, 260, 90, 310, 150, 280]
def dualparam(orders, threshold):
    new_line = []
    for i, sale in enumerate(orders): #в enumerate() само един параметър ли може да се ползва?
        if sale >= threshold:
            if i % 2 == 0:
                new_line.append('PRIORITY: ' + str(sale))
            else:
                new_line.append('NORMAL: ' + str(sale))
    return new_line
print(dualparam(orders, 200))
# Task 109 — Dynamic Label Report
orders = [50, 120, 180, 220, 260, 90, 310, 150, 280]
def troyparam(orders, threshold, label):
    new_line = []
    for i, sale in enumerate(orders):
        if sale >= threshold:
            if i % 2 == 0:
                new_line.append(label + ' ' + str(sale))
            else:
                new_line.append('NORMAL: ' + str(sale))
    return new_line
print(troyparam(orders, 200, "VIP"))