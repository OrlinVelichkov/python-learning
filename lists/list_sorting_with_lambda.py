#09.08.2026 - 20:30h
# 🚀 Етап 12 — Lesson 4
#Мой личен опит за загрявка след теорията
my_favorite_cars = [
    ['Mercedes', 600],
    ['Audi', 800],
    ['Tesla', 900],
    ['Lamborghini', 1100]
]
my_favorite_cars.sort(key=lambda car: car[1], reverse=True)
print(my_favorite_cars)
ranking = sorted(my_favorite_cars, key=lambda car: car[1], reverse=True)
print(f'Нов списък {ranking}')

def topcars(car):
    return car[1]
new_cars = sorted(my_favorite_cars, key=topcars)
print(f'TOP CARS {new_cars}')

# 🚀 Етап 12 — Lesson 4
students = [
    ["Ivan", 5.50],
    ["Maria", 5.90],
    ["Georgi", 4.80],
    ["Elena", 5.70]
]
students.sort(key=lambda student: student[1])
print(students)
# 🎯 Mission 2 — Друг индекс
products = [
    ["Keyboard", 70],
    ["Mouse", 25],
    ["Monitor", 350],
    ["USB Cable", 10],
    ["Laptop", 1200]
]
new_list_of_products = sorted(products, key=lambda item: item[1])
print(f'Original: {products}')
print(f'Sorted: {new_list_of_products}')
# 🎯 Mission 3 — Вече трябва ти да разпознаеш критерия
employees = [
    ["Maria", 32, 2800],
    ["Ivan", 25, 2200],
    ["Georgi", 41, 3500],
    ["Elena", 29, 2600]
]
# Част А
sorted_by_age = sorted(employees, key=lambda employee: employee[1])
sorted_by_salary = sorted(employees, key=lambda employee: employee[2])
print(sorted_by_age)
print(sorted_by_salary)