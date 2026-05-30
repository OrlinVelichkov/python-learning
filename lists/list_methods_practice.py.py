# Task 1 — append()
data = [1, 2]
data.append(3)
data.append(4)
print(data)
# Task 2 — extend()
data = [10]
data.extend([20, 30, 40])
print(data)
# Task 3 — insert()
nums = [1, 3, 4]
nums.insert(1, 2)
nums.insert(4, 5)#тук опитах да (-1, 5) мислех че мога да вмъкне преди последния елемент който е -1 но не се получи
print(nums)
# Task 4 — remove()
letters = ["a", "b", "c", "b"]
letters.remove("b")
print(letters)
# Task 5 — pop()
nums = [10, 20, 30, 40]
store10 = nums.pop(0)
store40 = nums.pop(-1)
print(store10)
print(store40)
print(nums)
# Task 6 — clear()
data = [1, 2, 3]
data.clear()
print(data)
# Task 7 — index()
animals = ["cat", "dog", "bird"]
print(f"Индекса на dog е: {animals.index("dog")}")
# Task 8 — count()
nums = [1, 2, 2, 3, 2]
print(nums.count(2))
# Task 9 — sort()
nums = [30, 10, 20]
nums.sort()
print(nums)
# Task 10 — reverse()
nums = [1, 2, 3, 4]
nums.reverse()
print(nums)
# Task 11 — sorted()
nums = [50, 10, 30]
new = sorted(nums)
# new = sorted(nums, reverse=True)
print(nums)
print(new)