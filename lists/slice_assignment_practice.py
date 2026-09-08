numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers[::] = [888]
print(numbers)

formula_one_teams = ['Mercedes1', 'Red Bull Racing', 'Ferrari', 'McLaren1', 'Alpine', 'Aston Martin', 'AlphaTauri1', 'Haas', 'Alfa Romeo', 'Williams1']

formula_one_teams[::3] = ['Tom', 'Jerry', 'Spike', 'Bugs']
print(formula_one_teams)
data = [1, 2, 3, 4, 5, 6, 7, 8]
data[1:-1] = data[-2:0:-1]
data[2:-2] = 'Tom',
print(data)

def ranking(name):
    if name.startswith('A') or name.endswith('e'):
        return name.upper()
top_five_singers = ['Adele', 'Beyonce', 'Rihanna', 'Taylor Swift', 'Lady Gaga']
ranking = list(filter(ranking, top_five_singers))
 
print(ranking)
