#19.06.2026 - 23:49h
# Task 80 — Training Session Report
sessions = [80, 45, 90, 120]
def new_line(parameter):
    new_session_list = []
    for i, minute in enumerate(parameter, start=1):
        new_session_list.append('Session ' + str(i) + ': ' + str(minute) + ' minutes')
    return(new_session_list)
print(new_line(sessions))
# Task 81 — Even Position Labels
players = ["Ivan", "Maria", "Petar", "Georgi", "Nikolay"]
def even(parameter):
    even_list = []
    for i, name in enumerate(parameter):
        if i % 2 == 0:
            even_list.append('#' + str(i) + ' ' + name)
        else:
            even_list.append(name)
    return even_list
print(even(players))
# Mini Drill 81A (Mutation Version)
players = ["Ivan", "Maria", "Petar", "Georgi", "Nikolay"]
def even(parameter):
    for i, name in enumerate(parameter):
        if i % 2 == 0:
            parameter[i] = '#' + str(i) + ' ' + name
    return parameter
print(even(players))
# Task 82 — Top 3 Ranking
players = ["Ivan", "Maria", "Petar", "Georgi", "Nikolay"]
def first_three(parameter):
    new_list = []
    for i, name in enumerate(parameter):
        if i < 3:
            new_list.append('TOP: ' + name)
        else:
            new_list.append(name)
    return new_list
print(first_three(players))
# Task 83 — Special Positions
products = ["Mouse", "Keyboard", "Monitor", "Headphones", "Webcam", "Microphone"]
def special(parameter):
    new_list = []
    for i, product in enumerate(parameter):
        if i == 0 or i == 3: #правилен избор ли съм направи за оператор or?
            new_list.append('SPECIAL: ' + product)
        else:
            new_list.append(product)
    return new_list
print(special(products))
# Task 84 — Featured Products
products = [
    "Mouse",
    "Keyboard",
    "Monitor",
    "Headphones",
    "Webcam",
    "Microphone",
    "Speaker",
    "Laptop"
]

def featured(parameter):
    new_list_featured = []
    for i, product in enumerate(parameter):
        if i % 3 == 0:
            new_list_featured.append('FEATURED: ' + product)
        else:
            new_list_featured.append(product)
    return new_list_featured
print(featured(products))
#20.06.2026 - 01:12h