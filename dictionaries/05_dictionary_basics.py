#Dictionaries — Stage 5: Dictionary Inspection
# 🥊 Mission 1 — Inspect Keys
product = {
    "name": "Mouse",
    "price": 25,
    "stock": 42
}
key_lists = product.keys()
# print(key_lists)
print(type(product.keys()))
# 🥊 Mission 2 — Inspect Values
value_lists = product.values()
print(value_lists)
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
#