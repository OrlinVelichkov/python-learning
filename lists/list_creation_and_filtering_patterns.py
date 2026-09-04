team_a = ['Tom', 'Jerry']
team_b = ['Donald', "Bugs Bunny"]

team_c = team_a + team_b
print(team_c)
for i, (team_a_member, team_b_member) in enumerate(zip(team_a, team_b), start=1):
    print(f"Match {i}: {team_a_member} vs {team_b_member}")

winner = team_a.copy()
team_a[0] = 'Spike'
print("Winner team:", winner)
print("Updated team A:", ' and '.join(team_a))
#exercise for list creation with split()
data = "Tom,Jerry,Donald,Bugs Bunny"
team_d = data.split(",")
team_d = [member.strip() for member in team_d]  # Remove any leading/trailing whitespace
print("Team D:", ' and '.join(team_d))
upper_team_d = list(map(str.upper, team_d))
print(upper_team_d)

looney_tunes = ['Bugs Bunny', '888', 'Daffy Duck', 'Porky Pig', 'Elmer Fudd', 'Tweety', 'Sylvester', 'Yosemite Sam', 'Foghorn Leghorn']
first_char_name = list(filter(lambda name: name.startswith('E') or name.startswith('T'), looney_tunes))
print(first_char_name)
last_char_name = list(filter(lambda name: name.endswith('y') or name.endswith('g'), looney_tunes))
print(last_char_name)
two_name = list(filter(lambda name: ' ' in name, looney_tunes))
print(two_name)
only_alpha = list(filter(lambda name: name.isalpha(), looney_tunes))
print(only_alpha)

def isalpha(name):
    return name.isalpha()
deflist = list(filter(isalpha, looney_tunes))
print(deflist)