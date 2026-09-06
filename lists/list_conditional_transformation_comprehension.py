barcelona_top_scorers = ['Lionel Messi', 'Luis Suárez', 'Neymar Jr', 'ronaldinho', 'Samuel Eto\'o', 'Hristo Stoichkov', 'Johan Cruyff', 'romário', 'David Villa', 'Thierry Henry']
top_of_them = [name.upper() if name.startswith('H') or name.startswith('L') else name.title() if name.startswith('R') or name.startswith('r') else name for name in barcelona_top_scorers]
print(top_of_them)