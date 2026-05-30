# Active Repair Drill 1
# Task 1 — OR трябва да е първо
users = ["ivan", "maria"]
roles = ["editor"]

if "ivan" in users and ("admin" in roles or len(users) >= 2):
    print("Access granted")
# Task 2 — AND трябва да е първо
products = ["mouse", "keyboard"]
cart = ["keyboard"]

if ("keyboard" in cart and len(cart) >= 2) or "mouse" in products:
    print("Order accepted")
# Task 3 — OR блок + len проверка
cities = ["Sofia", "Plovdiv"]
drivers = ["Ivan"]

if ("Sofia" in cities or "Varna" in cities) and len(drivers) >= 1:
    print("Delivery active")
# Task 4 — Membership alternatives
products = ["monitor", "mouse", "keyboard"]

if ("monitor" in products or "keyboard" in products) and "printer" not in products:
    print("Inventory valid")
# Task 5 — Access fallback
codes = ["A1", "B2"]
generated = codes * 2

if ("A1" in generated and "X9" not in generated) or len(generated) > 10:
    print("System activated")
# Repair Task 1
users = ["ivan", "maria"]
roles = ["editor"]

# Достъп се дава само ако:
# 1. "ivan" е в users
# И
# 2. има поне едно от следните:
#    - "admin" е в roles
#    - roles съдържа поне 1 роля

if "ivan" in users and ("admin" in roles or len(roles) >= 1):
    print("Access granted")
# Repair Task 2
users = ["ivan", "maria"]
roles = ["editor"]
subscriptions = ["premium"]

# Достъп се дава ако:
#
# 1. Потребителят е в users
#
# И
#
# 2. Изпълнено е поне едно от следните:
#    - има admin роля
#    - има editor роля И premium абонамент
#
# Поправи само if условието.

if "ivan" in users and ("admin" in roles or "editor" in roles and "premium" in subscriptions):
    print("Access granted")
# Repair Task 3
users = ["ivan", "maria"]
roles = ["support"]
subscriptions = ["basic"]

# Достъп се дава ако:
# 1. Потребителят е в users
# И
# 2. Изпълнено е едно от следните:
#    Вариант A:
#    - има admin роля
#    Вариант B:
#    - има editor И premium
#    Вариант C:
#    - има support И premium
# Поправи само if условието.

if "ivan" in users and ("admin" in roles or "editor" in roles and "premium" in subscriptions or "support" in roles and "premium" in subscriptions):
    print("Access granted")
# Repair Task 4
users = ["ivan", "maria"]
roles = ["support"]
subscriptions = ["premium"]
permissions = ["read"]

# Достъп се дава ако:
# 1. Потребителят е в users
# И
# 2. Изпълнено е едно от следните:
#    Вариант A:
#    - има admin роля
#    Вариант B:
#    - има editor
#    - и има поне едно от:
#         premium
#         read permission
#    Вариант C:
#    - има support
#    - и premium
# Поправи само if условието.

if "ivan" in users and (
    "admin" in roles
    or
    (
        "editor" in roles
        and
        (
            "premium" in subscriptions
            or
            "read" in permissions
        )
    )
    or
    (
        "support" in roles
        and
        "premium" in subscriptions
    )
):
    print("Access granted")

# Part 5 — List Operations Workflow Practice
# Task 1 — Team Merge
team_a = ["Ivan", "Maria"]
team_b = ["Petar", "Georgi"]

merged_team = team_a + team_b
if 'Petar' in merged_team and len(merged_team) == 4:
    print('Team ready')
# Task 2 — Access Card Generation
cards = ["A1", "B2"]
generated_cards = cards * 4
if 'A1' in generated_cards and len(generated_cards) == 8:
    print('Cards generated')
# Task 3 — Product Validation
products = ["mouse", "keyboard", "monitor"]
if 'keyboard' in products and 'printer' not in products and len(products) == 3:
    print('Catalog valid')
# Task 4 — Combined Warehouse
warehouse_a = ["monitor", "keyboard"]
warehouse_b = ["mouse"]
inventory = warehouse_a + warehouse_b
if 'mouse' in inventory and 'chair' not in inventory and len(inventory) == 3:
    print('Inventory ready')
# Task 5 — Event Registration
registered = ["Ivan", "Maria"]
vip = ["Georgi"]
all_people = registered + vip
if 'Ivan' in all_people and 'Georgi' in all_people and len(all_people) == 3:
    print('Event confirmed')
# Създай:
# all_people

# Ако:
# - "Ivan" съществува
# - "Georgi" съществува
# - общият брой е 3

# print("Event confirmed")