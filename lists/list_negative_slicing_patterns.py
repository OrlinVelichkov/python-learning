# Lesson 4 — Negative Slicing

# Task 1
nums = [10, 20, 30, 40, 50, 60]
print(nums[-3:])
# Task 2
nums = [10, 20, 30, 40, 50, 60]
print(nums[:-2])
# Task 3
nums = [10, 20, 30, 40, 50, 60]
print(nums[-4:-1])
# Task 4
names = ["Ivan", "Maria", "Petar", "Georgi", "Stefan", "Nikolay"]
print(names[-3:])
# Task 5
names = ["Ivan", "Maria", "Petar", "Georgi", "Stefan", "Nikolay"]
print(names[-6:-2]) #или алтернативно names[:-2]
# Бонус въпрос
nums = [10, 20, 30, 40, 50, 60]
nums[-4:-1]
# output [30, 40, 50]
#############################
# Negative Step Slicing
# Task 1
nums = [10, 20, 30, 40, 50, 60]
print(nums[::-2])
# Task 2
letters = ["A", "B", "C", "D", "E", "F"]
print(letters[::-2])
# Task 3
names = ["Ivan", "Maria", "Petar", "Georgi", "Stefan", "Nikolay"]
print(names[::-2])
# Task 4 - > за тези два начина се сетих, опитах и трети но не се получи, друг вариант ли очакваше от мен освен [::-1]
nums = [10, 20, 30, 40, 50, 60]
print(nums[::-1])
reversed_ = sorted(nums, reverse=True)
print(reversed_)
copy = nums[:]
copy.reverse() #припомни ми кога се ползва reverse и кога referse=True
print(copy)
# Task 5
letters = ["A", "B", "C", "D", "E", "F"]
print(letters[-2::-2])
# Bonus
nums = [10, 20, 30, 40, 50, 60]
nums[-2::-2]
# output[50, 30, 10]