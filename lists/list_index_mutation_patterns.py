# Warm-up Drill — Re-enter the Flow
nums = [5, 10, 15, 20]
for num in nums:
    if num > 10:
        print(num)
# TRUE Active Coding Drill 2 — Selective Accumulation
nums = [5, 12, 7, 20]
total = 0
for num in nums:
    if num > 10:
        total += num
print(total)#идентацията тук къде трябва да е? Подравнена с for ли?
# TRUE Active Coding Drill 3
nums = [5, 12, 7, 20]
for i in range(len(nums)):
    if nums[i] > 10:
        nums[i] += 100
print(nums)
#Отбележи го като weak място, в някой момент ще поискам да го упражним
# TRUE Active Coding Drill 4
nums = [5, 12, 7, 20, 30]
count = 0
for num in nums:
    if num > 10:
        count += 1
print(count)
# TRUE Active Coding Drill — i Pattern Reinforcement 1
nums = [2, 4, 6, 8]
for i in range(len(nums)):
    if nums[i] >= 6:
        nums[i] += 50
print(nums)
# TRUE Active Coding Drill — i Pattern Reinforcement 2
words = ["cat", "dog", "bird"]
for i in range(len(words)):
    if len(words[i]) > 3:
        words[i] += "!"
print(words)
# TRUE Active Coding Drill — i Pattern Reinforcement 3
nums = [10, 15, 20]
for i in range(len(nums)):
    nums[i] -= i
print(nums)