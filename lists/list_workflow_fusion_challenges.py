# Warm-up 1
nums = [3, 14, 5, 20, 7]
for num in nums:
    if num % 2 == 0:
        num //= 2
        print(num)
# Warm-up 2
words = ["cat", "airplane", "dog", "helicopter"]
for i, word in enumerate(words):
    if len(word) > 6:
        print(f'{i} -> {word}')
# Warm-up 3
nums = [1, 3, 9, 12, 15]
for num in nums:
    if num % 2 == 0:
        print(num)
        break
# Workflow Problem 1
nums = [5, 12, 7, 20, 3, 18]
new_even = []
for num in nums:
    if num %2 == 0:
        if num > 15:
            new_even.append(num *10)
        else:
            new_even.append(num)
print(new_even)
# Workflow Problem 2
words = ["cat", "airplane", "bus", "helicopter", "bike"]
for i, word in enumerate(words):
    if len(word) > 8:
        print(f'{i} -> {word}')
        break
# Workflow Problem 3
nums = [4, 9, 5, 12, 8, 15]
new_list = []
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        data = nums[i] + nums[i+1]
        new_list.append(data)
print(new_list)
# Workflow Problem 4
names = ["Ivan", "Maria", "Peter", "Anna"]
scores = [5, 3, 6, 2]
cities = ["Sofia", "Varna", "Plovdiv", "Burgas"]
flag = False
for i in range(len(names)):
    if scores[i] < 4:
        flag = True
        print(f'{names[i]} -> {scores[i]} -> {cities[i]}')
print(flag)
# Part 3 — Neighbor + Logic Fusion
nums = [3, 9, 5, 12, 4, 10]
new_list = []
for i in range(len(nums)-1):
    if nums[i+1] > nums[i] and nums[i+1] % 2 == 0:
        new_list.append(nums[i+1])
print(new_list)
# Fusion Drill 2 — neighbor counting + condition
nums = [10, 7, 12, 5, 20, 18]
count = 0
for i in range(len(nums)-1):
    if nums[i+1] < nums[i] and nums[i] % 2 == 0:
        count += 1
print(count) #условието не е добре написано, моето решение дава 3 като резултат, изглежда не успях да разбера какво се иска

# Fusion Drill 3 — neighbor search + break
nums = [5, 8, 12, 7, 20]
for i in range(len(nums)-1):
    if nums[i] > 10 and nums[i+1] < nums[i]:
        print(f'{nums[i]} -> {nums[i+1]}')
        break
# Fusion Drill 4 — synchronized traversal + filtering + construction
names = ["Ivan", "Maria", "Peter", "Anna"]
scores = [5, 3, 6, 2]
new_name = []
for i in range(len(names)):
    if scores[i] < 4:
        new_name.append(names[i])
print(new_name)
# Part 4 — Low-Hint Transition Challenges
# Transition Challenge 1
nums = [5, 14, 7, 20, 9, 30]
new_even = []
for num in nums:
    if num % 2 == 0:
        if num > 15:
            new_even.append(num // 2)
        else:
            new_even.append(num)
print(new_even)
# Transition Challenge 2
words = ["cat", "airplane", "bus", "helicopter", "bike"]
for i, word in enumerate(words):
    # if word.startswith('h'):
    if word[1] == "i":
        print(f'{i} -> {word}')
        break
# Transition Challenge 3
nums = [4, 9, 5, 12, 8, 15, 6]
new = []
for i in range(len(nums)-1):
    if nums[i+1] > nums[i] and nums[i+1] % 2 != 0:
        data = nums[i+1] + nums[i]
        new.append(data)
print(new)
# Transition Challenge 4
names = ["Ivan", "Maria", "Peter", "Anna"]
scores = [5, 3, 6, 2]
cities = ["Sofia", "Varna", "Plovdiv", "Burgas"]
new_cities = []
for i in range(len(names)):
    if scores[i] < 4:
        new_cities.append(cities[i])
print(new_cities)