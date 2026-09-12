#За преговор:
#any and all
#filter
#map
#previous/now/next with enumerate and range
#traversal with while loop
#slice notation
#.copy and [:] mutation

#nested list exercise for any and all functions
nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = any(any(num == 6 for num in num_group) for num_group in nested_lists)
print(result)
string_nested_list = [["apple", "banana", "kiwi"], ["cherry", "date", "kiwi"], ["kiwi", "fig", "grape"]]
result2 = all(any(len(fruit) == 4 for fruit in basket) for basket in string_nested_list)
print(result2)

#give me an exercise for filter and map functions
#Exercise for filter and map functions:
def even(num):
    return num % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(map(str, filter(even, numbers)))

print(even_list)

cartoon_characters = ["Mickey Mouse", "Donald Duck", "Bugs Bunny", "SpongeBob SquarePants", "Tom and Jerry"]
for i in range(1, len(cartoon_characters)-1):
    print(cartoon_characters[i-1], cartoon_characters[i], cartoon_characters[i+1])
for i, hero in enumerate(cartoon_characters[1:-1],start=1):
    print(f"{cartoon_characters[i-1]} - {hero} - {cartoon_characters[i+1]}")


name_of_seven_dwarfs = ["Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"]
for name in name_of_seven_dwarfs:
    print(name)
while name_of_seven_dwarfs:
    current_dwarf = name_of_seven_dwarfs[0]
    print(current_dwarf)
    name_of_seven_dwarfs.remove(current_dwarf)
i = 0
while i < len(name_of_seven_dwarfs):
    print(name_of_seven_dwarfs[i])
    i += 1

characters_from_voltron = ["Lance", "Keith", "Pidge", "Hunk", "Shiro", "Allura", "Coran"]
copy_lst = characters_from_voltron[:]
copy_lst[1:2] = 'Orlin',
print(characters_from_voltron)
print(copy_lst)
new_copy = copy_lst.copy()
# new_copy[:] = ['Voltron']
robot = 'Voltron'
robot = robot[::-1]
print(robot)

characters_from_101_dalmatians = ["Pongo", "Perdita", "Lucky", "Rolly", "Patch", "Penny", "Freckles"]
characters_from_smallvile = ["Lex Luthor", "Lena Luthor", "Brainiac", "General Zod", "Doomsday"]
new_characters = list(filter(lambda name: len(name.split()) > 1 and name.split()[1].startswith('Z'), characters_from_smallvile))
print(new_characters)
new_characters2 = [name for name in characters_from_smallvile if len(name.split()) > 1 and name.split()[1].startswith('Z')]
print(new_characters2)