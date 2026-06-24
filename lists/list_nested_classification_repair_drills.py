#25.06.2026 - 0:25h
# Repair Drill 104A — Same Pattern
orders = [80, 120, 250, 300, 90, 150, 220]
def orders_insight(data):
    new_line_list = []
    for i, order in enumerate(data):
        if 100 <= order <= 199:
            if i % 3 == 0:
                new_line_list.append('FAST MEDIUM: ' + str(order))
            else:
                new_line_list.append('MEDIUM: ' + str(order))
        elif order >= 200:
            if i % 3 == 0:
                new_line_list.append('FAST LARGE: ' + str(order))
            else:
                new_line_list.append('LARGE: ' + str(order))
    return new_line_list
print(orders_insight(orders))
# Repair Drill 104B — Express Medium and Large
orders = [110, 220, 90, 180, 250, 70, 300, 150]
def orderium(parametrium):
    new_line = []
    for i, forsale in enumerate(parametrium):
        if 100 <= forsale <= 199:
            if i % 3 == 0:
                new_line.append('EXPRESS MEDIUM: ' + str(forsale))
            else:
                new_line.append('MEDIUM: ' + str(forsale))
        elif forsale >= 200:
            if i % 3 == 0:
                new_line.append('EXPRESS LARGE: ' + str(forsale))
            else:
                new_line.append('LARGE: ' + str(forsale))
    return new_line
print(orderium(orders))
# Repair Drill 104C — Integration Task      
orders = [120, 80, 250, 180, 300, 90, 150, 220, 400]
def priority(orderstick):
    new_line = []
    for i, sale in enumerate(orderstick):
        if 100 <= sale <= 199:
            if i % 2 == 0:
                new_line.append('PRIORITY MEDIUM: ' + str(sale))
            else:
                new_line.append('MEDIUM: ' + str(sale))
        elif sale >= 200:
            if i % 2 == 0:
                new_line.append('PRIORITY LARGE: ' + str(sale))
            else:
                new_line.append('LARGE: ' + str(sale))
    return new_line
print(priority(orders))
# Task 105 — Special Orders Report
orders = [120, 50, 250, 180, 300, 150, 220, 400, 75]
def new_order_list(parameter):
    new_line = []
    for i, sale in enumerate(parameter):
        if 100 <= sale <= 199:
            if i % 2 == 0:
                new_line.append('PRIORITY MEDIUM: ' + str(sale))
            else:
                new_line.append('MEDIUM: ' + str(sale))
        elif 200 <= sale <= 349:
            if i % 2 == 0:
                new_line.append('PRIORITY LARGE: ' + str(sale))
            else:
                new_line.append('LARGE: ' + str(sale))
        elif sale >= 350:
            if i % 2 == 0:
                new_line.append('PRIORITY SPECIAL: ' + str(sale))
            else:
                new_line.append('SPECIAL: ' + str(sale))
    return new_line
print(new_order_list(orders))  