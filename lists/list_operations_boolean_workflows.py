# 🥊 Mission 1 — List Concatenation
frontend = ["HTML", "CSS"]
backend = ["Python", "SQL"]
full_stack = frontend + backend
print(full_stack)
print(frontend)
print(backend)
# 🥊 Mission 2 — Repetition
pattern = ["A", "B"]
repeated_pattern = pattern * 3
print(repeated_pattern)
# 🥊 Mission 3 — Membership
products = ["Keyboard", "Mouse", "Monitor", "Webcam"]
if 'Mouse' in products:
    print('Mouse found')
if 'Laptop' not in products:
    print('Laptop missing')
# 🥊 Mission 4 — Check Before Append
cart = ["Mouse", "Monitor"]
if 'Keyboard' not in cart:
    cart.append('Keyboard')
print(cart)
# 🥊 Mission 5 — Boolean Workflow
skills = ["Python", "Git", "HTML", "CSS"]
if 'Python' in skills and 'Git' in skills:
    print('Backend basics ready')
if 'JavaScript' in skills or 'HTML' in skills:
    print('Web skill found')
# 🥊 Mission 6 — if / elif / else
inventory = ["Mouse", "Keyboard"]
if 'Laptop' in inventory:
    print('Laptop available')
elif 'Keyboard' in inventory:
    print('Keyboard available')
else:
    print('Target products unavailable')
# 🥊 Mission 7 — List State
orders = ["A102", "A103", "A104", "A105"]
if len(orders) == 0:
    print("No orders")
elif 1 <= len(orders) <= 3:
    print("Normal workload")
else:
    print("High workload")
# 🔥 Mission 8 — Stage 7 Mini Checkpoint
available_products = [
    "Keyboard",
    "Mouse",
    "Monitor",
    "Webcam"
]

cart = [
    "Mouse",
    "Keyboard"
]
if 'Monitor' in available_products and 'Monitor' not in cart:
    cart.append('Monitor')
if 'Mouse' in cart and 'Keyboard' in cart:
    print('Core accessories selected')
if 'Laptop' in cart or 'Monitor' in cart:
    print('Major product selected')
if len(cart) >= 3:
    print('Cart ready')
else:
    print('Add more products')
print(cart)