#21.06.2026 - 22:50h
# Task 89 — Priority Orders
orders = [
    "Order-101",
    "Order-102",
    "Order-103",
    "Order-104",
    "Order-105",
    "Order-106",
    "Order-107",
    "Order-108",
    "Order-109"
]
def priority(parameter):
    new_line = []
    for i, order in enumerate(parameter):
        if i % 3 == 0:
            new_line.append('PRIORITY: ' + order)
        elif i % 3 == 1:
            new_line.append('NORMAL: ' + order)
        elif i % 3 == 2:
            new_line.append('NORMAL: ' + order)
    return new_line
print(priority(orders))

#     for i in range(len(parameter)): #Вариант 2 на Task 89 — Priority Orders с range(len()), всъшност кой метод е по pythonic?
#         if i % 3 == 0:
#             new_line.append('PRIORITY: ' + parameter[i])
#         elif i % 3 == 1:
#             new_line.append('NORMAL: ' + parameter[i])
#         elif i % 3 == 2:
#             new_line.append('NORMAL: ' + parameter[i])
#     return new_line
# print(priority(orders))

# Task 90 — VIP Large Orders
orders = [50, 120, 80, 250, 40, 300, 90, 150]
def vip_label(parameter):
    new_line = []
    for i, order in enumerate(parameter):
        if i % 3 == 0:
            new_line.append('VIP: ' + str(order)) #за пръв път вече се сещам преди кода че конкатенцията работи само със str, преди това го поправях като дадеше грешка.
        else:
            new_line.append('NORMAL: ' + str(order))
    return new_line
print(vip_label(orders))
# Task 91 — Weekend Delivery
orders = [50, 120, 80, 250, 40, 300, 90, 150, 70]
def orderflow(parameter):
    new_line = []
    for i, order in enumerate(parameter):
        if i % 3 == 0:
            new_line.append('EXPRESS: ' + str(order))
        elif i % 3 == 1:
            new_line.append('STANDARD: ' + str(order))
        elif i % 3 == 2:
            new_line.append('STANDARD: ' + str(order))
    return new_line
print(orderflow(orders))
# Task 92 — Truck Loading Zones
packages = [12, 8, 15, 22, 7, 18, 11, 9, 30]
def truck(parameter):
    new_line = []
    for i, box in enumerate(parameter):
        if i % 3 == 0:
            new_line.append('ZONA A: ' + str(box))
        elif i % 3 == 1:
            new_line.append('ZONA B: ' + str(box))
        elif i % 3 == 2:
            new_line.append('ZONA C: ' + str(box))
    return new_line
print(truck(packages))