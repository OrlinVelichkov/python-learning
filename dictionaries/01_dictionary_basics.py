#2026-09-25
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
product = {"name": "Laptop", "price": 1200, "in_stock": True, "discount": 0.15}
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
course = dict(title= "Python", level="Beginner", lessons=120, active=True)
my_course = {"title": "Python", "level": "Beginner", "lessons": 120, "active": True}
print(course)
print(my_course)
print(course["title"])
print(course["lessons"])
print(type(course["active"]))
print(type(course))
