#08.06.2026 - 22:10h
# Active Coding — Session
# Task 24
scores = [88, 72, 95, 61]
def get_reverse(nums):
    return nums[::-1]
print(get_reverse(scores))
# Task 25
clients = ["Ivan", "Maria", "Petar", "Georgi"]
def get_first_three(names):
    return names[:3]
print(get_first_three(clients))
# Task 26
orders = [10, 20, 30, 40, 50, 60]
def last_three_orders(orders):
    return orders[-3:]
print(last_three_orders(orders))
# Task 27
books = ["Nemo", "Atlantis", "Robin Hood", "Sherlock", "Odyssey"]
def get_gap(book):
    return book[::2]
print(get_gap(books))
# Task 28
movies = ['Legionaire', 'Batman', 'Wild Wild West', 'Avatar']
def favorite(movie):
    for i, movie in enumerate(movies, start=1):
        print(i, movie)
favorite(movies)
# Task 29
def test():
    print("A")
    return 100
    print("B")

print(test())