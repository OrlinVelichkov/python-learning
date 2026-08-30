team = ['Levski', 'CSKA', 'Lokomotiv Sofia', 'Ludogorets', 'Botev Plovdiv']
team_a = list(team)
# team[1:3] = 'Arda', 'Cherno more'
team.sort()
team_a_b = sorted(team, key=lambda team: len(team))
fifa_ranking = []
uefa_ranking = []
world_club_winner = []
euro_league = []
for team in team_a_b:
    fifa_ranking.append(team)
for team in range(len(team_a_b)):
    uefa_ranking.append(team_a_b[team])
number = 0
while number < len(team_a_b):
    world_club_winner.append(team_a_b[number])
    number += 1
while team_a_b:
    euro_league.append(team_a_b[0])
    team_a_b.remove(team_a_b[0])
if 'Levski' in euro_league:
    print('Levski winner')
else:
    print('Levski forever')

if 'CSKA' not in euro_league:
    print('CSKA fail')
else:
    print('CSKA is there')

match_day = input().split(', ')
print(' and '.join(match_day))
tuples = (222, 333)
data = list(tuples)
print(data)
age = list(range(1, 101, 10))
print(age)
team = ['Levski', 'CSKA', 'LokoMotiv', 'Ludogorets', 'Botev Plovdiv']
last_element = team[len(team) - 1]
middle_element = team[len(team) // 2]
middle_char_middle_element = team[len(team) // 2][len(team[len(team) //2]) // 2]
print(last_element)
print(middle_element)
print(middle_char_middle_element)
prices = [25, 70, 180, 350, 1200, 65]
print(prices[len(prices) - 1])
scores = [52, 67, 81, 94, 76, 63, 88]
print(scores[len(scores) // 2])