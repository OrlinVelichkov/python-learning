# # Part 3 — Combined Mini Problems
# Mini Problem 1 — enumerate + construction + filtering
words = ["car", "airplane", "bus", "helicopter", "bike"]
new_list = []
# for i in range(len(words)): #Вариант без enumerate()
#     if len(words[i]) > 5:
#         new_list.append(i)
for i, word in enumerate(words):
    if len(word) > 5:
        new_list.append(i)
print(new_list)
# Mini Problem 2 — flag + break + search
nums = [3, 5, 9, 14, 18]
flag = False
for num in nums:
    if num % 2 == 0:
        flag = True
        print(num)
        break
print(flag)
# Mini Problem 3 — neighbor + construction + condition
nums = [4, 9, 5, 12, 3]
next_value = []
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        next_value.append(nums[i+1])
print(next_value)
# Mini Problem 4 — synchronized traversal + flag
names = ["Ivan", "Maria", "Peter"]
scores = [5, 3, 6]
flag = False
for i in range(len(names)):
    if scores[i] < 4:
        flag = True
        print(f'{names[i]} -> {scores[i]}')
print(flag)
# Part 4 — Low-Hint Challenges
# Low-Hint Challenge 1
nums = [5, 12, 7, 20, 3]
new_list = []
for num in nums:
    if num % 2 == 0:
        num *= 10
        new_list.append(num)
print(new_list)
# Low-Hint Challenge 2
nums = [3, 8, 5, 11, 6]
for num in nums:
    if num %2 != 0 and num > 10:
        print(num)
        break
# Low-Hint Challenge 3
nums = [4, 9, 5, 12, 8]
new_list = []
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        plus = nums[i+1] + nums[i]
        new_list.append(plus)
print(new_list)
# Low-Hint Challenge 4
names = ["Ivan", "Maria", "Peter", "Anna"]
scores = [5, 3, 6, 2]
flag = False
for i in range(len(names)):
    if scores[i] < 4:
        flag = True
        print(f'{names[i]} -> {scores[i]}')
print(flag)
# Mini Pipeline Problem 1
nums = [5, 12, 7, 20, 9, 30]
even = []
for num in nums:
    if num % 2 == 0:
        if num > 15:
            num *= 2
            even.append(num)
        else:
            even.append(num)
print(even)
# Mini Pipeline Problem 2
words = ["cat", "airplane", "bus", "helicopter", "bike"]
for i, word in enumerate(words):
    if len(word) > 7:
        print(f'{i} -> {word}')
        break
# Mini Pipeline Problem 3
nums = [4, 9, 5, 12, 8, 15]
new_list = []
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        data = nums[i+1] + nums[i]
        new_list.append(data)
print(new_list)
# Mini Pipeline Problem 4
names = ["Ivan", "Maria", "Peter", "Anna"]
scores = [5, 3, 6, 2]
cities = ["Sofia", "Varna", "Plovdiv", "Burgas"]
for i in range(len(names)):
    if scores[i] < 4:
        print(f'{names[i]} -> {scores[i]} -> {cities[i]}')
# Compression Drill 1
nums = [2, 11, 4, 15, 8]
odd = []
for num in nums:
    if num %2 != 0:
        odd.append(num * 100)
print(odd)
# Compression Drill 2
nums = [5, 9, 3, 12, 7]
for num in nums:
    if num % 2 == 0:
        print(num)
        break
# Compression Drill 3
nums = [4, 10, 6, 15, 9]
count = 0
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        count += 1
print(count)
# Compression Drill 4
words = ["cat", "airplane", "bus", "helicopter"]
for i, word in enumerate(words):
    if len(word) > 7:
        print(f'{i} -> {word}')
# Compression Drill 5
names = ["Ivan", "Maria", "Peter"]
scores = [5, 2, 6]
flag = False
for i in range(len(names)):
    if scores[i] < 3:
        flag = True
        print(f'{names[i]} -> {scores[i]}')
print(flag)