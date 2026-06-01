# Final Integration Drill
# Part A — Read & Predict
# Без да пускаш кода.
# Кажи какъв ще бъде резултатът.
# Task 1
nums = [10, 20, 30, 40, 50, 60]
nums[1:5]
# Output [20, 30, 40, 50 ]
# Task 2
nums = [10, 20, 30, 40, 50, 60]
nums[:4]
# Output[10, 20, 30, 40]
# Task 3
nums = [10, 20, 30, 40, 50, 60]
nums[::2]
# Output[10, 30, 50]
# Task 4
nums = [10, 20, 30, 40, 50, 60]
nums[-3:]
# Output[40, 50, 60]
# Task 5
nums = [10, 20, 30, 40, 50, 60]
nums[::-2]
# Output[60, 40, 20]

# Part B — Build The Slice
# Task 6
nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])#main method споре мен
print(nums[-5:-2])
print(nums[1:-2])
#Кой е pythonic метода и защо?
# Task 7
nums = [10, 20, 30, 40, 50, 60]
print(nums[:-2])
# Task 8
nums = [10, 20, 30, 40, 50, 60]
print(nums[-2:])
# Task 9
nums = [10, 20, 30, 40, 50, 60]
print(nums[::-1])
copy = nums[:]
copy.reverse()
print(f'Знам че не е искан този метод: {copy}')
# Task 10
nums = [10, 20, 30, 40, 50, 60]
print(nums[1::2])

# Part C — Mixed Challenge
# Task 11
letters = ["A", "B", "C", "D", "E", "F"]
letters[-5:-1:2]
#Output["B", "D"]

# Task 12
letters = ["A", "B", "C", "D", "E", "F"]
letters[::-3]
#Output["F", "C"]