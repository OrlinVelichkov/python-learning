#20.06.2026 - 22:52h
# Task 85 — Bonus Badge
players = ["Ivan", "Maria", "Petar", "Georgi", "Nikolay", "Stefan"]
def bonus_label(player_bonus):
    new_line = []
    for i, player in enumerate(player_bonus):
        if i % 2 == 0:
            new_line.append('BONUS: ' + player)
        else:
            new_line.append(player)
    return new_line
print(bonus_label(players))
# Task 86 — Gold & Silver Ranking
players = ["Ivan", "Maria", "Petar", "Georgi", "Nikolay", "Stefan"]
def golden_rush(gold_and_silver):
    new_line = []
    for i, player in enumerate(gold_and_silver):
        if i % 2 == 0:
            new_line.append('GOLD: ' + player)
        # elif i % 2 != 0 #пробвах и с elif, резултата е същия като с else, кой вариант е по pythonic, може би else защото имаме само 2 избора?
        else:
            new_line.append('SILVER: ' + player)
    return new_line
print(golden_rush(players))
# Task 87 — Bronze, Silver, Gold
players = ["Ivan", "Maria", "Petar", "Georgi", "Nikolay", "Stefan"]
def top_winners(parameter):
    new_line = []
    for i, name in enumerate(parameter):
        if i % 3 == 0:
            new_line.append('GOLD: ' + name)
        elif i % 3 == 1:
            new_line.append('SILVER: ' + name)
        else:
            new_line.append('BRONZE: ' + name)
    return new_line
print(top_winners(players))
# Repair Drill 87A
products = [
    "Mouse",
    "Keyboard",
    "Monitor",
    "Headphones",
    "Webcam",
    "Microphone",
    "Speaker",
    "Laptop",
    "Printer"
]
def alpha(parameter):
    new_line = []
    for i, product in enumerate(parameter):
        if i % 3 == 0:
            new_line.append('A: ' + product)
        elif i % 3 == 1:
            new_line.append('B: ' + product)
        elif i % 3 == 2: #умишлено не ползвах else
            new_line.append('C: ' + product)
    return new_line
print(alpha(products))
# Repair Drill 87B
employees = [
    "Ivan",
    "Maria",
    "Petar",
    "Georgi",
    "Nikolay",
    "Stefan",
    "Martin",
    "Elena"
]
def team_colour(parameter):
    new_line = []
    for i, name in enumerate(parameter):
        if i % 2 == 0:
            new_line.append('TEAM RED: ' + name)
        elif i % 2 == 1:
            new_line.append('TEAM BLUE: ' + name)
    return new_line
print(team_colour(employees))
#умишлено не ползвах else за да тренирам остатък, е по подразбиране каквото остане щом не е 0, а избрах % 2 а не % 3 защото имаме два избора на на цвят RED и BLUE и си казах няма логика да ползвам 3
# Repair Drill 87C
clients = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H"
]
def label(parameter):
    new_line = []
    for i, client in enumerate(parameter):
        if i % 3 == 0:
            new_line.append('VIP: ' + client)
        elif i % 3 == 1:
            new_line.append('NORMAL: ' + client)
        elif i % 3 == 2:
            new_line.append('NORMAL: ' + client)
    return new_line
print(label(clients))
# Task 88 — Delivery Routes
cities = [
    "Sofia",
    "Plovdiv",
    "Varna",
    "Burgas",
    "Ruse",
    "Pleven",
    "Stara Zagora",
    "Shumen",
    "Dobrich"
]
def marked_cities(parameter): #Вариант с enumerate()
    new_line = []
    for i, city in enumerate(parameter):
        if i % 3 == 0:
            new_line.append('A: ' + city)
        elif i % 3 == 1:
            new_line.append('B: ' + city)
        elif i % 3 == 2:
            new_line.append('C: ' + city)
    return new_line
print(marked_cities(cities))

def marked_cities(parameter): #Вариант с len()
    new_line = []
    for i in range(len(parameter)):
        if i % 3 == 0:
            new_line.append('A: ' + parameter[i])
        elif i % 3 == 1:
            new_line.append('B: ' + parameter[i])
        elif i % 3 == 2:
            new_line.append('C: ' + parameter[i])
    return new_line
print(marked_cities(cities))
