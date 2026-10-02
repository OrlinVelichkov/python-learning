#exercise 1
# 🥊 Mission 1 — Remove with del
product = {
    "name": "Mouse",
    "price": 25,
    "stock": 42
}

print(product)
del product['stock']
print(product)
# 🥊 Mission 2 — Observe KeyError
user = {
    "name": "Ivan",
    "age": 30
}
# del user['city']
# print(user)
# 🥊 Mission 3 — pop()
product = {
    "name": "Keyboard",
    "price": 70,
    "stock": 15
}
print(product)
removed_stock = product.pop('stock')
print(f'Removed: {removed_stock}')
print(product)
# 🥊 Mission 4 — pop() with Default
product = {
    "name": "Monitor",
    "price": 350
}
option = product.pop('discount', None)
option2 = product.pop('discount', 'Not found')
print(option)
print(option2)
# 🥊 Mission 5 — .get() vs .pop()
user = {
    "name": "Maria",
    "city": "Plovdiv"
}
city1 = user.get('city')
print(city1)
city2 = user.pop('city')
print(city2)
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
del account['owner']
print(account)
final = account.popitem()
print(final)
print(account)
# 🥊 Mission 8 — clear()
settings = {
    "theme": "dark",
    "language": "bg",
    "notifications": True
}
print(settings)
settings.clear()
print(settings)
# 🥊 Mission 9 — popitem() Unpacking
user = {
    "name": "Elena",
    "age": 29,
    "city": "Varna"
}
key, value = user.popitem()
print(f'Key - {key}, Value - {value}')
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
brand = product.pop('brand', 'No found')
last_pair = product.popitem()
print(removed_stock)
print(brand)
print(last_pair)
print(product)
product.clear()
print(product)