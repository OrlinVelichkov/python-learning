#Exercise
def engine_ranking(engine):
    return 600 <= engine <= 900
most_powerful_engine_horsepower = [500, 600, 700, 800, 900, 1000]
filtered = list(filter(lambda engine: 600 < engine < 900, most_powerful_engine_horsepower))
filtered2 = list(filter(engine_ranking, most_powerful_engine_horsepower))
print(filtered)
print(filtered2)
for_cleaning = [0, '', 100, 0, '', '', 101, 0]
cleaned = list(filter(None, for_cleaning))
print(cleaned)
olympic_heavyweight_kg = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200]
for_papernews_type = list(map(str,filter(lambda weight: weight > 160, olympic_heavyweight_kg)))
print(for_papernews_type)
marvel_characters = ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow', 'Hawkeye', 'Spider-Man']
my_hero = list(map(str.upper, filter(lambda hero: hero.startswith('I') or hero.startswith('S'), marvel_characters)))
print(my_hero)
my_hero_lower = [hero.lower() if hero.startswith('C') else hero.upper() for hero in marvel_characters if hero.startswith(('I', 'S', 'C'))]
print(my_hero_lower)
# my_hero_lower.reverse()
# my_hero_lower.sort()
my2 = my_hero_lower[::-1]
print(my_hero_lower)
print(my2)
my2[1:2] = ['Superman']
print(my2)
middle_word = my2[len(my2) //2]
left_middle_word = middle_word[:4]
right_middle_word = middle_word[-3:]
new_word = left_middle_word + 'R' + right_middle_word
# my2.insert(1, new_word)
my2[1:1] = [new_word]
my2[2:3] = []
# del my2[0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 1]
numbers[1:-1] = numbers[-2:0:-1]
print(numbers)
extended_list = my2 * 2
print(extended_list)
for i, hero in enumerate(extended_list[1:-1],start=1):
    print(f"{extended_list[i-1]}: {hero}: {extended_list[i+1]}")