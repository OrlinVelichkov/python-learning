# Integrated Mutation + Slicing Challenges — Session 1
# Challenge 1 — Multi-Step Transformation
nums = [10, 20, 30, 40, 50]
nums[1:3] = [200]
nums[0], nums[-1] = nums[-1], nums[0]
nums[1:1] = [111, 222]
print(nums)
# Challenge 2 — Structural Editing
letters = ['a', 'b', 'c', 'd', 'e', 'f']
letters[1:3] = []
letters[-2:-1] = ['X', 'Y']#тук не бях сигурен дали варианта [-2:-1] е правилния избор..
letters[0], letters[-1] = letters[-1], letters[0]
print(letters)
# Challenge 3 — Dynamic Positional Thinking
cities = ['Sofia', 'London', 'Berlin', 'Tokyo', 'Madrid']
cities[len(cities)//2] = 'ROME'
cities[1:2] = []
cities[-1:-1] = ['PARIS', 'OSLO'] #тък мисля че това е начина [-1:-1]
print(cities)
# Integrated Mutation + Slicing Challenges — Final Session
# Challenge 1 — Full Structural Transformation
nums = [1, 2, 3, 4, 5, 6]
nums[1:3] = []
nums[-2:-1] = [500, 600]
# nums[4:5] = [500, 600] #от любопитство, този вариант защо не дава правилен резултат?
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)
# Challenge 2 — Insert + Shrink
letters = ['a', 'b', 'c', 'd']
letters[1:1] = ['X', 'Y']
letters[-2:] = ['Z']#това е моето първо решение, но имам въпрос...
# letters[2:] = ['Z'] Защо положителен slicing не дава резултат, нали индекс 2 е 'c' и трябва да замени до края?
print(letters)
# Challenge 3 — Dynamic Integrated Editing
cities = ['Sofia', 'London', 'Berlin', 'Tokyo', 'Madrid']
cities[len(cities)//2] = 'ROME'
cities[0:1] = []
cities[-1:-1] = ['PARIS']
cities[0], cities[-1] = cities[-1], cities[0]
print(cities)
# Следваща задача — Sequencing Repair Drill
data = ['A', 'B', 'C', 'D', 'E', 'F']
data[1:3] = []
data[-1:-1] = ['X', 'Y']
data[0:1] = ['START']
data[1], data[-1] = data[-1], data[1]
print(data)