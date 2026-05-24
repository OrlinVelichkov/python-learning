# Part 1 — Fast Warm-up
a = [1, 2]
b = [3, 4]
c = a + b
print(c)
# Warm-up 2
nums = [0]
new = nums * 4
print(new)
# Warm-up 3
foods = ["pizza", "burger", "salad"]
print("burger" in foods)
# Warm-up 4
colors = ["red", "blue", "green"]
print(len(colors) > 2)
#не съм сигурен как искаше условието да направя проверката..
# Part 2 — Core List Operations Drills
# Drill 1 — + + len()
a = [1, 2, 3]
b = [4, 5]
c = a + b
print(len(c))
# Drill 2 — * + membership
colors = ["red", "blue"]
repeated_list = colors * 3
count = 0
# if "blue" in repeated_list:
for color in repeated_list:
    if color == "blue":
        count += 1
        print("blue" in repeated_list)
        print(count)
#тук излязох от рамките на условието на задачата..искам да експериментирам..обаче не разбирам защо не мога да преброи 3 пъти "blue" с # if "blue" in repeated_list по този начин?
# Drill 3 — concatenation + membership
nums1 = [10, 20]
nums2 = [30, 40]
total = nums1 + nums2
print(50 not in total)
# Drill 4 — len() as collection property
items = ["phone", "tablet", "laptop", "mouse"]
print(len(items) >= 4)
# Part 3 — List Operations + Processing Fusion
# Fusion Drill 1 — + + construction
a = [1, 2]
b = [3, 4]
c = a + b
new_abc = []
for num in c:
    if num % 2 == 0:
        new_abc.append(num)
print(new_abc)
# Fusion Drill 2 — * + traversal
words = ["hi"]
repeated = words * 5
for word in repeated:
    print(word)
# Fusion Drill 3 — membership + filtering
nums = [5, 10, 15, 20]
if 15 in nums:
    print('Found')
else:
    print("Not Found")
# Fusion Drill 4 — len() + logic
items = ["pen", "book", "phone"]
if len(items) < 5:
    print("Small list")
else:
    print("Large list")
# Part 4 — Low-Hint List Operations Challenges
# Challenge 1 — + + filtering + construction
a = [5, 10]
b = [15, 20]
combined_list = a + b
new_list = []
for num in combined_list:
    if num > 10:
        new_list.append(num)
print(new_list)
# Challenge 2 — * + membership
words = ["go"]
repeated = words * 4
print("go" in repeated)
# Challenge 3 — len() + logic + construction
items = ["pen", "book", "phone", "mouse"]
new_list = []
if len(items) >= 4:
    new_list.extend(items * 2) #не се получи с append()
print(new_list)
# Challenge 4 — membership + traversal
nums = [5, 10, 15, 20]
if 15 in nums:
    for num in nums:
        if num > 10:
            print(num)
else:
    print('Числото 15 не същестува')

# Workflow Fusion Challenge 1
a = [5, 10]
b = [15, 20]
new_list1 = []
combined = a + b
if len(combined) > 3:
    for num in combined:
        if num % 5 == 0:
            new_list1.append(num)
print(new_list1) 
# Workflow Fusion Challenge 2
words = ["go", "run"]
repeated = words * 3
if "run" in repeated:
    for word in repeated: 
        if len(word) > 2:
            print(word)
else:
    print("Run is not in repeated")

# Workflow Fusion Challenge 3
nums = [10, 15, 20]
repeated = nums * 2
new_list = []
for num in repeated:
    if num > 10:
        new_list.append(num)#как се създава нов списък директно в if блока, без да декларирам празен списък в началото?
print(new_list)
# Workflow Fusion Challenge 4
items = ["phone", "tablet"]
combined = items + ["laptop", "mouse"]
if len(combined) >= 4:
    print("tablet" in combined)