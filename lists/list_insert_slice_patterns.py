# Insert Slice
# Task 1
nums = [10, 20, 30, 40]
nums[2:2] = [999]
print(nums)
# Task 2
nums = [10, 20, 30, 40]
nums[0:0] = [100]
print(nums)
# Task 3
letters = ["A", "B", "C", "D"]
letters[2:2] = ['X']
print(letters)
# Task 4
names = ["Ivan", "Maria", "Petar"]
# names[len(names):len(names)] = ['Stefan']
names[4:4] = ['Stefan']
print(names)
# Task 5
nums = [1, 2, 5, 6]
nums[2:2] = [3, 4]
# nums.reverse()#просто правя малки експерименти, знам че не е от заданието..
print(nums[::-1])#просто правя малки експерименти, знам че не е от заданието..
# Bonus
nums = [10, 20, 30]
nums[1:1] = [100, 200]
#Output[10, 100, 200, 20, 30]

# Integrated Mutation
# Part A — Classify + Predict
# Task 1
nums = [10, 20, 30, 40, 50]
nums[1:3] = [999]
#Replace 
#Output[10, 999, 40, 50]
# Task 2
nums = [10, 20, 30, 40, 50]
nums[2:5] = []
#Delete
#Output[10, 20]
# Task 3
nums = [10, 20, 30, 40]
nums[2:2] = [111]
#Insert
#Output[10, 20, 111, 30, 40]
# Task 4
letters = ["A", "B", "C", "D"]
letters[1:3] = ["X"]
#Replace
#Output["A", "X", "D"]
# Task 5
names = ["Ivan", "Maria", "Petar"]
names[0:0] = ["Stefan"]
#Insert
#Output["Stefan", "Ivan", "Maria", "Petar"]
# Part B — Build The Mutation
# Task 6
mutation = [10, 20, 30, 40, 50]
mutation[1:3] = [100, 200]
print(mutation)
# Task 7
mutation2 = [10, 20, 30, 40, 50]
mutation2[2:] = []
print(mutation2)
# Task 8
mutation3 = ["A", "B", "D"]
mutation3[2:2] = ['C']
print(mutation3)
# Task 9
names = ["Ivan", "Maria", "Petar"]
names[1:2] = ['Stefan']
print(names)
# Task 10
numbers = [1, 2, 5, 6]
numbers[2:2] = [3, 4]
print(numbers)
# Part C — Workflow Tracking
# Task 11
nums = [10, 20, 30, 40]
nums[1:1] = [100]
nums[3:4] = []
#Output[10, 100, 20, 30, 40] step 1
#Output[10, 100, 20, 40] step 2

# Task 12
letters = ["A", "B", "C", "D"]
letters[1:3] = ["X", "Y"]
letters[0:0] = ["START"]
#Output["A", "X", "Y", "D"]
#Output["START", "A", "X", "Y", "D"]

# Repair Drill
# Task 1
nums = [10, 20, 30]
nums[1:1] = [999]
# 0 -> 10
# 1 -> 999
# 2 -> 20
# 3 -> 30

# Task 2
nums = [10, 20, 30]
nums[0:0] = [111]
# 0 -> 111
# 1 -> 10
# 2 -> 20
# 3 -> 30

# Task 3
nums = [10, 20, 30, 40]
nums[2:3] = []
# 0 -> 10
# 1 -> 20
# 2 -> 40

# Active Tracking Drill
nums = [1, 2, 3, 4]
nums[1:1] = [100]
nums[3:4] = []
#[1, 100, 2, 3, 4]
#[1, 100, 2, 4]

# Task 5
nums = [10, 20, 30, 40]
nums[2:2] = [999]
nums[1:2] = []
#[10, 20, 999, 30, 40]
#[10, 999, 30, 40]

# Mini Drill
# Task 1
nums = [10, 20, 30]
nums[len(nums):len(nums)] = [40]
#[10, 20, 30, 40]

# Task 2
letters = ["A", "B", "C"]
letters[len(letters):len(letters)] = ["D", "E"]
#["A", "B", "C", "D", "E"]
# Task 3
names = ["Ivan", "Maria"]
names[len(names):len(names)] = ["Petar"]
#["Ivan", "Maria", "Petar"]
# Task 4
nums = [10, 20, 30]
nums[len(nums):len(nums)] = [40, 50]

# Task 5
nums[len(nums):len(nums)] = [999]
nums.append(999)
#и двете ми харесват