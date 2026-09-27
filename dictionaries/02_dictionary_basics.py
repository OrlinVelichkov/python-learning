#2026-09-2026
# Dictionaries — Stage 2: Accessing Values
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
print(product.get("stock"))
# Mission 4 — .get() with Default
customer = {
    "name": "Ivan",
    "city": "Sofia"
}
print(customer.get("phone", "Not provided"))
# Mission 5 — Existing Key with .get()
course = {
    "title": "Python",
    "lessons": 120
}
print(course.get("title"))
print(course.get("lessons"))
# Mission 6 — Default Does Not Mutate
user = {
    "name": "Elena"
}
email = user.get("email", "no email")
print(email)
print(user)
# Mission 7 — None as Real Value
profile = {
    "name": "Georgi",
    "phone": None
}

phone = profile.get("phone")
email = profile.get("email")
print(phone)
print(email)
# Mission 8 — Choose the Correct Access Method
order = {
    "id": 1001,
    "customer": "Ivan",
    "total": 250
}
print(order["id"])
print(order["customer"])
print(order.get("note", "no note"))
# Final Checkpoint — Stage 2
product = {
    "name": "Monitor",
    "price": 350,
    "stock": 8,
    "discount": None
}
print(product["name"])
print(product.get("price"))
print(product.get("brand"))
print(product.get("category", "Unknown"))
print(product.get("discount"))
print(product)
#end
