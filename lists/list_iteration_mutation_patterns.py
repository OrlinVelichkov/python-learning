# TODAY'S SESSION STRUCTURE (80 min)
# Part 1 — Fast Loop Automation
# Fast Drill 1
nums = [2, 7, 4, 9]
for num in nums:
    if num % 2 != 0:
        num *= 2
        print(num)

for i in range(len(nums)):
    if nums[i] % 2 != 0:
        nums[i] *= 2
        print(nums[i])
#за този pattern кой от двата начина е по правилен, аз направих експеримент с nums[i] и autonomously осъзнавам че nums[i] е стойност в nums
# Fast Drill 2
nums = [10, 20, 30]#Вариант А
new_list = []
for num in nums:
    num -= 5
    new_list.append(num)
print(new_list)

nums = [10, 20, 30]#Вариант Б
new_list = []
for i in range(len(nums)):
    nums[i] -= 5
    new_list.append(nums[i])
print(new_list)
#кой вариант е по правилен - знам че не е нужно да пиша два варианта, но тренирам..
# Fast Drill 3
nums = [3, 6, 9, 12]#Вариант A
count = 0
for num in nums:
    if num % 3 == 0:
        count += 1
print(count)

nums = [3, 6, 9, 12]#Вариант Б
count = 0
for i in range(len(nums)):
    if nums[i] % 3 == 0:
        count +=1
print(count)
#Може би Вариант Б е излишен защото тук на mutate-твам?