#05.08.2026 - 23:25h
# 🚀 Етап 12 — Lesson 1
# sort() vs sorted()
# 🎯 Mission 1
numbers = [9, 4, 7, 1, 8, 2]

# Before
print(numbers)
#After
numbers.sort()
print(numbers)
# 🎯 Mission 2
numbers = [15, 3, 20, 8, 11]
#Original
print(numbers)
#Sorted
new_numbers = sorted(numbers)
print(new_numbers)
print(numbers)
# 🎯 Mission 3
prices = [39, 12, 55, 18, 7]
prices.sort()
print(prices)
scores = [88, 65, 91, 70, 84]
new_score = sorted(scores)
print(new_score)
print(scores)
# 🚀 Етап 12 — Lesson 2
# 🎯 Mission 1
numbers = [14, 3, 27, 9, 18]
#Before
print(numbers)
#After
numbers.sort(reverse=True)
print(numbers)
# 🎯 Mission 2
scores = [88, 72, 95, 61, 80]
#Original:
print(scores)
#Sorted:
new_scores = sorted(scores, reverse=True)
print(new_scores)
#Original again:
print(scores)
# 🎯 Mission 3
prices = [19, 8, 42, 15, 27]
ratings = [4, 2, 5, 3, 1]
prices.sort(reverse=True)
new_ratings = sorted(ratings, reverse=True)
print(prices)
print(ratings)
print(new_ratings)
# 🚀 Етап 12 — Lesson 3
# 🎯 Mission 1
animals = [
    "Elephant",
    "Cat",
    "Tiger",
    "Dog",
    "Giraffe"
]
animals.sort(key=len)
print(animals)
animals.sort(key=len, reverse=True)
print(animals)
# 🎯 Mission 2
cities = [
    "Sofia",
    "London",
    "Rome",
    "Amsterdam",
    "Paris"
]
new_cities = sorted(cities, key=len)
print(new_cities)
new_cities = sorted(cities, key=len, reverse=True)
print(new_cities)
# 🎯 Mission 3
products = [
    "Keyboard",
    "Mouse",
    "Monitor",
    "USB",
    "Laptop"
]
products.sort(key=len)
print(products)
brands = [
    "Apple",
    "HP",
    "Lenovo",
    "Dell",
    "ASUS"
]
new_brands = sorted(brands, key=len)
print(brands)
print(new_brands)