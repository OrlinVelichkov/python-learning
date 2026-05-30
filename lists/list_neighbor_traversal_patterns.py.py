# SESSION STRUCTURE (80 min)
# Part 1 — Fast Mixed Warm-up
# Warm-up 1
nums = [2, 11, 4, 15, 6]
for num in nums:
    if num % 2 != 0 and num > 10:
        print(num)
# Warm-up 2
words = ["cat", "elephant", "dog", "tiger"]
for i, word in enumerate(words):
    if len(word) > 4:
        print(f'{i} -> {word}')
# Warm-up 3
nums = [3, 5, 8, 12, 7]
for num in nums:
    if num % 2 == 0:
        print(num)
        break
# Neighbor Consolidation Drill 1
nums = [5, 12, 8, 20, 7]
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        print(f'{nums[i]} -> {nums[i+1]}')
# Neighbor Consolidation Drill 2
nums = [10, 15, 5, 8]
new_list = []
for i in range(len(nums)-1):
    data = nums[i] + nums[i+1]
    new_list.append(data)
print(new_list)
# Neighbor Consolidation Drill 3
nums = [9, 4, 7, 2, 10]
count = 0
for i in range(len(nums)-1):
    if nums[i+1] < nums[i]:
        count += 1
print(count)
# Neighbor Consolidation Drill 4
nums = [3, 8, 6, 12, 5]
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        print(f'{nums[i]} -> {nums[i+1]}')
        break
#мога да кажа че 95% лекота..