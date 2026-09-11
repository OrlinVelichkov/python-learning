oscar_winners = ["meryl Streep", "Jack Nicholson", "ingrid Bergman"]
newspaper = list(map(str.upper, filter(lambda name: name.lower().startswith('j'), oscar_winners)))
newspaper.insert(0, 'Tom Cruise')
print(newspaper)

teams = [
    ["Michael Jordan", "Magic Johnson"],
    ["Larry Bird", "LeBron James"],
    ["Kobe Bryant", "Shaquille O'Neal"],
    ["Tim Duncan", "Kevin Garnett"]]
pro_teams = any(any(name.split()[-1] == "Johnson" for name in group) for group in teams)
print(pro_teams)