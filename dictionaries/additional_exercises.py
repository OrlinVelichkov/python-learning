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
print(account["owner"])
# 🥊 Mission 9 — Literal Key vs Variable Key

data = {}

key = "price"
data['key'] = 100
data[key] = 200
print(data)
# 🔥 Mission 10 — Stage 3 Mini Checkpoint
new_field = "active"
new_value = True
field_to_change = "price"
discounted_price = 70
product = {
    "name": "Mechanical Keyboard",
    "price": 80,
    "stock": 10
}
product['price'] = 75
product['category'] = 'Accessoaries'
product['stock'] += 5
product[new_field] = new_value
product[field_to_change] = discounted_price
print(product)