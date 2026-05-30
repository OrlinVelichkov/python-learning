# List Methods Foundations
#Задача 1
nums = [10, 20, 30]
nums.append(40) 
nums.extend([50, 60])
nums.insert(1, 15)
print(nums)

#Задача 2
nums = [1, 2]
nums.append(3)
nums.extend([4, 5])
nums.insert(2, 999)
nums.append([7, 8])
nums.extend([9])
print(nums)

# Task 1
data = [10, 20, 30]
data.insert(0, 5)
data.insert(2, 15)
data.insert(4, 25)
data.append(35)
print(data)
# Active Coding Drill 2
nums = [1, 2, 3]
nums.insert(0, 0)
nums.insert(3, 100)
nums.insert(4, 200)
nums.append([4, 5])
print(nums)
# Removing + Extraction Methods
# Active Coding Drill 1
nums = [10, 20, 30, 40, 50]
nums.remove(10)
nums_pop = nums.pop()
print(nums)
print(nums_pop)
# Active Coding Drill 2
data = ["a", "b", "c", "d", "e"]
new_data = []
extraxt_value1 = data.pop()
extraxt_value2 = data.pop(-2)#Въпрос, с отрицателен индекс ли е добре да работи с pop() или с положителен?
extraxt_value3 = data.pop(0)
new_data.append(extraxt_value1)
new_data.append(extraxt_value2)
new_data.append(extraxt_value3)
print(data)
print(new_data)
print(extraxt_value1)
print(extraxt_value2)
print(extraxt_value3)
#data.remove("a")#никъде не стана ясно защо да ползвам remove() при положение че се иска да покажа extraxt value, но ползвах все пак и remove()
# Active Coding Drill 3
items = ["pen", "book", "pen", "bag", "pen", "phone"]
bag = items.index("bag")
pen = items.count("pen")
items.clear()
print(f"{bag} и {pen}")
print(items)
# Active Coding Drill 4
nums = [40, 10, 30, 20]
nums.sort(reverse=True)
# nums.reverse()
print(nums)
#Задача 1 Repair
nums = [100, 5, 999, 1]
nums.sort(reverse=True)
print(nums)
#Задача 2 Repair
nums = [7, 100, 3, 50]
nums.sort()
nums.reverse()
nums.sort(reverse=True)
print(nums)
# Active Coding Drill 5
nums = [30, 10, 20]
result = sorted(nums)
print(nums)
print(result)
# Active Coding Drill 6
nums = [3, 1, 2]
result = sorted(nums)
result.append(999)
print(nums)
print(result)