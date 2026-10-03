#Today I will practice working with dictionaries in Python.

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(my_dict["name"])  # Output: Alice

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"

# Modifying an existing value
my_dict["age"] = 26

# Deleting a key-value pair
del my_dict["city"]

# Iterating through the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

#Start after warm up!
# 🥊 Mission 1 — Remove with del
product = {
    "name": "Mouse",
    "price": 25,
    "stock": 42
}
del product["stock"]
print(product)
# 🥊 Mission 2 — Observe KeyError
user = {
    "name": "Ivan",
    "age": 30
}
# del product["city"]
# print(product)
# 🥊 Mission 3 — pop()
product = {
    "name": "Keyboard",
    "price": 70,
    "stock": 15
}
removed_stock = product.pop("stock")
print(removed_stock)
print(product)
# 🥊 Mission 4 — pop() with Default
product = {
    "name": "Monitor",
    "price": 350
}
print(product.pop("discount", "Not found"))
print(product)
# 🥊 Mission 5 — .get() vs .pop()
user = {
    "name": "Maria",
    "city": "Plovdiv"
}
city1 = user.get("city")
city2 = user.pop("city")
print(f"{city1} and {city2}")
print(user)
# 🥊 Mission 6 — popitem()
course = {
    "title": "Python",
    "level": "Beginner",
    "lessons": 120
}
removed_pair = course.popitem()
print(removed_pair)
print(course)
# 🥊 Mission 7 — Dynamic Remove
account = {
    "owner": "Ivan",
    "balance": 1000,
    "currency": "EUR"
}

field = "currency"
del account[field]
print(account)
# 🥊 Mission 8 — clear()
settings = {
    "theme": "dark",
    "language": "bg",
    "notifications": True
}
settings.clear()
print(settings)
# 🥊 Mission 9 — popitem() Unpacking
user = {
    "name": "Elena",
    "age": 29,
    "city": "Varna"
}
key, value = user.popitem()
print(user)
print(f'{key} and {value}')
# 🔥 Mission 10 — Stage 4 Mini Checkpoint
product = {
    "name": "Laptop",
    "price": 1200,
    "stock": 8,
    "discount": 0.10,
    "category": "Electronics"
}
del product["discount"]
removed_stock = product.pop("stock")
brand_result = product.pop("brand", "Missing")
last_pair = product.popitem()
print(removed_stock)
print(brand_result)
print(last_pair)
print(product)
product.clear()
print(product)

# End of exercises
#start of new exercises

# 🥊 Mission 1 — Inspect Keys
product = {
    "name": "Mouse",
    "price": 25,
    "stock": 42
}
print(product.keys())
print(type(product.keys()))
# 🥊 Mission 2 — Inspect Values
print(product.values())
print(type(product.values()))
# 🥊 Mission 3 — Inspect Items
print(product.items())
print(type(product.items()))
# 🥊 Mission 4 — Convert to Lists
user = {
    "name": "Ivan",
    "age": 30,
    "city": "Sofia"
}
keys_list = list(user.keys())
values_list = list(user.values())
items_list = list(user.items())

print(keys_list)
print(values_list)
print(items_list)
print(type(keys_list))
print(type(values_list))
print(type(items_list))
# 🥊 Mission 5 — Index After Conversion
course = {
    "title": "Python",
    "level": "Beginner",
    "lessons": 120
}
keys = list(course.keys())
values = list(course.values())
items = list(course.items())
print(keys[0])
print(values[1])
print(items[-1])
# 🥊 Mission 6 — Item Tuple Unpacking
product = {
    "name": "Monitor",
    "price": 350,
    "stock": 8
}
items = list(product.items())
key, value = items[0]
print(key)
print(value)
# 🥊 Mission 7 — Inspection Does Not Mutate
settings = {
    "theme": "dark",
    "language": "bg",
    "notifications": True
}
settings.keys()
settings.values()
settings.items()
print(settings)
# 🥊 Mission 8 — Live View
product = {
    "name": "Keyboard",
    "price": 70
}
keys_view = product.keys()
print(keys_view)
product["stock"] = 15
print(keys_view)
# 🥊 Mission 9 — View vs Snapshot
user = {
    "name": "Maria",
    "city": "Plovdiv"
}
keys_view = user.keys()
keys_snapshot = list(user.keys())
user["age"] = 28
print(keys_view)
print(keys_snapshot)
# 🔥 Mission 10 — Stage 5 Mini Checkpoint
product = {
    "name": "Laptop",
    "price": 1200,
    "stock": 8,
    "category": "Electronics"
}
keys_view = product.keys()
values_view = product.values()
items_view = product.items()
print(type(keys_view))
print(type(values_view))
print(type(items_view))

keys_list = list(product.keys())
values_list = list(product.values())
items_list = list(product.items())
print(keys_list[0])
print(values_list[-1])
print(items_list[1])
key, values = items_list[1]
print(key)
print(value)
product["active"] = True
print(keys_view)
print(keys_list)