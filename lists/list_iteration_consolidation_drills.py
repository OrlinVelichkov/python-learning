# Drill 1 — enumerate + filtering
words = ["cat", "elephant", "dog", "tiger"]
for i, word in enumerate(words):
    if len(word) > 3:
        print(f'{i} -> {word}')
# Drill 2 — flag
nums = [2, 4, 6, 8]
flag = False
for num in nums:
    if num > 10:
        flag = True
print(flag)
# Drill 3 — break
nums = [3, 5, 9, 12, 20]
for num in nums:
    if num > 10:
        print(num)
        break
# Mixed Drill 1 — enumerate + flag
words = ["car", "plane", "bus", "helicopter"]
flag = False
for i, word in enumerate(words):
    if len(word) > 7:
        flag = True
print(f'{i} -> {word}')#тук няма идентация нали?
print(flag)#тук няма идентация нали?
# Mixed Drill 2 — break + neighbor traversal
nums = [3, 7, 12, 10, 5]
for i in range(len(nums)-1):
    if nums[i+1] < nums[i]:
        print(f'{nums[i]} -> {nums[i+1]}')
        break
# Mixed Drill 3 — construction + filtering + enumerate
words = ["red", "banana", "blue", "kiwi"]
new_words = []
for i, word in enumerate(words):
    if len(word) > 4:
        new_words.append(i)
print(new_words)
# for i in range(len(words)): Този вариант също работи, без enumerate, кое е по правилно?
#     if len(words[i]) > 4:
#         new_words.append(i)
# print(new_words)
# Mixed Drill 4 — mutation choice awareness
nums = [2, 5, 8, 1]
new_odd = []
for num in nums: #тук съвсем ясно си казах.. нов list, значи ще ползвам num а не nums[i]...
    if num % 2 != 0:
        num *= 10
        new_odd.append(num)
print(new_odd)
# Drill 1 — indentation
words = ["car", "helicopter", "bus", "airplane"]
flag = False
for i in range(len(words)): 
    if len(words[i]) > 5:
        flag = True
        print(words[i])
print(flag)
#можех и с word in words.. просто така реших да я направя задачата 
# Drill 2 — boundary reflex
nums = [4, 9, 6, 12]
for i in range(len(nums)-1):
    print(f'{nums[i]} -> {nums[i+1]}')
# nums = [10, 7, 8, 3]
# Drill 3 — combined
nums = [10, 7, 8, 3]
for i in range(len(nums)-1):
    if nums[i+1] < nums[i]:
        print(f'{nums[i]} -> {nums[i+1]}')
        break