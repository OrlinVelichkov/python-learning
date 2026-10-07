# Stage 1
# 🥊 Mission 1 — Create Your First Dictionary
person = {
"name": "Ivan",
"age": 30,
"city": "Sofia"
}
print(person)
# 🥊 Mission 2 — Access by Key
print(person["name"])
print(person["age"])
print(person["city"])
# 🥊 Mission 3 — Different Value Types
product = {
"name": "Laptop",
"price": 1200,
"in_stock": True,
"discount": 0.15
}
print(type(product["name"]))
print(type(product["price"]))
print(type(product["in_stock"]))
print(type(product["discount"]))
# 🥊 Mission 4 — Empty Dictionary
data1 = {}
data2 = dict()
print(type(data1))
print(type(data2))
# 🥊 Mission 5 — Duplicate Key
user = {
    "name": "Ivan",
    "age": 30,
    "name": "Maria"
}
print(user)
print(user["name"])
# 🥊 Mission 6 — List vs Dictionary
product_list = ["Mouse", 25, 42]
product_dict = {
    "name": "Mouse",
    "price": 25,
    "stock": 42
}
print(product_list[1])
print(product_dict["price"])
# 🔥 Mission 7 — Stage 1 Mini Checkpoint
course = {
"title": "Python",
"level": "Beginner",
"lessons": 120,
"active": True
}
print(course)
print(course["title"])
print(course["lessons"])
print(type(course["active"]))
print(type(course))
#Stage 2
# Mission 1 — Direct Access
user = {
    "name": "Maria",
    "age": 28,
    "city": "Plovdiv"
}
print(user["name"])
print(user["age"])
print(user["city"])
# Mission 2 — Observe KeyError
product = {
    "name": "Keyboard",
    "price": 70
}
# print(product["stock"])
# Mission 3 — Safe Access with .get()
print(product.get('stock'))

# Mission 4 — .get() with Default
customer = {
    "name": "Ivan",
    "city": "Sofia"
}
print(customer.get('phone', 'Missing'))

# Mission 5 — Existing Key with .get()
course = {
    "title": "Python",
    "lessons": 120
}
print(course.get('title'))
print(course.get('lessons'))

# Mission 6 — Default Does Not Mutate
user = {
    "name": "Elena"
}
email = user.get('email', 'no email')
print(email)
print(user)
# Mission 7 — None as Real Value
profile = {
    "name": "Georgi",
    "phone": None
}
phone = profile.get("phone")
email = profile.get('email')
print(phone)
print(email)
# Mission 8 — Choose the Correct Access Method
order = {
    "id": 1001,
    "customer": "Ivan",
    "total": 250
}
print(order['id'])
print(order['customer'])
print(order.get('note', 'No note'))
# Final Checkpoint — Stage 2
product = {
    "name": "Monitor",
    "price": 350,
    "stock": 8,
    "discount": None
}
print(product['name'])
print(product.get('price'))
print(product.get('brand'))
print(product.get('category', "Unknown"))
print(product.get('discount'))
print(product)

# Stage 3: Adding & Updating Data
# 🥊 Mission 1 — Add New Key
product = {
    "name": "Keyboard",
    "price": 70
}
product['stock'] = 15
print(product)
# 🥊 Mission 2 — Update Existing Key
user = {
    "name": "Ivan",
    "age": 30
}
user["age"] = 31
print(user)

# 🥊 Mission 3 — Add Several Fields
car = {
    "brand": "Toyota"
}
car['model'] = 'Corolla'
car['year'] = 2025
car['electric'] = False
print(car)
# 🥊 Mission 4 — Value from Variable
product = {
    "name": "Monitor",
    "price": 350
}

new_price = 320

product["price"] = new_price
print(product["price"])
print(product)
# 🥊 Mission 5 — Dynamic Key
user = {
    "name": "Maria"
}

field = "city"

user[field] = 'Plovdiv'
print(user)

# 🥊 Mission 6 — Dynamic Key + Dynamic Value
product = {
    "name": "Laptop"
}

field = "stock"
quantity = 8
product[field] = quantity
print(product)

# 🥊 Mission 7 — Update Using Current Value
product = {
    "name": "Mouse",
    "stock": 20
}
product["stock"] += 5
print(product)
# 🥊 Mission 8 — Decrease Existing Value
account = {
    "owner": "Ivan",
    "balance": 1000
}
account["balance"] -= 250
print(account)

# 🥊 Mission 9 — Literal Key vs Variable Key
data = {}

key = "price"

data['key'] = 100
data[key] = 200
print(data)

# 🔥 Mission 10 — Stage 3 Mini Checkpoint
product = {
    "name": "Mechanical Keyboard",
    "price": 80,
    "stock": 10
}
new_field = "active"
new_value = True
field_to_change = "price"
discounted_price = 70
product["price"] = 75
product['category'] = 'Accessories'
product["stock"] += 5
product[new_field] = new_value
product[field_to_change] = discounted_price
print(product)

# Stage 4
# 🥊 Mission 1 — Remove with del
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
# print(user)
# 🥊 Mission 3 — pop()
product = {
    "name": "Keyboard",
    "price": 70,
    "stock": 15
}
removed_stock = product.pop('stock')
print(removed_stock)
print(product)
# 🥊 Mission 4 — pop() with Default
product = {
    "name": "Monitor",
    "price": 350
}
removed_discount = product.pop('discount', 'Not found')
print(removed_discount)
print(product)
# 🥊 Mission 5 — .get() vs .pop()
user = {
    "name": "Maria",
    "city": "Plovdiv"
}
city1 = user.get('city')
city2 = user.pop('city')
print(city1)
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
key, value = last_pair
print(key, value)
print(removed_stock)
print(brand)
print(last_pair)
print(product)
product.clear()
print(product)
# Stage 5
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
first_item = items[0]
key, value = first_item
print(key, value)
# 🥊 Mission 7 — Inspection Does Not Mutate
settings = {
    "theme": "dark",
    "language": "bg",
    "notifications": True
}
settings.keys()
settings.values()
settings.items()
print(settings.keys())
print(settings.values())
print(settings.items())     
print(settings)
# 🥊 Mission 8 — Live View
product = {
    "name": "Keyboard",
    "price": 70
}
keys_view = product.keys()
print(keys_view)
product['stock'] = 15
print(keys_view)
# 🥊 Mission 9 — View vs Snapshot
user = {
    "name": "Maria",
    "city": "Plovdiv"
}
keys_view = user.keys()
keys_snapshot = list(user.keys())
user["age"] = 28
print(f'Live view: {keys_view}')
print(f'Snapshot: {keys_snapshot}')
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
key, value = items_list[1]
print(key, value)
product['active'] = True
print(keys_view)
print(keys_list)

# Stage 6
# 🥊 Mission 1 — Traverse Keys
product = {
    "name": "Mouse",
    "price": 25,
    "stock": 42
}
for key in product:
    print(key)
# 🥊 Mission 2 — Traverse Values
for value in product.values():
    print(value)
# 🥊 Mission 3 — Traverse Items
user = {
    "name": "Ivan",
    "age": 30,
    "city": "Sofia"
}
for key, value in user.items():
    print(f'{key} - {value}')
# 🥊 Mission 4 — Filter
scores = {
    "Ivan": 82,
    "Maria": 95,
    "Georgi": 68,
    "Elena": 88
}
for name, score in scores.items():
    if score >= 80:
        print(name, score)
# 🥊 Mission 5 — Counter
count = 0
for score in scores.values():
    if score >= 80:
        count += 1
print(count)
# 🥊 Mission 6 — Accumulator
total = 0
prices = {
    "mouse": 25,
    "keyboard": 70,
    "monitor": 350,
    "headphones": 55
}
for price in prices.values():
    total += price
print(total)
print(sum(prices.values()))
# 🥊 Mission 7 — Update Through Traversal
stock = {
    "mouse": 10,
    "keyboard": 5,
    "monitor": 3
}
for key in stock:
    stock[key] += 2
print(stock)
# 🥊 Mission 8 — Key + Value Logic
products = {
    "mouse": 25,
    "keyboard": 70,
    "monitor": 350,
    "cable": 10
}
for item, price in products.items():
    if price > 50:
        print(f'{item}: {price}')
# 🔥 Mission 9 — Stage 6 Mini Checkpoint
inventory = {
    "mouse": 12,
    "keyboard": 7,
    "monitor": 5,
    "headphones": 20
}
count = 0
total = 0
for key in inventory:
    print(key)
for value in inventory.values():
    print(value)
for key, value in inventory.items():
    print(key, value)
for stock in inventory.values():
    if stock >= 10:
        count += 1
for total_stock in inventory.values():
    total += total_stock
for key in inventory:
    inventory[key] += 1
print(inventory)
print(count)
print(total)
