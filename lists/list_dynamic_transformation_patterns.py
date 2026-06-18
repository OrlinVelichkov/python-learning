 #18.06.2026 - 23:22h
# Task 73 — VIP Customer Labels
customers = ["ivan", "maria", "petar", "georgi"]
def new_line(parameter):
    new_list = []
    for name in parameter:
        new_list.append('VIP: ' + name.upper())
    return new_list
print(new_line(customers))

# Task 74 — Dynamic Customer Labels
customers = ["ivan", "maria", "petar", "georgi"]
label = "VIP"
def dynamic_label(parameter1, parameter2):
    customers2 = []
    for name in parameter1:
        customers2.append(parameter2 +':'+' '+ name.capitalize())
    return customers2
print(dynamic_label(customers, label))
# Task 75 — Product Report Labels
products = ["Mouse", "Keyboard", "Monitor", "Headphones"]
price = 50
def detailed_price(parameter1, parameter2):
    new_price_list = []
    for product in parameter1:
        new_price_list.append('Product: ' + product + ' - Price: ' + str(parameter2))
    return new_price_list
print(detailed_price(products, price))
# Task 76 — Revenue Projection
sales = [10, 25, 40, 15]
price_per_sale = 12
def multiply(parameter1, parameter2):
    multiply_list = []
    for sale in parameter1:
        multiply_list.append(sale * parameter2)
    return multiply_list
print(multiply(sales, price_per_sale))
# Task 77 — Email Generator
customers = ["Ivan", "Maria", "Petar", "Georgi"]
domain = "@caliber.bg"
def emailgen(parameter1, parameter2):
    customers2 = []
    for name in parameter1:
        customers2.append(name+parameter2) #Как да променя съществуващия list customers = ["Ivan", "Maria", "Petar", "Georgi"] с обновената версия с имейли вместо да правя нов list?
    return customers2
print(emailgen(customers, domain))
# Task 78 — Username Generator
users = ["Ivan Petrov", "Maria Ivanova", "Petar Georgiev"]
def users_list(parameter):
    new_users = []
    for name in parameter:
        new_users.append(name.lower())
    return new_users
print(users_list(users))
# Task 79 — User ID Labels
users = ["Ivan", "Maria", "Petar", "Georgi"]
start_id = 1000
def user_id(parameter1, parameter2):
    user_list = []
    for i, user in enumerate(parameter1):
        user_list.append('User-'+str(parameter2 + i) + ': ' + user)
    return user_list
print(user_id(users, start_id))
