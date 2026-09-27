best_movies = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Star Wars']
my_choice = list(filter(lambda movie: 'The' not in movie, best_movies))
my_second_choice = list(filter(lambda movie: movie.startswith('S'), best_movies))
my_third_choice = list(filter(lambda movie: len(movie) > 4 and 'Dark' in movie, best_movies))

print(my_choice)
print(my_second_choice)
print(my_third_choice)

uppercase_movies = list(map(lambda movie: movie.upper(), best_movies))
print(uppercase_movies)