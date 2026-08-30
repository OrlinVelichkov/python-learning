world_cup_team = ['Brazil', 'Germany', 'Argentina', 'France', 'Spain', 'Italy', 'Netherlands', 'Belgium', 'Portugal', 'England']
best_player_in_every_team = ['Neymar', 'Müller', 'Messi', 'Griezmann', 'Iniesta', 'Buffon', 'Robben', 'De Bruyne', 'Ronaldo', 'Harrison']
world_cup_team.extend(best_player_in_every_team)
coach = ['Luiz Felipe Scolari', 'Joachim Löw', 'Lionel Scaloni', 'Didier Deschamps', 'Luis Enrique', 'Roberto Mancini', 'Frank de Boer', 'Roberto Martínez', 'Fernando Santos', 'Gareth Southgate']
world_cup_team.append(coach[len(coach) - 1][len(coach[len(coach) - 1]) - 12])
last_coach = coach[len(coach) - 1]
surename = last_coach.split()[1]
print(surename[len(surename) // 2])
top_teams = world_cup_team[:]
top_teams.insert(3, world_cup_team[0])
position_of_team = top_teams.index(top_teams[len(top_teams)//2])
count = top_teams.count(top_teams[len(top_teams)//2])
print(count)
print(position_of_team)
top_teams.remove('Argentina')
print(top_teams)
poped_team = world_cup_team.pop(3)
print(world_cup_team)
print(poped_team)
top_teams.clear()
print(top_teams)
top_teams.reverse()
print(top_teams)
queue = ["Ivan", "Maria", "Georgi", "Elena"]
first_person = queue.pop(0)
print(first_person)
print(queue)
inventory = ["Keyboard", "Mouse", "Monitor"]
inventory.append('Laptop')
inventory.extend(['Webcam', 'Headphones'])
inventory.insert(1, 'USB hub')
position = inventory.index('Monitor')
inventory.remove('Mouse')
last_element = inventory.pop()
print(inventory.count('Keyboard'))
print(last_element)
print(position)
print(inventory)