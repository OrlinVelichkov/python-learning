#Dictionaries — Stage 5: Dictionary Inspection
# 🥊 Mission 1 — Inspect Keys
product = {
    "name": "Mouse",
    "price": 25,
    "stock": 42
}
key_lists = product.keys()
print(key_lists)
print(type(product.keys()))
# 🥊 Mission 2 — Inspect Values
value_lists = product.values()
print(value_lists)
print(type(value_list))
# 🥊 Mission 3 — Inspect Items
print(type(product.items()))
print(product.items())
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
middle_char_of_last_key = keys[len(keys) - 1][len(keys[-1]) // 2]
print(middle_char_of_last_key)
# 🥊 Mission 6 — Item Tuple Unpacking
product = {
    "name": "Monitor",
    "price": 350,
    "stock": 8
}
items = list(product.items())
print(items)
first_item = items[0]
print(first_item)
key, value = first_item
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
key_view = product.keys()
print(key_view)
product["stock"] = 15
print(key_view)
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
print(type(keys_list))
print(type(values_list))
print(type(items_list))
print(keys_list[0])
print(values_list[-1])
print(items_list[1])

second_item = items_list[1]
print(second_item) #контролен print
key, value = second_item
print(f"Ключа е: {key}, а стойността е :{value}")
product["active"] = True
print(keys_view)
print(keys_list)