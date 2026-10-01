#Dictionaries — Stage 4: Removing Dictionary Data.
# 🥊 Mission 1 — Remove with del
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
del my_dict["age"]
print(my_dict)

product = {
    "name": "Mouse",
    "price": 25,
    "stock": 42
}
del product['stock']
print(product)
# 🥊 Mission 2 — Observe KeyError
user = {
    "name": "Ivan",
    "age": 30
}
# del user['city']
print(user)

# 🥊 Mission 3 — pop()
item = {
    "name": "Keyboard",
    "price": 45,
    "stock": 10
}
removed_stock = item.pop("stock")
print(item)
print("Removed stock:", removed_stock)

product = {
    "name": "Keyboard",
    "price": 70,
    "stock": 15
}
removed_stock = product.pop('stock')
print(removed_stock)
print(product)

# 🥊 Mission 4 — pop() with Default
inventory = {
    "apples": 10,
    "oranges": 5
}
removed_bananas = inventory.pop("bananas", 0)
print("Removed bananas:", removed_bananas)
print(inventory)

product = {
    "name": "Monitor",
    "price": 350
}

result = product.pop('discount', 'Not found')
print(result)
print(product)

# 🥊 Mission 5 — .get() vs .pop()
data = {
    "name": "Alice",
    "age": 25
}

# Using .get()
city = data.get("city", "Not found")
print("City (using get):", city)

# Using .pop()
city = data.pop("city", "Not found")
print("City (using pop):", city)
print("Data after pop:", data)

user = {
    "name": "Maria",
    "city": "Plovdiv"
}
city1 = user.get('city')
print(city1)
print(user)

city2 = user.pop('city')
print(city2)
print(user)

# 🥊 Mission 6 — popitem()
inventory = {
    "apples": 10,
    "oranges": 5,
    "bananas": 7
}
removed_item = inventory.popitem()
print("Removed item:", removed_item)
print(inventory)

course = {
    "title": "Python",
    "level": "Beginner",
    "lessons": 120
}

removed_pair = course.popitem()
print(course)
print(removed_pair)

# 🥊 Mission 7 — Dynamic Remove
dynamic_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

key_to_remove = "b"
removed_value = dynamic_dict.pop(key_to_remove, None)
print(f"Removed {key_to_remove}: {removed_value}")
print(dynamic_dict)

account = {
    "owner": "Ivan",
    "balance": 1000,
    "currency": "EUR"
}

field = "currency"

del account[field]
print(account)

# 🥊 Mission 8 — clear()
inventory = {
    "apples": 10,
    "oranges": 5,
    "bananas": 7
}
inventory.clear()
print("Cleared inventory:", inventory)
settings = {
    "theme": "dark",
    "language": "bg",
    "notifications": True
}
settings.clear()
print(settings)

# 🥊 Mission 9 — popitem() Unpacking
profile = {
    "username": "john_doe",
    "email": "john@example.com",
    "age": 28
}

key, value = profile.popitem()
print(f"Removed pair: {key} = {value}")
print(profile)

user = {
    "name": "Elena",
    "age": 29,
    "city": "Varna"
}

key, value = user.popitem()
print(key)
print(value)
print(user)

# 🔥 Mission 10 — Stage 4 Mini Checkpoint
product = {
    "name": "Laptop",
    "price": 1200,
    "stock": 8,
    "discount": 0.10,
    "category": "Electronics"
}
del product['discount']
removed_stock = product.pop('stock')
brand = product.pop('brand', 'Missing')
last_pair = product.popitem()
print(removed_stock)
print(brand)
print(last_pair)
print(product)
product.clear()
print(product)