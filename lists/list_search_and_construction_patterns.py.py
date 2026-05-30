# Building New Lists Dynamically
nums = [5, 12, 7, 20, 30]
new_list = []
for num in nums:
    if num > 10:
        new_list.append(num)
print(new_list)
# Transformation While Building New Lists
# TRUE Active Coding Drill
nums = [1, 2, 3, 4]
new_list = []
for num in nums:
    num *= 2
    new_list.append(num)
print(new_list)
# for i in range(len(nums)):
#     nums[i] *= 2
#     new_list.append(nums[i])
# print(new_list)
#втория вариант променя и оригиналния list
# Conditional Transformation + New List Building
nums = [5, 12, 7, 20]
new_list = []
for num in nums:
    if num > 10:
        num *= 10
        new_list.append(num)
print(new_list)
# TRUE Active Coding Drill — Find First Match
nums = [3, 7, 12, 5, 20]
found = None #зашо ползваме none?
for num in nums:
    if num > 10:
        found = num#тук е един вид презаписване?
        break# ползваме break за да спрем на първото число което е по-голямо от 10 нали?
print(found)
# TRUE Active Coding Drill
nums = [3, 7, 12, 5]
flag = False
for num in nums:
    if num > 10:
        flag = True
        break
print(flag)
# Neighbor Access Pattern
# TRUE Active Coding Drill
nums = [10, 20, 30, 40]
for i in range(len(nums)-1):
    print(f"{nums[i]} --> {nums[i + 1]}")
# Neighbor Drill 1
nums = [10, 15, 25, 40]
for i in range(len(nums)-1):
    print(nums[i + 1] - nums[i])
# Neighbor Drill 2
nums = [5, 8, 6, 10]
for i in range(len(nums)-1):
    if nums[i + 1] > nums[i]:
        print(f"{nums[i]} -> {nums[i + 1]}")
# Neighbor Drill 3
nums = [3, 7, 6, 9, 12, 10]
count = 0
for i in range(len(nums)-1):
    if nums[i + 1] > nums[i]:
        count +=1
print(count)
#това е weak spot макар че се справих, мисля утре да направим repair drill, днешната сесия от 80 мин е към своя край