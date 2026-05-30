# Boolean Composition & Workflow Decisions
# Part 1  Boolean Warm-up
users = ["ivan", "maria", "peter"]
if 'maria' in users and len(users) >= 3:
    print("Users validated")
# Warm-up 2
products = ["phone", "tablet"]
bonus = ["charger"]
combined = products + bonus
if 'charger' in combined and len(combined) > 2:
    print("Bonus active")
# Warm-up 3
roles = ["user", "editor"]
if 'admin' not in roles and len(roles) < 5:
    print("Restricted mode")
# Part 2 — Boolean Composition Drills
# Boolean Drill 1 — and + validation
users = ["ivan", "maria", "peter"]
if 'ivan' in users and len(users) == 3:
    print("User system valid")
# Boolean Drill 2 — or logic
roles = ["user"]
if 'admin' in roles or len(roles) > 2:
    print("Extended permissions")
#ако има грешка в кода ми, прочети си условието за Boolean Drill 2 — or logic
# Boolean Drill 3 — mixed collection logic
products = ["phone", "tablet"]
bonus = ["charger"]
combined = products + bonus
if 'charger' in combined and len(combined) == 3:
    print("Bundle ready")
# Boolean Drill 4 — not in + or
codes = ["A1", "B2"]
if 'C3' not in codes or len(codes) < 5:
    print("Validation warning")
# Part 3 — Workflow Decision Problems
# Workflow Problem 1 — Access Validation
users = ["ivan", "maria"]
roles = ["user", "editor"]
if 'ivan' in users and 'admin' not in roles:
    print("Limited access")
# Workflow Problem 2 — Inventory Logic
inventory = ["mouse", "keyboard"]
extra = ["monitor"]
combined_inventory = inventory + extra
if 'monitor' in combined_inventory or len(combined_inventory) > 5:
    print("Inventory expanded")
# Workflow Problem 3 — Cart Validation
cart = ["phone", "tablet"]
bonus = ["charger"]
combined_cart = cart + bonus
if "charger" in combined_cart and len(combined_cart) == 3:
    print("Cart valid")
# Workflow Problem 4 — Repeated Structure Validation
codes = ["A1"]
repeated_list = codes * 5
if "A1" in repeated_list and len(repeated_list) > 3:
    print("Codes accepted")
# Part 4 — Low-Hint Boolean Workflow Challenges
# Challenge 1 — Access Validation System
users = ["ivan", "maria", "petar"]
roles = ["editor", "support"]
username = "ivan"

if username in users and 'admin' not in roles and len(users) >=3:
    print("Limited access granted")
# Challenge 2 — Product Availability
products = ["mouse", "keyboard", "monitor"]
cart = ["keyboard", "monitor"]
if 'keyboard' in products and len(cart) >= 2 and 'printer' not in cart:
    print('Order ready') 
# Challenge 3 — Delivery Validation
cities = ["Sofia", "Plovdiv", "Varna"]
active_drivers = ["Georgi", "Ivan"]
selected_city = "Sofia"
if selected_city in cities and len(active_drivers) >= 2 and 'Blocked' not in cities:
    print("Delivery available")
# Challenge 4 — Repetition Workflow
codes = ["A1", "B2"]
generated_codes = codes * 3
if 'A1' in generated_codes and len(generated_codes) > 5 and 'X9' not in generated_codes:
    print("Code generation successful")
# Challenge 5 — Combined Inventory Logic
warehouse_a = ["monitor", "keyboard"]
warehouse_b = ["mouse", "chair"]
combined_inventory = warehouse_a + warehouse_b
if 'chair' in combined_inventory and len(combined_inventory) >= 4 and 'printer' not in combined_inventory:
    print("Inventory validated")
# Part 4B — Mixed AND / OR Workflow Challenges
# Challenge 1 — VIP Access Logic
users = ["ivan", "maria", "petar"]
roles = ["support"]
username = "ivan"

if username in users and 'admin' in roles or 'support' in roles:
    print("VIP access granted")
# Challenge 2 — Shipping Validation
products = ["mouse", "keyboard", "monitor"]
cart = ["keyboard"]
if 'keyboard' in cart and len(cart) >= 2 or 'monitor' in products:
    print("Shipping approved")
# Challenge 3 — Multi-City Delivery
cities = ["Sofia", "Plovdiv"]
drivers = ["Ivan"]

selected_city = "Varna"
if selected_city in cities or 'Sofia' in cities and len(drivers) >= 1:
    print("Delivery started")
# Challenge 4 — Combined Inventory Rules
warehouse_a = ["monitor"]
warehouse_b = ["mouse", "keyboard"]

combined = warehouse_a + warehouse_b
if 'monitor' in combined and 'printer' in combined or len(combined) >= 3:
    print("Inventory system ready")
# Challenge 5 — Repetition Access System
codes = ["A1", "B2"]

generated = codes * 2
if 'A1' in generated and 'X9' not in generated or len(generated) > 10:
    print("System activated")
users = ["ivan", "maria"]
roles = ["editor"]

if "ivan" in users and "admin" in roles or (len(users) >= 2):
    print("Access granted")
cities = ["Sofia"]
drivers = ["Ivan"]

if ("Varna" in cities or "Sofia" in cities) and len(drivers) >= 1:
    print("Delivery active")
products = ["monitor", "mouse", "keyboard"]

if ("monitor" in products or "keyboard" in products) and len(products) >= 3:
    print("Inventory ready")