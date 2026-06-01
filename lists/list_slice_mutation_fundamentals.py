# Slicing Mutation
# Task 1
nums = [10, 20, 30, 40, 50]
nums[1:3] = [100, 200]
print(nums)
# Task 2
nums = [10, 20, 30, 40, 50]
nums[2:4] = [999]
print(nums)
# Task 3
letters = ["A", "B", "C", "D", "E"]
letters[1:3] = ["X", "Y"]
print(letters)
# Task 4
names = ["Ivan", "Maria", "Petar", "Georgi"]
names[1:3] = ['Stefan']
print(names)
# Task 5
nums = [1, 2, 3, 4, 5, 6]
nums[2:5] = [100, 200]
nums[0:0] = [1000]
print(nums)

# Delete Slice
# Task 1
nums = [10, 20, 30, 40, 50]
nums[1:3] = []
print(nums)
# Task 2
nums = [10, 20, 30, 40, 50]
nums[:2] = []
print(nums)
# Task 3
letters = ["A", "B", "C", "D", "E"]
letters[2:4] = []
print(letters)
# Task 4
names = ["Ivan", "Maria", "Petar", "Georgi", "Stefan"]
names[1:3] = []
print(names)
# Task 5
nums = [1, 2, 3, 4, 5, 6]
nums[-3:] = []#прецених че е по-добре да ползвам negative slicing тук, какво мислиш?
print(nums)
# Бонус въпрос
nums = [10, 20, 30, 40, 50]
nums[1:4] = []
#Output[10, 50]