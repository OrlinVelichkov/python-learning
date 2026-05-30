# Advanced Slice Mutation Patterns — Session 1
# structural editing
# Drill 1 — Shrink List
nums = [10, 20, 30, 40, 50]
nums[1:4] = [999] 
print(nums)
# Drill 2 — Expand List
letters = ['a', 'b', 'c']
letters[1:2] = ['X', 'Y', 'Z']
print(letters)
# Drill 3 — Remove via Slicing
cities = ['Sofia', 'London', 'Berlin', 'Tokyo', 'Madrid']
cities[1:3] = []
print(cities)
# Advanced Slice Mutation Patterns — Reinforcement Drill
# Задача 1 — Shrink Harder
nums = [1, 2, 3, 4, 5, 6]
nums[1:5] = [999]
print(nums)
# Задача 2 — Expand Harder
letters = ['a', 'b', 'c']
letters[1:] = ['X', 'Y', 'Z', 'W']
print(letters)
# Задача 3 — Remove Middle Section
cities = ['Sofia', 'London', 'Berlin', 'Tokyo', 'Madrid']
cities[2:4] = []
print(cities)
# Задача 4 — Insert via Slicing
nums = [10, 20, 30]
nums[1:1] = [100, 200] #Бележка за repair drill: тук не знаех начина, погледнах hint-a, какво стои зад логиката че [1:1] указва мястото между 10 и 20
print(nums)
# Задача 5 — Full Structural Mutation
data = [100, 200, 300, 400, 500]
data[1:3] = []
data[-1:] = [999, 888]#интересно, ако не ползвам : след -1 замества с целия списък [999, 888]
print(data)