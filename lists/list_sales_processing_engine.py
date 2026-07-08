# Task 116 — Sales Processing Engine
#08.07.2026 - 21:15h

customers = [
    "Ivan",
    "Maria",
    "Petar",
    "Georgi",
    "Nikolay",
    "Elena",
    "Stefan"
]

orders = [
    120,
    250,
    80,
    320,
    180,
    450,
    210
]

cities = [
    "Sofia",
    "Plovdiv",
    "Varna",
    "Burgas",
    "Ruse",
    "Pleven",
    "Stara Zagora"
]

threshold = 150
priority_label = "FAST"
vip_label = "VIP"


def deals(customers_p, orders_p, cities_p, threshold, priority_label, vip_label):
    new_line = []
    for i, (name, sale, city) in enumerate(zip(customers_p, orders_p, cities_p)):
        if sale >= threshold:
            if sale >= 300:
                new_line.append(vip_label + ' | ' + name + ' | ' + city + ' | ' + str(sale))
            else:
                if i % 2 == 0:
                    new_line.append(priority_label + ' | ' + name + ' | ' + city + ' | ' + str(sale))
                else:
                    new_line.append('STANDARD' + ' | ' + name + ' | ' + city + ' | ' + str(sale))
    return new_line
print(deals(customers, orders, cities, threshold, priority_label, vip_label))

# Task 117 — Boss Fight
customers = [
    "Ivan",
    "Maria",
    "Petar",
    "Georgi",
    "Nikolay",
    "Elena",
    "Stefan",
    "Radoslav"
]

orders = [
    120,
    250,
    80,
    320,
    180,
    450,
    210,
    95
]

cities = [
    "Sofia",
    "Plovdiv",
    "Varna",
    "Burgas",
    "Ruse",
    "Pleven",
    "Stara Zagora",
    "Shumen"
]
threshold = 100
vip_limit = 300
priority_label = "FAST"
vip_label = "VIP"

def bossseven(customersp, ordersp, citiesp, threshold, vip_limit, priority_label, vip_label):
    new_boss_line = []
    for i, (name, order, city) in enumerate(zip(customersp, ordersp, citiesp)):
        if order >= threshold:
            if order >= vip_limit:
                new_boss_line.append(vip_label + " | " + name + " | " + city + " | " + str(order))
            else:
                if i % 2 == 0:
                    new_boss_line.append(priority_label + " | " + name + " | " + city + " | " + str(order))
                else:
                    new_boss_line.append('STANDARD' + " | " + name + " | " + city + " | " + str(order))
    return new_boss_line
print(bossseven(customers, orders, cities, threshold, vip_limit, priority_label, vip_label))




    





