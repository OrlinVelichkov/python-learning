fifa_ballon_dor_winners = ['Lionel Messi', 'Cristiano Ronaldo', 'Luka Modric', 'Kaka', 'Ronaldinho', 'Zinedine Zidane', 'Ronaldo Nazario', 'George Weah', 'Johan Cruyff', 'Michel Platini']
for i in range(len(fifa_ballon_dor_winners)):
    fifa_ballon_dor_winners[i] = 'Mr. ' + fifa_ballon_dor_winners[i]
print(fifa_ballon_dor_winners)
print(f'Best player {i + 1} - {fifa_ballon_dor_winners[i]}')
print('Dream team of the best players in the world:')
for i, player in enumerate(fifa_ballon_dor_winners):
    fifa_ballon_dor_winners[i] = 'Mr. ' + player
    print(i + 1, fifa_ballon_dor_winners[i])
for i in range(1, len(fifa_ballon_dor_winners)-1):
    print(fifa_ballon_dor_winners[i-1], fifa_ballon_dor_winners[i], fifa_ballon_dor_winners[i+1])

champion_league_winners = ['Real Madrid', 'AC Milan', 'Liverpool', 'Bayern Munich', 'Barcelona', 'Ajax', 'Manchester United', 'Juventus', 'Inter Milan', 'Chelsea']
year = [2002, 2003, 2005, 2007, 2009, 2010, 2011, 2013, 2014, 2015]

for i in range(len(champion_league_winners)):
    print(f'{champion_league_winners[i]} - {year[i]}')
for team, year in zip(champion_league_winners, year):
    print(f'{team} - {year}')
for i, (team, year) in enumerate(zip(champion_league_winners, year),start=1):
    print(f'{i}. {team} - {year}')
Mission 1 — Value Traversal
products = ["Keyboard", "Mouse", "Monitor", "Laptop"]
for item in products:
    print(item)
Mission 2 — Index Traversal
cities = ["Sofia", "Plovdiv", "Varna", "Burgas"]
for i in range(len(cities)):
    print(i, cities[i])
Mission 3 — enumerate()
players = ["Ivan", "Maria", "Georgi", "Elena"]
for i, player in enumerate(players,start=1):
    print(i, player)
Mission 4 — Mutation Through Index
numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)
Mission 5 — Neighbor Traversal
temperatures = [18, 21, 19, 25, 23]
for i in range(1, len(temperatures) - 1):
    print(temperatures[i-1], temperatures[i], temperatures[i+1])
Mission 6 — Compare Neighbors
temperatures = [18, 21, 19, 25, 23]
for i in range(len(temperatures) - 1):
    if temperatures[i+1] > temperatures[i]:
        print(temperatures[i], temperatures[i+1])
Mission 7 — Parallel Traversal
products = ["Keyboard", "Mouse", "Monitor", "Laptop"]
prices = [70, 25, 350, 1200]

for i, (item, price) in enumerate(zip(products, prices), start=1):
    print(i, item, price)

# Mission 8 — Stage 6 Mini Checkpoint
names = ["Ivan", "Maria", "Georgi", "Elena"]
scores = [72, 91, 64, 88]

for i, name in enumerate(names, start=1):
    print(f'{i}. {name}')
for name, score in zip(names, scores):
    print(f'{name} - {score}')
for i in range(len(scores)):
    scores[i] += 5
print(scores)

a = [1, 3, 5, 7, 9]
b = list(range(1, 10, 2))
c = [2 * i - 1 for i in range(1, 6)]

print(a)
print(b)
print(c)