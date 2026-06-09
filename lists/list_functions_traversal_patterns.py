#09.06.2026 - 23:05h
# Functions + Traversal
# Active Coding — Session 5
# Task 38
names = ["Ivan", "Maria", "Petar"]
def get_name(name_list):
    for name in name_list:
        print(name)
get_name(names)
# Task 39
cities = ["Sofia", "Varna", "Plovdiv"]
def print_all_cities(city_list):
    for city in city_list:
        print(f'Град: {city}')
print_all_cities(cities)
# Task 40
scores = [88, 72, 95, 61]
def all_scores(score_list):
    for score in score_list:
        print(f'Резултат, както следва: {score}')
all_scores(scores)
# Task 41
books = ["Nemo", "Atlantis", "Robin Hood", "Sherlock"]
books_2 = ["Pinochio", "Zorro", "Hercules", "Snow White"]
def my_books(books_list):
    for i, book in enumerate(books_list, start=1):
        print(f'Book {i}: {book}')
my_books(books)
my_books(books_2)#исках да тествам как работи преизползването на кода чрез функцията
# Task 42
clients = ["Ivan", "Maria", "Petar"]
payments = [120, 180, 90]
def name_and_value(items_1, items_2):
    for name, payment in zip(items_1, items_2):
        print(f'{name} -> {payment}')
name_and_value(clients, payments)
# Task 43 — Real World
addresses = ['Lozenets', 'Nadejda', 'Malinova dolina', 'Center', 'Paradise']
fees = [51, 50, 80, 100, 80]
def show_clients_rentability(analysis_1, analysis_2):
    for i, (address, fee) in enumerate(zip(analysis_1, analysis_2), start=1):
        print(f'№{i}: Адрес: {address}, Такса: {fee}')
show_clients_rentability(addresses, fees)
# в моя Task 43 — Real World логиката ми не се получи на 100%, не знам как да направя функция която да ползва enumerate и zip така че да печата i, и елементи от двата list-a
def show(items):
    for item in items:
        print(item)

show(["A", "B", "C"])
#Output
# A
# B
# C
#Край 0:06h