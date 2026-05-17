# Stage 6 — List Iteration + Traversal
nums = [10, 20, 30]
for num in nums:
    print(num)
#num представлява елемент от списъка nums, като за всеки num се печата неговата стойност
# Active Coding Drill 1
words = ["red", "green", "blue"]
for word in words:
    print(word)
# Active Coding Drill 2
nums = [5, 10, 15]
for num in nums:
    print(num * 2)
# Active Coding Drill 3 — first accumulation intuition
nums = [10, 20, 30]
total = 0
for num in nums:
    total = total + num
print(total)
# Active Coding Drill 4
nums = [1, 2, 3, 4]
count = 0
for num in nums:
    count = count + 1
print(count)
# Active Coding Drill
nums = [100, 200, 300]
for i in range(len(nums)):
    print(i, nums[i])
# Stage 6 Part 2 - Index Traversal
# TRUE Active Coding Drill — Index Traversal
nums = [100, 200, 300]
for i in range(len(nums)):
    print(f"{i} -> {nums[i]}")
# TRUE Active Coding Drill — Index Processing
nums = [10, 20, 30]
for i in range(len(nums)):
    print(f"Index {i} has value {nums[i]}")
# TRUE Active Coding Drill — Mutation via Index Traversal
nums = [1, 2, 3]
for i in range(len(nums)):#каква е разликата с двата варианта
    print(nums[i] * 10)
for num in nums:#каква е разликата с двата варианта
    print(num * 10)
# TRUE Active Coding Drill — First Real Mutation Loop
prices = [5, 10, 15]
for i in range(len(prices)):
    prices[i] = prices[i] + 100
print(prices)
# Drill 1 — Multiply Mutation
nums = [1, 2, 3, 4]
for i in range(len(nums)):
    nums[i] = nums[i] * 2
print(nums)
# Drill 2 — Subtraction Mutation
temps = [30, 35, 40]
for i in range(len(temps)):
    temps[i] = temps[i] - 5
print(temps)
# Drill 3 — String Mutation
words = ["red", "blue", "green"]
for i in range(len(words)):
    words[i] = words[i] + "!"
print(words)
# Drill 4 — Square Mutation
nums = [2, 3, 4]
for i in range(len(nums)):
    nums[i] = nums[i] ** 2
print(nums)
# Drill 5 — Dynamic Self Mutation
nums = [10, 20, 30]
for i in range(len(nums)):
    nums[i] = nums[i] + i
print(nums)
#имам няколко въпроса, днешната сесия беше 92 минути, 45 от тях бяха за repair на етап 5, останалите за етап 6, с предимно true active coding, през 2026 особенно в ерата не AI някак чак талкова детайлно учене дори на елементарни неща като for i in range(len(nums)):, не е ли малко престараване, в смисъл че ако бяхме 2010 може би щеше да е задължително такива drills, (на мен много ми допада това учене, но си мисля че сигурно е глупаво така бавно да уча...)
