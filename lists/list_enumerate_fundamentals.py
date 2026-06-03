# Built-in Functions
# enumerate()
# Active Coding — Session 1
# Task 1
names = ["Ivan", "Maria", "Petar"]
for i, name in enumerate(names):
    print(i, name)
# Task 2
cities = ["Sofia", "Varna", "Plovdiv"]
for i, city in enumerate(cities):
    print(i, city)
# Task 3
scores = [88, 72, 95, 61]
for i, score in enumerate(scores):
    print(i, score)
# Task 4
fitness_diet_calories = [210, 314, 715, 289]
for i, per_eat in enumerate(fitness_diet_calories):
    print(i, per_eat)
# Bonus Observation
nums = [10, 50, 111, 200]
for i in range(len(nums)):
    print(i, nums[i])
nums2 = [10, 50, 111, 200]
for i, item in enumerate(nums2):
    print(i, item)
# Mini Repair Drill
# Task 5
fruits = ["apple", "banana", "orange"]
for i, fruit in enumerate(fruits):
    print(f'Fruit #{i}: {fruit}')
# Task 6
temperatures = [24, 28, 31, 22]
for i, degree in enumerate(temperatures):
    print(f'Day {i}: {degree}')
# Task 7
english_words = [25, 18, 30, 22]
for i, word in enumerate(english_words):
    print(f'Session {i}: {word}')
# Task 8
my_book_list = ['Harry Poter', 'Nemo', 'Sherlock Homes']
for i, book in enumerate(my_book_list):
    print(f'Рафт: {i+1}: {book}')