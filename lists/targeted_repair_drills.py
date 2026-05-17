# TARGETED REPAIR DRILLS
# Repair Task 1 — insert() + negative indexes
nums = [10, 20, 30]
nums.insert(-1, 999) #защото -1 е последния елемент, а insert вкарва нов елемент преди въпросния индекс
print(nums)
# Repair Task 2 — insert sequencing
nums = [1, 2, 3]
nums.insert(1, 100)
nums.insert(2, 200)
print(nums)
#първия indesrt вкарва елемент пред числото 2, и така индексите стават 0 за 1, 1 за 100, 2 за 2, след това пред числото 2 вмъкваме 200 и се получава
#[1, 100, 200, 2, 3]
# Repair Task 3 — reverse() vs sorting
nums = [8, 1, 5, 3]
nums.reverse() #просто flip-ва позициите
print(nums)
#[3, 5, 1, 8]
nums = [8, 1, 5, 3]
nums.sort(reverse=True)# тук вече прави descending
print(nums)
#[8, 5, 3, 1]
# Repair Task 4 — append vs extend structure shape
data = [1, 2]
data.append([3, 4]) #nested structure
print(data)
#[1, 2, [3, 4]]
data = [1, 2]
data.extend([3, 4])#flat expansion
print(data)
#[1, 2, 3, 4]
# Repair Task 5 — sequencing awareness
nums = [10, 20, 30, 40]
nums.pop(1)
nums.remove(40)
print(nums)
#след .pop(1) индексите се съкращават от 0, 1, 2, 3 на само 3 индекса 0, 1, 2, елементите след премахната стойност се изтеглят с един индекс напред
#при такива ситуации бих ползвал отрицателен индекс ако искам да работя с поледния елемент, защото ако ползвам положителен той няма да е актуален като ред
# Repair Task 6 — sorted() vs sort()
nums = [30, 10, 20]
new_nums = sorted(nums)
new_nums.append(999)
print(nums)
print(new_nums)
#nums не се променя защото чрез метода sorted() правим копие на nums