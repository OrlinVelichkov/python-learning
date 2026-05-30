# Stage 6 Consolidation Layer
# Part 1 — enumerate() Automation
# Enumerate Drill 1
words = ["apple", "banana", "kiwi"]
for i, fruit in enumerate(words):
    print(f"{i} - > {fruit}")

# Enumerate Drill 2
nums = [10, 20, 30]
for i, num in enumerate(nums):
    if num > 15:
        print(i)
# Part 2 — Flag Automation
# Flag Drill 1

nums = [2, 4, 6, 8]
Flag = False
for num in nums:
    if num % 2 != 0:
        Flag = True
print(Flag)

# Flag Drill 2
words = ["cat", "dog", "elephant"]
Flag = False
for word in words:
    if len(word) > 5:
        Flag = True
print(Flag)
# Part 3 — break Automation
# Break Drill 1
nums = [1, 3, 7, 10, 12]
for num in nums:
    if num % 2 == 0:
        break # защо break е над print,същия резултат има и ако е след print
print(num)
# Break Drill 2
nums = [5, 9, 11, 20, 30]
for num in nums:
    if num > 10:
        print(num)
        break