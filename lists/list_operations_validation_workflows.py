# Part 1 — Fast Warm-up Compression
# Warm-up 1
a = [10, 20]
b = [30]
combined_list = a + b
print(20 in combined_list)
# Warm-up 2
words = ["go"]
repeated_list = words * 5
print(len(repeated_list))
# Warm-up 3
items = ["phone", "tablet", "laptop"]
if len(items) >= 3:
    print(f'Yes, the items have 3 or more elements')
else:
    print(f'No, the items, is smaller')
print('tablet' in items)

# Fusion Drill 1 — + + membership + filtering
a = [5, 10]
b = [15, 20]
combined_list2 = a + b
# for num in combined_list2: #този вариант не се получава, просто бях любопитен какво ще е поведението
#     if num == 20 and num > 10:
#         print(num)
if 20 in combined_list2:
    for num in combined_list2:
        if num > 10:
            print(num)
# Fusion Drill 2 — * + traversal + construction
words = ["ha"]
new_list = []
repeated = words * 4
for word in repeated:
    if len(word) >= 2: #защо ако създаваме new_list = [] след if len(word), резултата е ['ha']
        new_list.append(word)
print(new_list)
# Fusion Drill 3 — len() + decision logic
items = ["phone", "tablet", "laptop", "mouse"]
if len(items) > 3:
    print("Large collection")
else:
    print("Small collection")
print('tablet' in items)
# Fusion Drill 4 — combined operations workflow
nums = [10, 20]
new = []
repeated3 = nums * 3
for num in repeated3:
    if num >= 20:
        new.append(num)
print(new)

# Validation Drill 1 — username check
users = ["ivan", "maria", "peter"]
if 'maria' in users:
    print("User exists")
else:
    print("User not found")
# Validation Drill 2 — collection size validation
cart = ["phone", "tablet"]
if len(cart) >= 2:
    print("Free delivery")
else:
    print("Delivery not available")
# Validation Drill 3 — repeated structure + validation
codes = ["A1"]
repeated4 = codes * 5
if 'A1' in repeated4:
    print(len(repeated4))
# Validation Drill 4 — combined validation flow
products = ["mouse", "keyboard", "monitor"]
if 'keyboard' in products and len(products) > 2:
        print("Valid product collection")

# Real-Style Task 1 — Inventory Check
inventory = ["mouse", "keyboard", "monitor"]
if "keyboard" in inventory and len(inventory) >= 3:
    print("Ready for order")
else:
    print("Inventory problem")
# Real-Style Task 2 — Username Validation
users = ["ivan", "maria", "peter"]
# new_list2 = []
if "admin" not in users:
        # new_list2.extend(users * 2)
        new_list2 = users * 2
print(new_list2)
# Real-Style Task 3 — Cart Workflow
cart = ["phone", "tablet"]
bonus = ["charger"]
combined_cart = cart + bonus
if len(combined_cart) > 2:
    print("Bonus available")
else:
    print('Bonus unavailable')
print('charger' in combined_cart)
# Real-Style Task 4 — Simple Access Logic
roles = ["user", "editor"]
if 'admin'in roles: #тук може би можеше с not in?
    print("Full access")
else:
    print("Restricted access")
# Part 5 — Low-Hint Integration Challenges
# Integration Challenge 1
inventory = ["mouse", "keyboard"]
bonus = ["pad"]
combined_inventory = inventory + bonus
if 'keyboard' in combined_inventory and len(combined_inventory) >= 3:
    print("Store ready") 
# Integration Challenge 2
users = ["ivan", "maria"]
repeated5 = users * 3
print('admin' not in repeated5)
print(len(repeated5))
# Integration Challenge 3
products = ["phone", "tablet", "laptop"]
if len(products) > 2:
    new_list3 = products * 2
print('tablet' in new_list3)
# Integration Challenge 4
codes = ["A1", "B2"]
extra = ["C3"]
combined_codes_list = codes + extra
if "D4" not in combined_codes_list:
    print("Missing code")
print(len(combined_codes_list))