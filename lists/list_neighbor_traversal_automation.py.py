# Stage 6 — Repair + Automation Session
# Warm-up Drill 1
nums = [2, 5, 8, 1]
for num in nums:
    if num >= 5:
        num *= 10
        print(num)
# Warm-up Drill 2
nums = [3, 6, 9]
new_list = []
for num in nums:
    num += 1
    new_list.append(num)
print(new_list)
# Warm-up Drill 3
nums = [1, 4, 7, 2, 9]
count = 0
for num in nums:
    if num % 2 != 0:
        count += 1
print(count)
# Neighbor Repair Drill 1
nums = [4, 9, 3, 8]
for i in range(len(nums)-1):
    if nums[i+1] < nums[i]:
        print(nums[i+1])
# Neighbor Repair Drill 2
nums = [10, 15, 13, 20]
new_list = []
for i in range(len(nums)-1):
    data = nums[i + 1] - nums[i]
    new_list.append(data)
print(new_list)
#тук ми отне няколко опита дакато се получи, основно бъркам boundary
# Neighbor Repair Drill 3
nums = [5, 8, 12, 10, 15]
count = 0
for i in range(len(nums)-1):
    if nums[i + 1] > nums[i]:
        count += 1
print(count)
#отновно забравям за boundary
# Micro Drill 1
nums = [2, 5, 1, 7]
for i in range(len(nums)-1):
    if nums[i + 1] > nums[i]:
        print(f'{nums[i + 1]} --> {nums[i]}')
# Micro Drill 2
nums = [10, 20, 15, 25]
for i in range(len(nums)-1):
    data = nums[i] + nums[i + 1]
    print(data)#30, 35, 40
# Micro Drill 3
nums = [3, 8, 6, 9]
new_list = []
for i in range(len(nums)-1):
    data = abs(nums[i] - nums[i + 1])
    new_list.append(data)
print(new_list)
# Repair Drill 1 — neighbor + new list
nums = [4, 10, 7, 12]
new_list = []
for i in range(len(nums)-1):
    data = nums[i + 1] - nums[i]
    new_list.append(data)
print(new_list)
# Repair Drill 2 — neighbor + print pair
nums = [3, 9, 5, 11]
for i in range(len(nums)-1):
    if nums[i + 1] > nums[i]:
        print(f'{nums[i]} -> {nums[i + 1]}')
# Repair Drill 3 — neighbor + count
nums = [10, 8, 12, 7, 9]
count = 0
for i in range(len(nums)-1):
    if nums[i + 1] < nums[i]:
        count += 1
print(count)