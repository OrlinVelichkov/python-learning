most_beautiful_waterfall = ["Niagara Falls", "Victoria Falls", "Angel Falls", "Iguazu Falls", "Yosemite Falls", "Plitvice Lakes Waterfall"]
rating = [9.5, 9.8, 9.7, 9.6, 9.4, 9.3]
print(f'My favorite waterfalls:')
for i, (waterfall, rating) in enumerate(zip(most_beautiful_waterfall, rating), start=1):
    print(f'№{i}. {waterfall} - Rating: {rating}')

print(f'My favorite waterfalls:')
for i in range(len(most_beautiful_waterfall)):
    print(f'№{i + 1}. {most_beautiful_waterfall[i]} - {rating[i]}')

most_beautiful_waterfall[len(most_beautiful_waterfall) - 1] = 'Крушунските водопади'
del rating[-1]
print(most_beautiful_waterfall)
print(rating)

marvel_heroes = ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow', 'Hawkeye']
for i in range(1, len(marvel_heroes) - 1):
    print(marvel_heroes[i - 1], marvel_heroes[i], marvel_heroes[i + 1])

for i, hero in enumerate(marvel_heroes):
    if 0 < i < len(marvel_heroes) - 1:
        print(marvel_heroes[i-1], hero, marvel_heroes[i+1])
for i, hero in enumerate(marvel_heroes[1:-1], start=1):
    print(marvel_heroes[i - 1], hero, marvel_heroes[i + 1])