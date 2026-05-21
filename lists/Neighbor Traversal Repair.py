# Part 2 — Neighbor Traversal Repair
# Drill 1 — print pairs
nums = [4, 8, 3, 10]
for i in range(len(nums) - 1):
    print(f'{nums[i]} -> {nums[i+1]}') #определено още ме затруднява този pattetn, два опита и 5 минути мисъл..
# Drill 2 — new list with sums
nums = [10, 20, 5, 15]
new_list = []
for i in range(len(nums)-1):#отновно забравих границата.. видях че пише out of range и добавих -1 ...
    data = nums[i] + nums[i + 1]
    new_list.append(data)
print(new_list)
# Drill 3 — count drops
nums = [9, 7, 8, 4, 10]
count = 0
for i in range(len(nums)-1): # пак... този out of range... винаги се налага дебъг.....
    if nums[i + 1] < nums[i]:
        count +=1
print(count)
# Burst Drill 1 — print bigger pairs
nums = [2, 9, 4, 11, 3]
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        print(f'{nums[i]}, {nums[i+1]}')
# Burst Drill 2 — neighbor differences list
nums = [5, 8, 2, 10]
new_list = []
for i in range(len(nums)-1):
    data = nums[i+1] - nums[i]
    new_list.append(data)
print(new_list)
# Burst Drill 3 — count rises
nums = [1, 3, 2, 5, 4, 8]
count = 0
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        count += 1
print(count)
# Burst Drill 4 — sum only rising neighbors
nums = [2, 7, 5, 9]
total = 0
for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        total += nums[i+1]
print(total)